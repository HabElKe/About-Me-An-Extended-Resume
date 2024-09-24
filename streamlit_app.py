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
    label="About Me: Learner, Educator, Polyglot",
    description="A snapshot of me, a curious and eternal learner",
    color_name="red-70",
)

st.markdown('''
Welcome to my digital corner of the world! 👋🏼 I'm **Habiba** 🧕🏼, an *Electrical & Computer Systems Engineering* graduate with a passion for exploring the intricate workings of both technology 👩🏽‍💻 and the creative arts 🎨. 

I take pride in being a versatile and autonomous learner, always eager to dive into new challenges. This curiosity has led me to explore a diverse range of interests, including language learning, crochet 🧶, embroidery 🧵, drawing 👩🏽‍🎨, poetry 📜, writing ✍🏼, photography 📸, and more!

In the world of **Data Science** 💻, I have honed my skills and independence as a **Junior Data Scientist**, where I maintain databases, craft insightful visualizations, and work with ML & NLP models. 

My journey has enabled me to experience both the fast-paced nature of the tech world 👩🏽‍💻 as well as the more serene environment of the classroom 👩🏽‍🏫, where I had the privilege of teaching Arabic to students of all ages for 3 years, as well as doing some private tutoring in English and French.

With a strong foundation in engineering and a heart deeply invested in the world of languages and arts, I embrace the interplay between logic and creativity. I invite you to join me on this exciting journey as I continue to grow 📈, learn 📚, and create ✨. 

Thank you for visiting 🙏🏽, and I hope you find inspiration in the intersection of my diverse passions and professional pursuits!
''')

show_pages(
    [
        Page("streamlit_app.py", "Home", "🏠"),
        Page("professional.py", "Professional", "💻"),
        Page("academic.py", "Academic", "📖"),
        Page("personal.py", "Personal", "🧕🏼"),
    ]
)
