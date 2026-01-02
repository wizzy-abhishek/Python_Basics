import streamlit as st

st.title("Hello, I am Abhishek Anand")

col1, col2 = st.columns([1,1])
with col2:
    st.image("assets/MyImage.png")


st.text("I am a software enginner.\n"\
        "I love to develop applications that are robust, innovative, and architecturally strong.")