import streamlit as st 
import joblib
import numpy as np

model=joblib.load('model.pkl')

st.title('Student Performance ')

f1=st.number_input('Hours studied',min_value=0.0,max_value=24.0,step=0.5)
f2=st.number_input('Previous score',min_value=0.0,max_value=100.0,step=1.0)
extra = st.selectbox("Extracurricular Activities", ["Yes", "No"])
extra_encoded = 1.0 if extra == "Yes" else 0.0

f4=st.number_input('Sleep Hours',min_value=0.0,max_value=24.0,step=1.0)
f5=st.number_input('Sample Question papers practiced',min_value=0.0,max_value=10.0,step=1.0)
if st.button("Predict"):
    data = np.array([[f1, f2, extra_encoded,f4,f5]])
    prediction = model.predict(data)
    st.success(f"Prediction: {prediction[0]}")
