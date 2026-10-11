import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
from streamlit_marquee import streamlit_marquee
from st_pages import Page, Section, add_page_title, show_pages
import warnings

warnings.filterwarnings('ignore')


# Streamlit webpage properties & layout
st.set_page_config(page_title="Habiba El Keraby", page_icon="🧕🏽", layout="wide")

rain(
    emoji="👋🏼",
    font_size=24,
    falling_speed=7,
    animation_length=2
)

streamlit_marquee(**{
    # the marquee container background color
    'background': "#FF5733",
    # the marquee text size
    'fontSize': '24px',
    # the marquee text color
    "color": "#ffffff",
    # the marquee text content
    'content': 'WELCOME TO MY DIGITAL CORNER OF THE WORLD!',
    # the marquee container width
    'width': '2400px',
    # the marquee container line height
    'lineHeight': "35px",
    # the marquee duration
    'animationDuration': '10s',
})

colored_header(
    label="A Learner, Educator & Researcher",
    description="A snapshot of my work, interests and lifelong learning journey",
    color_name="red-70",
)

st.markdown('''
Welcome to my digital corner of the world.

I'm Habiba, an educator and researcher working at the intersection of AI, data science, programming and language education.

My background spans engineering, machine learning research, technical teaching and multilingual education. I enjoy turning complex subjects into structured learning experiences and creating resources that help people understand, practise and eventually learn independently.

Alongside my professional work, I'm a language learner and creative enthusiast. This website brings together the different parts of that journey.
''')

#st.divider()

show_pages(
    [
        Page("streamlit_app.py", "Home", "🏠"),
        Page("professional.py", "Professional", "💻"),
        Page("academic.py", "Academic", "📖"),
        Page("personal.py", "Personal", "🧕🏼"),
    ]
)
