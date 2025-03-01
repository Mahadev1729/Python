import streamlit as st 

st.title("streamlit text input")

name=st.text_input("Enter your name")

age=st.slider("Select your age:",0,100,25)


st.write(f"your age is {age}")
if name:
    st.write(f"hello,{name}")
else:
    st.write(f"Hello,unknown")    
