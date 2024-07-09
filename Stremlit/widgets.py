import streamlit as st
import pandas as pd

st.title("streamlit text input")
name = st.text_input("Enter your name :-")

age=st.slider("Select your age:",0,100,25)

options =['python','java','c','c++']
choices = st.selectbox("choose your fav programming language",options)

if name:
    st.write(f'Hello,{name}')

uplodaded_file = st.file_uploader("Hey choose a csv file",type="csv")
if uplodaded_file:
    df = pd.read_csv(uplodaded_file)
    st.write(df)
