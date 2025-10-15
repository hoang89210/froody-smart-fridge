import cv2
import tensorflow as tf
import pandas as pd
import json

model = tf.keras.models.load_model('models/froody_detector.h5')
classes = ['thit_bo', 'rau_muong', 'trai_cay']  # Từ train

def scan_fridge(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224,224))
    pred = model.predict(img.reshape(1,224,224,3))
    detected = classes[pred.argmax()]
    
    # Lookup nutrition
    with open('data/raw/nutrition.json') as f:
        nutrition = json.load(f)
    info = next((item for item in nutrition if detected in item['name'].lower()), {})
    
    # Suggest
    suggestion = f"Detected: {detected}. Cal: {info.get('calories',0)}. Expiry: {info.get('expiry_days',0)} days. Recipe: Grill thịt bò low-cal!"
    print(suggestion)
    return suggestion

if __name__ == "__main__":
    scan_fridge('test_image.jpg')  # Thay bằng ảnh tủ lạnh sim