import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.colored_header import colored_header

#----INTRO SECTION----#
colored_header(
    label="My Professional Journey",
    description="",
    color_name="red-70",
)
# Functionalities to be implemented
st.subheader("About Me")

col1, col2 = st.columns(2)
with col1:
  st.link_button("View Portfolio", "https://www.datascienceportfol.io/Habiba_ElKeraby")
with col2:
  st.link_button("View LinkedIn Profile", "https://www.linkedin.com/in/habiba-el-keraby-7839b3194/")

st.markdown('''I'm a versatile and curious Electrical & Computer Systems Engineering graduate, driven by the pursuit of knowledge and a commitment to professional growth. As a Junior Data Scientist at Appsaya Technologies, my work involves database management, data analysis & visualization, and utilizing ML & NLP tools for the creation of innovative business matching solutions. 

Beyond my current professional activity, I've taught Arabic to students of various ages and levels and worked on Deep Learning COVID-19 detection methods in chest X-ray images during my time at Monash University. My journey is defined by a quest for learning, and I invite you to explore the intersection of engineering and my creative hobbies with me.''')

#----TECHINCAL PROFILE SECTION----#
colored_header(
    label="Technical Profile",
  description="",
    color_name="red-70",
)
col1, col2 = st.columns(2)
with col1:
  st.markdown("**Programming Languages**")
with col2:
  st.markdown("Python, SQL, C, MATLAB, R")
st.divider()
col1, col2 = st.columns(2)
with col1:
  st.markdown("**Academic Interests**")
with col2:
  st.markdown("Natural Language Processing, Machine Learning, Data Visualization")
st.divider()
col1, col2 = st.columns(2)
with col1:
  st.markdown("**Data Visualization**")
with col2:
  st.markdown("Tableau Public, PowerBI, matplotlib, seaborn")
st.divider()
col1, col2 = st.columns(2)
with col1:
  st.markdown("**Database & Version Control**")
with col2:
  st.markdown("MySQL, Github")
st.divider()
col1, col2 = st.columns(2)
with col1:
  st.markdown("**Tools & Libraries**")
with col2:
  st.markdown("Numpy, Pandas, Scikit-Learn, Tensorflow, NLTK, Keras, PyTorch, Streamlit, Google Colaboratory, Replit, Rstudio")
st.divider()