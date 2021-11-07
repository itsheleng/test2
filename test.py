# helloworld.py
#import the library
import streamlit as st
import altair as alt
import pandas as pd
import streamlit.components.v1 as components
import datetime
import streamlit as stl
import numpy as np

# add title
st.title('CEI 523 Assignment 2021 📈')
st.info('Case study for our given data for predictive maintenance')


st.text("")
st.text("")

from IPython.display import display

file = "data.csv"
opened = open(file, "r")
readed = pd.read_csv(file)
print(readed)

st.sidebar.text("")
st.sidebar.text("")
st.sidebar.title("🔗 Sources")
st.sidebar.info('[Given Data](https://drive.google.com/file/d/1cEMvten1WEJTae9xRw0JNezHrZZhhT9o/view?usp=sharing)'+'\r')

st.sidebar.title("🛈 About") 
st.sidebar.info('Created and maintained by:'+'\r'+'[Eleni Giakoumi](eg.giakoumi@edu.cut.ac.cy)'+'[ Andreas Othonos](am.othonos@edu.cut.ac.cy)'+'[ Andriani Petrou](ae.petrou@edu.cut.ac.cy)')



