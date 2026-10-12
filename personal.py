import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.colored_header import colored_header
#from streamlit_card import card

st.set_page_config(layout="wide")

#----PERSONAL INTERESTS SECTION----#
colored_header(
    label="My Personal Interests",
    description="The things I enjoy learning, making, and exploring beyond my professional work",
    color_name="red-70"
)

c1,c2,c3,c4,c5, c6 = st.columns(6)
with c1:
  st.markdown('##### Crochet 🧶')
with c2:
  st.markdown('##### Embroidery 🧵')
with c3:
  st.markdown('##### Drawing 👩🏽‍🎨')
with c4:
  st.markdown('##### Poetry 📜')
with c5:
  st.markdown('##### Writing ✍🏼')
with c6:
  st.markdown('##### Photography 📸')

#----LANGUAGES SECTION----#
colored_header(
    label="Language Learning",
    description="The languages I speak, study, and continue to discover",
    color_name="red-70"
)

st.write(
    """
Language learning has been a constant part of my life. Some languages grew
from family and education, while others came through travel, culture,
friendships, and independent study. I continue to learn languages both as a
way of connecting with people and as a way of understanding the places and
cultures around me.
"""
)

languages = [
    ("Arabic", "Native"),
    ("French", "C2 / Native-like"),
    ("English", "C2 / Native-like"),
    ("Spanish", "C2 / Proficient"),
    ("Persian", "C1 / Advanced"),
    ("Portuguese", "B2–C1 / Upper Intermediate–Advanced"),
    ("Mandarin Chinese", "A2–B1 / Lower Intermediate"),
    ("Turkish", "A1-A2 / Elementary"),
    ("Italian", "A1-A2 / Elementary"),
]

language_cols = st.columns(2)

for i, (language, level) in enumerate(languages):
    with language_cols[i % 2]:
        st.markdown(f"**{language}**")
        st.caption(level)


st.divider()

#----MAP SECTION----#
colored_header(
    label="An Overview of My Journey Around the World",
    description="The places I've lived, traveled to, and wish to visit",
    color_name="red-70",
)

df_born = df = pd.DataFrame(
    [
      [30.0443879, 31.2357257, 250, "#C6A15B"],# Cairo
    ],
    columns=["lat","long","size","col"]
)

df_live = pd.DataFrame(
    [
      [48.945820, 2.172220, 200, "#1a87bc"],# Sartrouville
      [26.3039999, 50.1960237, 200, "#1a87bc"],# Al Khubar
      [25.204849, 55.270782, 200, "#1a87bc"],# Dubai
      [51.507351, -0.127758, 200, "#1a87bc"],# London
      [3.1516964, 101.6942371, 200, "#1a87bc"],# KL
      [23.5880, 58.3829, 200, "#1a87bc"],# Muscat
      [30.5728, 104.0668, 200, "#1a87bc"],# Chengdu
    ],
    columns=["lat","long","size","col"]
)

df_visit = pd.DataFrame([
  [31.1991806, 29.8951716, 50, "#3265ff"],# Alexandria
  [27.8539447, 34.3021011, 50, "#3265ff"],# Sharm
  [27.222556, 33.8307062, 50, "#3265ff"],# Hurgada
  [37.3886303, -5.9953403, 50, "#3265ff"],# Seville
  [40.4167047, -3.7035825, 50, "#3265ff"],# Madrid
  [37.8845813, -4.7760138, 50, "#3265ff"],# Cordoba
  [37.1742210, -3.5990428, 50, "#3265ff"],# Granada
  [36.7213028, -4.4216366, 50, "#3265ff"],# Malaga
  [36.1285933, -5.3474761, 50, "#3265ff"],# Gibraltar
  [45.6256764, 9.0373283, 50, "#3265ff"],# Saronno
  [45.9394759, 9.1494101, 50, "#3265ff"],# Como
  [46.0050102, 8.9520281, 50, "#3265ff"],# Lugano
  [46.1695739, 8.7954859, 50, "#3265ff"],# Locarno
  [41.006381, 28.9758715, 50, "#3265ff"],# Istanbul
  [40.6212099, 31.6460259, 50, "#3265ff"],# Bolu
  [38.6582232, 35.5546374, 50, "#3265ff"],# Kayseri
  [38.646806, 34.8491554, 50, "#3265ff"],# Cappadocia
  [36.8864752, 30.7029585, 50, "#3265ff"],# Antalya
  [37.7833152, 29.0844832, 50, "#3265ff"],# Denizli
  [39.2387054, 28.1749129, 50, "#3265ff"],# Sindirgi
  [24.4538352, 54.3774014, 50, "#3265ff"],# Abu Dhabi
  [24.2248697, 55.7452211, 50, "#3265ff"],# Al Ain
  [26.2235041, 50.5822436, 50, "#3265ff"],# Manama
  [24.4686175, 39.6110134, 50, "#3265ff"],# Al-Madinah
  [21.420847, 39.826869, 50, "#3265ff"],# Makkah
  [6.3700386, 99.7928634, 50, "#3265ff"],# Langkawi
  [1.357107, 103.8194992, 50, "#3265ff"],# Singapore
  [29.7589382, -95.3676974, 50, "#3265ff"],# Houston

  # New places visited
  [22.9333, 57.5333, 50, "#3265ff"],# Nizwa
  [39.9042, 116.4074, 50, "#3265ff"],# Beijing
  [29.5918, 52.5837, 50, "#3265ff"],# Shiraz
  [35.6892, 51.3890, 50, "#3265ff"],# Tehran
  [36.2605, 59.6168, 50, "#3265ff"],# Mashhad
],
  columns=["lat","long","size","col"]
)

df_tovisit = pd.DataFrame(
    [
      [4.099917, -72.9088133, 50, "#d132ff"],# Colombia
      [-6.8699697, -75.0458515, 50, "#d132ff"],# Peru
      [34.6401861, 39.0494106, 50, "#d132ff"],# Syria
      [33.8750629, 35.843409, 50, "#d132ff"],# Lebanon
      [31.1667049, 36.941628, 50, "#d132ff"],# Jordan
      [32.0254688, 35.2888075, 50, "#d132ff"],# Palestine
      [33.7680065, 66.2385139, 50, "#d132ff"],# Afghanistan

    ],
    columns=["lat","long","size","col"]
)

map_view = st.selectbox(
   "Select different map views:",
   ("View All", "Places I\'ve lived", "Places I\'ve visited", "Places I wish to visit", "Where I was born"),
)

if map_view=="View All":
  st.map(pd.concat([df_live, df_visit, df_tovisit, df_born],axis=0, ignore_index=True),
    latitude='lat',
    longitude='long',
    size='size',
    color='col',
    zoom=2
    )
elif map_view=="Places I\'ve lived":
  st.map(df_live,
    latitude='lat',
    longitude='long',
    size='size',
    color='col',
    zoom=2
    )
elif map_view=="Places I've visited":
  st.map(df_visit,
        latitude='lat',
        longitude='long',
        size='size',
        color='col',
        zoom=2
        )
elif map_view=="Places I wish to visit":
  st.map(df_tovisit,
        latitude='lat',
        longitude='long',
        size='size',
        color='col',
        zoom=2
        )
else:
  st.map(df_born,
    latitude='lat',
    longitude='long',
    size='size',
    color='col',
    zoom=6
    )

