# 🍽️ Restaurant Rating Prediction App

A professional Machine Learning web application that predicts restaurant ratings based on operational features such as average cost, table booking availability, online delivery, and price range.

Built using Python and deployed with Streamlit, this project demonstrates end-to-end ML workflow — from preprocessing to real-time prediction with a modern UI.

---

## 🚀 Live Features

✅ Real-time rating prediction  
✅ Interactive sliders & controls  
✅ StandardScaler preprocessing  
✅ Clean enterprise-style UI  
✅ Confidence estimation  
✅ Machine learning inference via trained model  

---

## 🧠 Machine Learning Overview

The application uses a pre-trained ML model (`mlmodel.pkl`) with the following input features:

- Average Cost for Two  
- Table Booking (Yes / No)  
- Online Delivery (Yes / No)  
- Price Range (1–4)

### Prediction Categories

| Score Range | Label |
|------------|-------|
| < 2.5 | Poor 😞 |
| 2.5 – 3.5 | Average 🙂 |
| 3.5 – 4.0 | Good 😊 |
| 4.0 – 4.5 | Very Good 😁 |
| > 4.5 | Excellent 🤩 |

---

## 🛠️ Tech Stack

- Python  
- NumPy  
- Joblib  
- :contentReference[oaicite:0]{index=0}  
- :contentReference[oaicite:1]{index=1}  

---

## ⚙️ Installation & Setup

 
1️⃣ Clone Repository

git clone https://github.com/hasnaa03/restaurant-rating-predictor.git
cd restaurant-rating-predictor

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Application
streamlit run app.py
App will open automatically in your browser.


📊 Example Input

Average Cost: 1000
Table Booking: Yes
Online Delivery: No
Price Range: 3

➡️ Output: Predicted rating with confidence score.

🎯 Learning Outcomes

Building production-ready ML applications
Feature scaling using StandardScaler
Model deployment with Streamlit
UI customization using CSS
Real-time inference
End-to-end ML workflow

🌟 Future Improvements

Add dataset upload option
Include visual analytics dashboards
Model comparison (Random Forest / XGBoost)
Cloud deployment
User authentication

⭐ If you like this project, don’t forget to star the repository!

https://github.com/hasnaa03/Restaurant-Rating-Prediction-App/blob/main/Screenshot%202026-02-15%20144525.png

https://github.com/hasnaa03/Restaurant-Rating-Prediction-App/blob/main/Screenshot%202026-02-15%20144735.png
