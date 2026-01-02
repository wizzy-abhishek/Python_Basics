import streamlit as st
import pandas as pd

st.title("Widgets In Streamlit")

uploaded_file = st.file_uploader("Enter a csv file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.to_csv("sample.csv")
    st.write(df)

option = ("Java", "Python", "Rust", "Go", "C++")
a = st.selectbox("Select one lang:", options=option)
st.warning(f"You have selected {a}")