import streamlit as slt
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris  

@slt.cache
def load_data():
    iris=load_iris()
    df=pd.DataFrame(iris,data,columns=iris.feature_names)
    df['species']=iris.target
    return df,iris.target_names

df,target_name=load_data()

model=RandomForestClassifier()
model.fit(df.iloc[:,:-1],df['species'])

slt.sidebar.title("Input Features")

