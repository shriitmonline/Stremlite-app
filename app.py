
import streamlit as st
# import pandas as pd
# from sklearn import datasets
# from sklearn.ensemble import RandomForestClassifier
# import pickle

st.write("""
# ODD EVEN PREDICTOR

This app predicts if number is odd or even
""")
#Get Input

st.header('User Input Number')

def user_input_features():
   
    Number = st.number_input("Your Number",min_value=0,max_value=2000000000,step=1)
    return Number

num = user_input_features()
st.subheader('Output')
if(num%2==0):
  st.write("# Number is Even")
else:
  st.write("# Number is Odd")
