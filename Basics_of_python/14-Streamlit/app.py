import streamlit as st 
import pandas as pd 
import numpy as np 

## Title of the application
st.title("hello streamlit")

## display simple text

st.write("This is a simple")

## for dataframe

df=pd.DataFrame({
    'first col':[1,2,3,4],
    'second col':[10,20,30,40]
})



## display the dataframe

st.write("Here is dataframe")
st.write(df)


##create line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)

