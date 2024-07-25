
import numpy as np
#import pickle
import pandas as pd
import joblib
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

joblib_in= open("Mane22222.joblib","rb")
classifier=joblib.load(joblib_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(gender, age, no_of_days_subscribed, multi_screen,
                                mail_subscribed, weekly_mins_watched, minimum_daily_mins,
                                maximum_daily_mins, weekly_max_night_mins, videos_watched,
                                maximum_days_inactive, customer_support_calls):
   
    prediction=classifier.predict([[gender, age, no_of_days_subscribed, multi_screen,
                                    mail_subscribed, weekly_mins_watched, minimum_daily_mins,
                                    maximum_daily_mins, weekly_max_night_mins, videos_watched,
                                    maximum_days_inactive, customer_support_calls]])
    print(prediction)
    return prediction



def main():
    st.title("Churn Data by Decision Tree")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit DECISION TREE ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    gender = st.text_input("gender","Type Here")
    age = st.text_input("age","Type Here")
    no_of_days_subscribed = st.text_input("no_of_days_subscribed","Type Here")
    multi_screen = st.text_input("multi_screen","Type Here")
    mail_subscribed = st.text_input("mail_subscribed","Type Here")
    weekly_mins_watched = st.text_input("weekly_mins_watched","Type Here")
    minimum_daily_mins = st.text_input("minimum_daily_mins","Type Here")
    maximum_daily_mins = st.text_input("maximum_daily_mins","Type Here")
    weekly_max_night_mins = st.text_input("weekly_max_night_mins","Type Here")
    videos_watched = st.text_input("videos_watched","Type Here")
    maximum_days_inactive = st.text_input("maximum_days_inactive","Type Here")
    customer_support_calls = st.text_input("customer_support_calls","Type Here")
    
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(eval(gender), eval(age), eval(no_of_days_subscribed), 
                                           eval(multi_screen),eval(mail_subscribed), eval(weekly_mins_watched), 
                                           eval(minimum_daily_mins), eval(maximum_daily_mins),
                                           eval(weekly_max_night_mins), eval(videos_watched), eval(maximum_days_inactive),
                                           eval(customer_support_calls))
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("This is about Churn Dataset by Decision Tree")

if __name__=='__main__':
    main()
    
    
    