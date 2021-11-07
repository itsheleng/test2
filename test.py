# test1.py
#import the library
import streamlit as st
import altair as alt
import streamlit.components.v1 as components
import datetime
import streamlit as stl
import numpy as np
impport pandas as pd


# add title
st.title('CEI 523 Assignment 2021 📈')
st.info('Case study for our given data for predictive maintenance')
st.text("")
st.text("")

dataset = pd.read_csv('https://github.com/itsheleng/test2/blob/3f6d2c0cfbdbeebbf2f6fb07fbdbee577004479c/data.csv')


st.sidebar.text("")
st.sidebar.text("")
st.sidebar.title("🔗 Sources")
st.sidebar.info('[Given Data](https://drive.google.com/file/d/1cEMvten1WEJTae9xRw0JNezHrZZhhT9o/view?usp=sharing)'+'\r')

st.sidebar.title("🛈 About") 
st.sidebar.info('Created and maintained by:'+'\r'+'[Eleni Giakoumi](eg.giakoumi@edu.cut.ac.cy)'+'[ Andreas Othonos](am.othonos@edu.cut.ac.cy)'+'[ Andriani Petrou](ae.petrou@edu.cut.ac.cy)')



