import streamlit as st 
import pandas as pd

st.title("streamlit text input")

name=st.text_input("Enter your name")

age=st.slider("Select your age:",0,100,25)

options= [
    "Select below one","Python", "JavaScript", "Java", "C", "C++", "C#", "Swift", "Go", "Rust", 
    "Kotlin", "TypeScript", "Ruby", "PHP", "Perl", "R", "Dart", "Scala", 
    "Haskell", "Lua", "Elixir", "Clojure", "F#", "Objective-C", "Visual Basic",
    "MATLAB", "Julia", "Shell", "Bash", "PowerShell", "Groovy", "Erlang",
    "Lisp", "Scheme", "Prolog", "COBOL", "Fortran", "Ada", "Pascal", "ABAP",
    "RPG", "ActionScript", "ML", "OCaml", "Tcl", "Smalltalk", "Crystal",
    "Forth", "PL/SQL", "FoxPro", "Modula-2", "Delphi", "Hack"
]

choice=st.selectbox("Choose your favorite language:",options)
st.write(f"You selected {choice}")

st.write(f"your age is {age}")


uploaded_file=st.file_uploader("Choose a csv file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
 
