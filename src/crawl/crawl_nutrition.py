import os
import requests
import json
from bs4 import BeautifulSoup
import urllib.request
import argparse

def crawl_nutrition(query, api_key='DEMO_KEY', output_json='data/raw/nutrition.json'):
    """Crawl USDA API for food nutrition."""
    url = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={api_key}&query={query}"
    response = requests.get(url)
    data = response.json()
    
    foods = []
    for food in data['foods'][:5]:  # Top 5 matches
        info = {
            'name': food['description'],
            'calories': food.get('foodNutrients', [{}])[0].get('value', 0) if food.get('foodNutrients') else 0,
            'protein': next((nut['value'] for nut in food.get('foodNutrients', []) if 'Protein' in nut['nutrientName']), 0),
            'expiry_days': 7  # Mock, real từ DB
        }
        foods.append(info)
    
    os.makedirs('data/raw', exist_ok=True)
    with open(output_json, 'w') as f:
        json.dump(foods, f, indent=4)
    print(f"Crawled nutrition for '{query}': {len(foods)} items")

def crawl_images(query, num=20, output_dir='data/raw/images'):
    """Crawl images from Google."""
    os.makedirs(output_dir, exist_ok=True)
    search_url = f"https://www.google.com/search?q={query}+food&tbm=isch"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    imgs = soup.find_all('img')[:num]
    
    for i, img in enumerate(imgs):
        try:
            src = img['src']
            if src.startswith('http'):
                urllib.request.urlretrieve(src, os.path.join(output_dir, f"{query}_{i}.jpg"))
        except:
            pass
    print(f"Crawled {num} images for '{query}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', required=True)
    parser.add_argument('--num_images', default=20)
    args = parser.parse_args()
    
    crawl_nutrition(args.query)
    crawl_images(args.query, args.num_images)