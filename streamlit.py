from turtle import st

import streamlit as st
import pandas as pd

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_training = st.beta_container()
with header:
    st.title('Welcome to Book Recommendation System')


with dataset:
    st.header('Best Books of The 21st Century Dataset')
    dataset = pd.read_csv("BRS-Dataset/Best_Book_21st.csv")
##    st.write(dataset.head())

    st.dataframe(dataset.head(10))
    st.subheader('Author and Publisher')
    author = (dataset['publisher'].head(30))
    st.bar_chart(author)

with features:
    st.header('The features I created')

    st.markdown('')

with model_training:
    st.header('Select your Ratings')
    # st.text('Select your Ratings')

    sel_col, disp_col = st.beta_columns(2)

    Horror = sel_col.slider('Horror', 1, 10)
    Romance = sel_col.slider('Romance', 1, 10)
    Thriller = sel_col.slider('Thriller', 1, 10)
    Non_Fiction = sel_col.slider('Non_Fiction', 1, 10)
