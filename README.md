# Froody 🧊🤖 – Smart Fridge AI Tracker

[<image-card alt="Python" src="https://img.shields.io/badge/Python-3.8%2B-blue" ></image-card>](https://python.org)
[<image-card alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-2.13-orange" ></image-card>](https://tensorflow.org)
[<image-card alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green" ></image-card>](https://opensource.org/licenses/MIT)
[<image-card alt="Stars" src="https://img.shields.io/github/stars/[username]/froody-smart-fridge?style=social" ></image-card>](https://github.com/[username]/froody-smart-fridge)

**Froody** là app tủ lạnh thông minh: Scan camera detect thực phẩm VN, crawl nutrition data, train model suggest recipe & expiry alert. Chill cho giảm cân – "Fridge nói: Ăn salad đi mày!"

<image-card alt="Demo GIF" src="images/demo.gif" ></image-card> <!-- Upload GIF chạy scan -->

## 🚀 Features
- **Crawl Data**: Nutrition + images từ USDA/Google cho thịt bò, rau củ VN.
- **Train Model**: CNN detect food (acc ~85%).
- **Fridge Scan**: Sim OpenCV predict + suggest low-cal recipe.
- **Expiry Track**: Alert hỏng dựa trên days.

## 🛠 Quick Start
1. Clone: `git clone https://github.com/[username]/froody-smart-fridge.git`
2. Install: `pip install -r requirements.txt`
3. Crawl: `python src/crawl/crawl_nutrition.py --query "rau bina"`
4. Train: `python src/train/train_model.py --epochs 10`
5. Scan: `python src/inference/fridge_scan.py`

## 📊 Example Output
| Food      | Calories | Expiry | Suggestion     |
|-----------|----------|--------|----------------|
| Thịt Bò  | 250     | 5 days| Grill w/ salad |
| Rau Muống| 20      | 3 days| Stir-fry light |

## 🤝 Contribute
Fork → PR to dev. Add VN recipes!

**Star nếu xịn! 🌟** Issues? Open up.