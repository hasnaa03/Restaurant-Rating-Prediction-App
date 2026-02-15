import streamlit as st
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Restaurant Rating",
    page_icon="🍽️",
    layout="wide"
)

model = joblib.load("mlmodel.pkl")
scaler = StandardScaler()

# ================= CUSTOM CSS =================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.header {
background: linear-gradient(90deg,#667eea,#764ba2);
padding:30px;
border-radius:15px;
color:white;
text-align:center;
}

.card {
background:#ffffff;
padding:25px;
border-radius:20px;
box-shadow:0px 6px 18px rgba(0,0,0,0.1);
}

.result {
background: linear-gradient(120deg,#89f7fe,#66a6ff);
padding:30px;
border-radius:25px;
text-align:center;
color:black;
box-shadow:0px 8px 25px rgba(0,0,0,0.2);
}

.metric {
background:linear-gradient(120deg,#f093fb,#f5576c);
padding:20px;
border-radius:15px;
color:white;
text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("""
<div class="header">
<h1>🍽️ Restaurant Rating Prediction App</h1>
<p>Professional Machine Learning Prediction System</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ================= SIDEBAR =================
st.sidebar.title("⚙️ Controls Panel")

averagecost = st.sidebar.slider("💰 Average Cost for Two",50,15000,1000,100)

tablebooking = st.sidebar.selectbox("📖 Table Booking",["Yes","No"])

onlinedelivery = st.sidebar.selectbox("🚚 Online Delivery",["Yes","No"])

pricerange = st.sidebar.select_slider("💎 Price Range",[1,2,3,4])

predict = st.sidebar.button("🚀 Run Prediction")

# ================= METRICS =================
m1,m2,m3,m4 = st.columns(4)

with m1:
    st.markdown(f"<div class='metric'>💰 Cost<br><h2>{averagecost}</h2></div>",unsafe_allow_html=True)
with m2:
    st.markdown(f"<div class='metric'>📖 Booking<br><h2>{tablebooking}</h2></div>",unsafe_allow_html=True)
with m3:
    st.markdown(f"<div class='metric'>🚚 Delivery<br><h2>{onlinedelivery}</h2></div>",unsafe_allow_html=True)
with m4:
    st.markdown(f"<div class='metric'>💎 Range<br><h2>{pricerange}</h2></div>",unsafe_allow_html=True)

st.write("")

# ================= MAIN =================
left,right = st.columns([1,1])

with left:
    st.markdown("<div class='card'><h3>📊 Model Information</h3>",unsafe_allow_html=True)
    st.write("""
    • Machine Learning Based Prediction  
    • StandardScaler Normalization  
    • Real-Time Classification  
    • Enterprise UI Design  
    """)
    st.markdown("</div>",unsafe_allow_html=True)

with right:

    if predict:

        booking = 1 if tablebooking=="Yes" else 0
        delivery = 1 if onlinedelivery=="Yes" else 0

        data = scaler.fit_transform(np.array([[averagecost,booking,delivery,pricerange]]))

        with st.spinner("🤖 AI is thinking..."):
            st.progress(70)

        pred = model.predict(data)[0]

        if pred < 2.5:
            label="😞 Poor"
        elif pred < 3.5:
            label="🙂 Average"
        elif pred < 4:
            label="😊 Good"
        elif pred < 4.5:
            label="😁 Very Good"
        else:
            label="🤩 Excellent"

        confidence = min(95,round(pred*20,1))

        st.markdown(f"""
        <div class='result'>
        <h1>{label}</h1>
        <h3>Rating Score: {round(float(pred),2)}</h3>
        <h4>Confidence: {confidence}%</h4>
        </div>
        """,unsafe_allow_html=True)

        st.balloons()

# ================= FOOTER =================
st.write("")
st.caption("© 2026 Restaurant Rating AI | Designed for Professional ML Projects")
