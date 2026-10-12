import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.colored_header import colored_header

# ============================================================
# LINKS
# Replace the placeholder URLs below with your actual links.
# ============================================================

TECHNICAL_TEACHING_PORTFOLIO = "https://digitallanguagelearner.my.canva.site/technical-teaching-portfolio"
LANGUAGE_TEACHING_PORTFOLIO = "https://digitallanguagelearner.my.canva.site/language-teaching-portfolio"
PYGAME_COURSE = "https://github.com/HabElKe/Pygame-Python-Beginners-Course"
LANGUAGE_MATERIALS = "https://payhip.com/SelfLearnerToolkit"

DATA_SCIENCE_PORTFOLIO = "https://www.datascienceportfol.io/Habiba_ElKeraby"
LINKEDIN = "https://www.linkedin.com/in/habiba-e-7839b3194/"


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

colored_header(
    label="My Professional Journey",
    description="Education, AI & Data Science, research, and the work that connects them",
    color_name="red-70"
)


# ---------------------------------------------------------
# About Me
# ---------------------------------------------------------

st.markdown("### About Me")

st.markdown(
    """
I am an **AI and Data Science educator and applied machine learning researcher**
with a background in electrical and computer systems engineering, data science,
and interdisciplinary research.

My professional work combines **AI and data science with education**. I have
taught Python programming, machine learning, deep learning, web programming,
and languages to learners with different backgrounds and levels of experience.

My research interests include machine learning, representation learning,
natural language processing, large language models, and the application of
computational methods to biomedical data.

Across both teaching and research, I enjoy making complex ideas understandable,
structuring learning around practical problems, and developing resources that
help learners become more confident and independent.
"""
)


# ---------------------------------------------------------
# Areas of Work
# ---------------------------------------------------------

st.markdown("### Areas of Work")

area_col1, area_col2 = st.columns(2)

with area_col1:
    st.markdown("#### AI & Machine Learning")
    st.write(
        "Applied machine learning, deep learning, NLP, LLMs, "
        "and representation learning."
    )

    st.markdown("#### Data Science")
    st.write(
        "Data analysis, visualization, statistical exploration, "
        "and computational approaches to interdisciplinary datasets."
    )

with area_col2:
    st.markdown("#### Education")
    st.write(
        "Programming, AI, data science, and multilingual language "
        "education through structured and practical instruction."
    )

    st.markdown("#### Research")
    st.write(
        "Interdisciplinary machine learning research, particularly "
        "at the intersection of AI and biomedical data."
    )


st.divider()


# =========================================================
# MAIN PROFESSIONAL TABS
# =========================================================

teaching_tab, research_tab = st.tabs(
    [
        "Teaching",
        "Research & Professional Experience",
    ]
)


# =========================================================
# TEACHING TAB
# =========================================================

with teaching_tab:

    st.markdown("### Teaching")

    st.write(
        "Teaching is a central part of my professional work. My experience "
        "spans technical subjects and language education, from individual "
        "instruction to structured multi-session courses."
    )

    # -----------------------------------------------------
    # Technical Teaching
    # -----------------------------------------------------

    st.markdown("#### Technical Teaching")

    st.markdown("**AI · Data Science · Programming**")

    st.write(
        "I teach programming and computational subjects through structured "
        "progression, practical application, and learner-centred instruction."
    )

    st.link_button(
        "View Technical Teaching Portfolio",
        TECHNICAL_TEACHING_PORTFOLIO
    )

    st.markdown("##### Pygame Project-Based Course")

    st.write(
        "A complete project-based Python/Pygame course, with lessons provided "
        "as commented Python files designed for use in the Trinket Pygame environment."
    )

    st.link_button(
        "Explore the Pygame Course on GitHub",
        PYGAME_COURSE
    )

    st.divider()

    # -----------------------------------------------------
    # Language Teaching
    # -----------------------------------------------------

    st.markdown("#### Language Teaching")

    st.markdown("**English · Arabic · French**")

    st.write(
        "My language-teaching experience includes classroom teaching, "
        "individual tutoring, exam preparation, and the design of "
        "personalized learning programmes and materials."
    )

    st.link_button(
        "View Language Teaching Portfolio",
        LANGUAGE_TEACHING_PORTFOLIO
    )

    st.markdown("##### Language Learning Materials")

    st.write(
        "Selected language-learning resources and materials available "
        "through my Payhip store."
    )

    st.link_button(
        "Visit My Language-Learning Materials",
        LANGUAGE_MATERIALS
    )

    st.divider()

    # -----------------------------------------------------
    # Teaching Areas
    # -----------------------------------------------------

    st.markdown("#### Teaching Areas")

    teaching_col1, teaching_col2 = st.columns(2)

    with teaching_col1:
        st.markdown("**Programming**")
        st.write("Python · Web Programming")

        st.markdown("**AI & Data**")
        st.write(
            "Machine Learning · Deep Learning · Data Science · Data Visualization"
        )

    with teaching_col2:
        st.markdown("**Languages**")
        st.write("Arabic · English · French")

        st.markdown("**Research & Academic**")
        st.write(
            "Academic writing · Literature review · Experimental design · "
            "Applied statistical analysis · Scientific presentations · "
            "LaTeX / Overleaf"
        )


