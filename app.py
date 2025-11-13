import joblib
import numpy as np
import pandas as pd
import streamlit as st

model = joblib.load('gbr.pkl')
saved_column = joblib.load('model_columns.pkl')

#Page Configuration
st.set_page_config(
    page_title='Health Insurance',
    page_icon='🏥',
    layout='centered',
    initial_sidebar_state='collapsed'
)

#Page style
st.markdown(
        """
    <style>
    .main-title {
        text-align: center;
        color: #D2042D;
        font-size: 40px;
        font-weight: bold;
    }
    .sub-title {
        text-align: center;
        font-size: 18px;
        color: #555;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='main-title'>🏥 Health Insurance Charges</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>An intelligent health insurance calculation tool powered by Machine Learning</p>", unsafe_allow_html=True)

st.subheader('Enter Patient Details')

age = st.number_input('Age: ', 18,100)
sex = st.selectbox('Sex: ', ['Male', 'Female'])
bmi = st.number_input('Body Mass Index: ', 10,70)
children = st.selectbox('No. oc Children: ', [0,1,2,3,4,5,6,7,8])
smoker = st.selectbox('Smoker? ', ['No', 'Yes'])
region = st.selectbox('Region: ', ['NorthWest', 'NorthEast', 'SouthWest', 'SouthEast'])

sex = 0 if sex=='Male' else 1
smoker = 0 if smoker=='No' else 1

if st.button('Calculate'):
    user_input = {
        'age' : age, 
        'sex' : sex, 
        'bmi' : bmi, 
        'children' : children, 
        'smoker' : smoker, 
        'region' : region
        }
    new_df = pd.DataFrame([user_input])
    new_df = pd.get_dummies(new_df, columns=['region'])
    new_df = new_df.reindex(columns=saved_column, fill_value=0)
    prediction = model.predict(new_df)[0]
    st.markdown(
        f"""
        <div style="background-color:#F4F6F7;padding:20px;border-radius:10px;border:2px solid #AAB7B8;">
            <h3 style="color:#2E4053;text-align:center;">💰 Estimated Insurance Cost:</h3>
            <h2 style="color:red;text-align:center;">${prediction:,.2f}</h2>
            <h5 style="color:#2E4053;text-align:center;">💡 This is an estimated cost based on your provided details.</h5>
        </div>
        """,
        unsafe_allow_html=True
    )
    
#Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>Made by Emmanuel | Powered by Gradient Boosting Regressor</p>", unsafe_allow_html=True)