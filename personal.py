import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.colored_header import colored_header
#from streamlit_card import card

st.set_page_config(layout="wide")

#----PERSONAL INTERESTS SECTION----#
colored_header(
    label="My Personal Interests",
    description="",
    color_name="red-70",
)
st.link_button("View Creative Work", "https://instagram.com/selftaughtcreativity?utm_source=qr&igshid=MzNlNGNkZWQ4Mg%3D%3D")
c1,c2,c3,c4,c5 = st.columns(5)
with c1:
  st.markdown('##### Crochet 🧶')
with c2:
  st.markdown('##### Drawing 👩🏽‍🎨')
with c3:
  st.markdown('##### Poetry 📜')
with c4:
  st.markdown('##### Writing ✍🏼')
with c5:
  st.markdown('##### Photography 📸')

#----LANGUAGES SECTION----#
colored_header(
    label="Language Learning",
    description="The stories behind my language studies",
    color_name="red-70",
)

st.markdown('''Language learning is, for me, a passion and a lifelong journey. I see language learning as a tool for personal growth and an opportunity to broaden my horizons and deepen my understanding of the world and the people in it.
''')
st.markdown('#### Spoken Languages:')
c1,c2,c3,c4= st.columns(4)
with c1:
  st.markdown('##### Arabic')
  st.markdown('##### Persian')
with c2:
  st.markdown('##### English')
  st.markdown('##### Portuguese')
with c3:
  st.markdown('##### French')
  st.markdown('##### Italian')
with c4:
  st.markdown('##### Spanish')
  st.markdown('##### Turkish')
lang_sel = st.selectbox(
  "Select a language to learn more about my journey with it:",
  ("Arabic", "English", "French","Italian","Persian","Portuguese","Spanish","Turkish"),
  index=None, placeholder="Languages Spoken"
)
if lang_sel == "Arabic":
  st.markdown(''':red[Level:] Native, Fluent  
  I was born in Cairo, Egypt and grew up in a household where we communicated mostly in Arabic. Arabic is my mother tongue, and the first language I ever spoke. Aside from speaking and understanding many Arabic dialects, I am interested in Modern Standard Arabic, and enjoy reading and educating myself about Arabic literature.
  ''')
elif lang_sel == "English":
  st.markdown(''':red[Level:] Fluent  
  Like most non-native English speakers, I first learned English in school. My academic and professional careers have made English a language I use on a daily basis. I now consider it one of my native languages because of how comfortably I can express my thoughts and ideas and how long I have been speaking it.
  ''')
elif lang_sel == "French":
  st.markdown(''':red[Level:] Fluent  
  French was the second language I ever learned, as a little child in kindergarten. My primary and elementary education were completed in French schools. Having lived in France for around a decade, begin a French national and speaking French with my siblings on a daily basis, I consider French to be one of my native languages.
''')
elif lang_sel == "Italian":
  st.markdown(''':red[Level:] Intermediate  
  I became interested in learning Italian when I realized how similar it was to both French and Spanish, two languages I was already comfortable speaking. I found it easy to understand, which pushed me to put in effort to study the language in a more stuctured way. I studied it autonomously using online resources, and had the chance to interact with the language directly through a trip to Italy in the summer of 2019.
''')
elif lang_sel == "Persian":
  st.markdown(''':red[Level:] Proficient  
  After studying many European languages, I wanted to study a language that would bring me closer to my mother tongue. I was increasingly interested in Arabic literature and the ancient Islamic world, and Persian was an inevitable part of that. I was also very excited about the Persian language's seemingly easy grammar and the huge amount of vocabulary similarity it shared with Arabic. This is why I chose to study Persian as my seventh language. I found a deep personal connection with the language and the culture, and learned a lot about its different variants and the countries where it's spoken. In my opinion, any language that bears such historical importance is bound to be increadibly impactful to anyone who chooses to learn it.
''')
elif lang_sel == "Portuguese":
  st.markdown(''':red[Level:] Advanced  
  I began studying Portuguese in the summer of 2014. I was interested in the similarities between Spanish and Portuguese, so I decided to dive into the language by studying it independently. I was my first experience with self-teaching, and it opened my eyes to the endless possibilities of well structured, autodidactic learning. As I already had a solid foundation in Spanish, I was able to comfortably navigate the vast amount of online content to select the best resources to progress.
''')
elif lang_sel == "Spanish":
  st.markdown(''':red[Level:] Proficient  
  I grew up with with Arabic as my mother tongue, and with French and English as staple languages in my academic career. I started learning Spanish as a foreign language at school, but I was so encouraged by seeing my progress that I made conscious efforts to maintain it. I remember one of the most impactful Spanish teachers I had. She was from Costa Rica, and it was in her class that I truly noticed a leap in my Spanish abilities. Her class was an environment where I was completely immersed in the language, and I found myself forming friendships with my Latin American neighbors and hearing stories of their life and culture. It was through Spanish that I first experienced the magic of connecting to others through their language.
''')
elif lang_sel == "Turkish":
  st.markdown(''':red[Level:] Beginner  
  Turkish is my most recent language project. It's a language I consider myself familiar with due to knowing Arabic and Persian, and growing up with Turkish friends during childhood. Turkish culture makes me feel at home, and the Turkish language is the perfect addition to my language learning journey, expecially because it feels like a natural progression after learning Persian.
''')

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
  [23.61515, 58.5912467, 50, "#3265ff"],# Muscat
  [26.2235041, 50.5822436, 50, "#3265ff"],# Manama
  [24.4686175, 39.6110134, 50, "#3265ff"],# Al-Madinah
  [21.420847, 39.826869, 50, "#3265ff"],# Makkah
  [6.3700386, 99.7928634, 50, "#3265ff"],# Langkawi
  [1.357107, 103.8194992, 50, "#3265ff"],# Singapore
  [29.7589382, -95.3676974, 50, "#3265ff"],# Houston
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
      [32.6475314, 54.5643516, 50, "#d132ff"],# Iran
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
