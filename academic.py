import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.colored_header import colored_header
from streamlit_dynamic_filters import DynamicFilters

#----INTRO SECTION----#
colored_header(
    label="My Academic Journey",
    description="",
    color_name="red-70",
)

st.markdown('''In my opinion, learning is a continuous, life-long journey. Whether it is in the context of formal education, online courses or self-teaching, I enjoy discovering new topics and building up my skillset.
''')

tab1, tab2= st.tabs(["Formal Education", "Online Courses"])

with tab1:

  st.markdown('#### Bachelor\'s of Electrical & Computer Systems Engineering')
  st.markdown('##### Monash University (2017-2021)')
  # Filter by coursework category (Engineering, Computer Science, Natural Sciences)
  st.markdown('View Completed Coursework')
  data = {
    'Coursework Module': ['Engineering Industry Training',
                          'Professional Practice',
                          'Real-Time Embedded Systems',
                          'Analogue Electronics',
                          'Computer Systems',
                          'Electrical Energy Systems',
                          'Computer Organization & Programming',
                          'Electrical Circuits',
                          'Information & Networks',
                          'Engineering Design',
                          'Control System Design',
                          'Organic Electronics & Micro-Devices',
                          'Engineering Design',
                          'Leadership & Innovation',
                          'Digital Systems',
                          'Signals & Systems',
                          'Introduction to Systems Engineering',
                          'Physics for Engineers',
                          'Advanced Electromagnetics',
                          'Probability Models in Engineering',
                          'Advanced Engineering Mathematics',
                          'Computing for Engineers',
                          'Engineering Mobile Apps',
                          'IoT: Communication, Data & Security',
                          'Artificial Intelligence for Engineers',
                          'Computer Vision',
                          'Neural Networks & Deep Learning',
                         ],
    'Coursework Category': ['Engineering',
                            'Engineering',
                            'Engineering',
                            'Engineering',
                            'Engineering',
                            'Engineering',
                            'Engineering',
                            'Engineering',
                            'Engineering',
                            'Engineering',
                            'Engineering',
                            'Engineering',
                            'Engineering',
                            'Engineering',
                            'Engineering',
                            'Engineering',
                            'Engineering',
                            'Natural Sciences',
                            'Natural Sciences',
                            'Natural Sciences',
                            'Natural Sciences',
                            'Computer Science',
                            'Computer Science',
                            'Computer Science',
                            'Computer Science',
                            'Computer Science',
                            'Computer Science',
                           ],
    }

  df = pd.DataFrame(data)
  st.write(df)
 

with tab2:

  # Filter by: with certificate, no certificate, completed, in-progress
  # Filter by Platform: Coursera, Udemy, Kaggle, Other
  st.markdown('View Online Courses [Last Updated January 2024]')

  courses_df = pd.DataFrame(
    [
      ['Getting Started with Python - University of Michigan','Coursera','With Certificate','Completed'],
      ['Python Data Structures - University of Michigan','Coursera','With Certificate','Completed'],
      ['Mathematics for ML - Imperial College London','Coursera','With Certificate','Completed'],
      ['An Intuitive Introduction to Probability - University of Zurich','Coursera','With Certificate','Completed'],
      ['Introduction to Computer Science','Coursera','With Certificate','Completed'],
      ['Google Data Analytics Professional Certificate','Coursera','With Certificate','Completed'],
      ['Data Science, Machine Learning, Data Analysis, Python & R','Udemy','No Certificate','In Progress'],
      ['ChatGPT Quick Guide - Prompt Engineering, Plugins, and more!','Udemy','No Certificate','In Progress'],
      ['Soft skills to be happy and productive in science / academia','Udemy','No Certificate','In Progress'],
      ['The Art Of Winning People Over','Udemy','No Certificate','In Progress'],
      ['Public Speaking','Udemy','No Certificate','In Progress'],
      ['Secret Sauce of Great Writing','Udemy','No Certificate','In Progress'],
      ['Chess course from beginner to master level','YouTube','No Certificate','In Progress'],
      ['Python','Kaggle','With Certificate','Completed'],
      ['Intro to Machine Learning','Kaggle','With Certificate','Completed'],
      ['Pandas','Kaggle','With Certificate','Completed'],
      ['Data Cleaning','Kaggle','With Certificate','Completed'],
      ['Intermediate Machine Learning','Kaggle','With Certificate','In Progress'],
      ['Data Visualization','Kaggle','With Certificate','In Progress'],
      ['Generative AI Fundamentals','Google Cloud Skills Boost','With Certificate','In Progress'],
      ['Create Image Captioning Models','Google Cloud Skills Boost','With Certificate','In Progress'],
      ['Introduction to Large Language Models','Google Cloud Skills Boost','With Certificate','In Progress'],
      ['Transformer Models & BERT Model','Google Cloud Skills Boost','With Certificate','In Progress'],

    ],
    columns=["Course Name","Platform","Certificate","Status"]
)

  course_dynamic_filters = DynamicFilters(courses_df, filters=["Platform","Certificate","Status"])

  course_dynamic_filters.display_filters()
  course_dynamic_filters.display_df()