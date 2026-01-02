import streamlit as st 
import pandas as pd
import numpy as np 

st.title("Learning streamlit")

st.text("Let's learn streamlit and develop beautiful apps")

dataframe = pd.DataFrame({
    "First Col":[1,2,3,4],
    "Second Col":[10,20,30,40]
})

st.dataframe(dataframe)
st.write("The above data frame is dummy")

chart = pd.DataFrame(
    np.random.rand(20,3), columns=['Abhishek', 'Hari Om', 'Aman']
)
st.line_chart(chart, y_label="Data", x_label="Red", color=["#fd0", "#f0f", "#04f"])