# =========================================================
# RESEARCH + PROFESSIONAL EXPERIENCE TAB
# =========================================================

with research_tab:

    # -----------------------------------------------------
    # Research & Publications
    # -----------------------------------------------------

    st.markdown("### Research & Publications")

    st.write(
        "My research focuses on applying machine learning and computational "
        "methods to complex datasets, with particular experience in biomedical "
        "data and natural language processing."
    )

    research_col1, research_col2, research_col3 = st.columns(3)

    with research_col1:
        st.markdown("#### Biomedical Machine Learning")
        st.write(
            "Representation learning, transcriptomic data, multi-omics data, "
            "and computational approaches to cancer research."
        )

    with research_col2:
        st.markdown("#### NLP & Large Language Models")
        st.write(
            "Information extraction from medical text using open-source LLMs "
            "and multi-agent approaches."
        )

    with research_col3:
        st.markdown("#### Research Communication")
        st.write(
            "Scientific writing, conference presentations, interdisciplinary "
            "collaboration, and technical communication."
        )

    st.markdown("#### Selected Publications & Presentations")

    publications = [
        (
            "Transcriptomic Predictors of Therapy Response Across Age Groups "
            "in an Omani Breast Cancer Cohort",
            "AACR 2025 abstract accepted. Co-first author; responsible for "
            "the data analysis and machine learning work."
        ),
        (
            "A Multi-Agent Open-Source LLM for Cancer Registry Information "
            "Extraction from Pathology & Medical Reports",
            "BioNLP 2026, accepted. Co-author and technical contributor."
        ),
        (
            "Comparative Evaluation of Dimensionality Reduction Strategies "
            "for Clustering-Based Patient Stratification in Breast Cancer "
            "Transcriptomics",
            "IWBBIO 2026, accepted and presented. Co-author and conference presenter."
        ),
        (
            "Automated Extraction of Multi-Field and Multi-Site Cancer "
            "Registry Information Using Open-Source Large Language Models",
            "Manuscript under revision for submission to JMIR Medical Informatics. "
            "Second author and technical contributor."
        ),
        (
            "Disentangling Architectural and Graph Effects in Multi-Omics "
            "Autoencoders: A Controlled Ablation and Null-Graph Study in "
            "Breast Cancer",
            "MSc thesis-based manuscript submitted to Springer Nature's NetMAHIB."
        ),
    ]

    for title, description in publications:
        st.markdown(f"**{title}**")
        st.write(description)

    st.divider()

    # -----------------------------------------------------
    # Professional Experience
    # -----------------------------------------------------

    st.markdown("### Professional Experience")

    st.markdown("#### Teaching & Education")

    st.markdown(
        """**Teaching Assistant — Sultan Qaboos University**  
*Feb 2025–May 2026*

Supported undergraduate teaching across Deep Learning Fundamentals,
Machine Learning, and Introduction to Python Programming, with approximately
30–35 students per course.
"""
    )

    st.markdown(
        """**Programming Instructor — Eveil@ng, Online Academy**  
*Jan 2024–Jun 2025; Jan 2025–Jun 2026*

Delivered approximately six-month courses in Web Programming and Python
Programming and prepared practical programming material for learners with
different levels of prior experience.
"""
    )

    st.markdown(
        """**Arabic Teacher — Local Cultural Center, Sartrouville, France**  
*2021–2024*

Taught Arabic to school-age and adult learners across multiple academic years,
adapting explanations and activities to different learner levels.
"""
    )

    st.markdown(
        """**Language Teacher — Academia Europa, Online Academy**  
*Dec 2021–Mar 2022*

Taught English and French online to learners with varied levels and learning goals.
"""
    )

    st.markdown(
        """**Python Tutor — Superprofs.com**  
*Summer 2025*

Provided one-to-one Python programming tutoring tailored to individual learning needs.
"""
    )

    st.markdown("#### Research & Data Science")

    st.markdown(
        """**Research Assistant – Medical AI & NLP — Sultan Qaboos University**  
*Feb–Dec 2025*

Developed automated cancer-registry information extraction workflows from
pathology and medical reports using open-source LLMs, including LLaMA-, Qwen-,
and DeepSeek-based models. Designed multi-agent workflows and worked with
hospital databases covering more than 600 patients.
"""
    )

    st.markdown(
        """**MSc Researcher – Biomedical Machine Learning — Sultan Qaboos University**  
*2024–2026*

Developed controlled deep learning experiments to study structural inductive
bias in unsupervised representations of high-dimensional breast cancer
multi-omics data, evaluating autoencoder, denoising, graph-regularized,
and graph-structured approaches.
"""
    )


# =========================================================
# PROFESSIONAL LINKS
# =========================================================

st.divider()

st.markdown("### Professional Links")

link_col1, link_col2 = st.columns(2)

with link_col1:
    st.link_button(
        "Data Science Portfolio",
        DATA_SCIENCE_PORTFOLIO
    )

with link_col2:
    st.link_button(
        "LinkedIn",
        LINKEDIN
    )
