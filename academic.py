import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.colored_header import colored_header
# from streamlit_dynamic_filters import DynamicFilters

# ============================================================
# PAGE HEADER
# ============================================================

colored_header(
    label="My Academic Journey",
    description="Education, research, and continuous learning",
    color_name="red-70"
)


# ============================================================
# FORMAL EDUCATION
# ============================================================

st.markdown("### Formal Education")

# ----------------------------
# MSc
# ----------------------------

st.markdown("#### MSc, Data Science and Machine Learning")

st.markdown(
    """
**Sultan Qaboos University, Muscat, Oman**  
*2024–2026*
"""
)

st.write(
    "Merit-based tuition fee waiver scholarship."
)

st.markdown("**Thesis:**")

st.write(
    "Controlled Evaluation of Structural Inductive Bias in Autoencoder-Based "
    "Representation Learning for Multi-Omics Breast Cancer Data."
)


st.divider()


# ----------------------------
# BSc
# ----------------------------

st.markdown("#### BSc (Hons), Electrical and Computer Systems Engineering")

st.markdown(
    """
**Monash University**  
*2017–2021*
"""
)

st.write(
    "High Achiever Scholarship."
)

st.markdown("**Final Year Project:**")

st.write(
    "COVID-19 Detection in Chest X-Ray Images Using Deep Learning; "
    "1st Runner-Up, department-wide Final Year Project Presentation Competition."
)


st.divider()


# ============================================================
# RESEARCH JOURNEY
# ============================================================

st.markdown("### Research Journey")

st.write(
    "My academic research has developed across machine learning, biomedical "
    "data, natural language processing, and interdisciplinary computational research."
)


research_col1, research_col2 = st.columns(2)

with research_col1:

    st.markdown("#### Biomedical Machine Learning")

    st.write(
        "My MSc research focused on controlled deep learning experiments for "
        "understanding how structural inductive bias affects learned representations "
        "of high-dimensional breast cancer multi-omics data."
    )

    st.write(
        "This work involved autoencoders, denoising autoencoders, graph-regularized "
        "and graph-structured approaches, with evaluation based on representation "
        "quality, stability, geometry, and clinical coherence."
    )


with research_col2:

    st.markdown("#### Medical AI & NLP")

    st.write(
        "As a Research Assistant at Sultan Qaboos University, I worked on "
        "automated cancer-registry information extraction from pathology and "
        "medical reports using open-source large language models."
    )

    st.write(
        "The work involved multi-agent workflows, document processing, "
        "information extraction, evaluation, error analysis, and interdisciplinary "
        "collaboration with clinical researchers."
    )


st.markdown("#### Current Research Direction")

st.write(
    "My broader research interests include machine learning, representation "
    "learning, natural language processing, large language models, and the "
    "application of computational methods to complex biomedical data."
)


st.divider()


# ============================================================
# SELECTED ACADEMIC WORK
# ============================================================

st.markdown("### Selected Academic Work")

st.markdown(
    """
**MSc Thesis**  
Controlled Evaluation of Structural Inductive Bias in Autoencoder-Based
Representation Learning for Multi-Omics Breast Cancer Data.
"""
)

st.markdown(
    """
**AACR 2025**  
Transcriptomic Predictors of Therapy Response Across Age Groups in an Omani
Breast Cancer Cohort — abstract accepted; co-first author.
"""
)

st.markdown(
    """
**BioNLP 2026**  
A Multi-Agent Open-Source LLM for Cancer Registry Information Extraction from
Pathology & Medical Reports — accepted; co-author and technical contributor.
"""
)

st.markdown(
    """
**IWBBIO 2026**  
Comparative Evaluation of Dimensionality Reduction Strategies for
Clustering-Based Patient Stratification in Breast Cancer Transcriptomics —
accepted and presented; co-author and conference presenter.
"""
)

st.markdown(
    """
**JMIR Medical Informatics**  
Automated Extraction of Multi-Field and Multi-Site Cancer Registry Information
Using Open-Source Large Language Models — manuscript under revision.
"""
)

st.markdown(
    """
**MSc Thesis-Based Manuscript**  
Disentangling Architectural and Graph Effects in Multi-Omics Autoencoders:
A Controlled Ablation and Null-Graph Study in Breast Cancer — submitted to
Springer Nature's NetMAHIB.
"""
)


st.divider()


# ============================================================
# ACADEMIC SKILLS
# ============================================================

st.markdown("### Academic Practice")

academic_col1, academic_col2 = st.columns(2)

with academic_col1:

    st.markdown("#### Research Methods")

    st.write(
        "Experimental design · Applied statistical analysis · "
        "Machine learning evaluation · Literature review · "
        "Data analysis · Scientific experimentation"
    )


with academic_col2:

    st.markdown("#### Research Communication")

    st.write(
        "Academic writing · Scientific presentations · "
        "Interdisciplinary collaboration · Technical communication · "
        "LaTeX / Overleaf"
    )


st.divider()


# ============================================================
# CONTINUOUS LEARNING
# ============================================================

st.markdown("### Continuous Learning")

st.write(
    "Formal education is only one part of my learning journey. I also regularly "
    "learn independently through technical courses, research literature, "
    "programming projects, and language study."
)

st.write(
    "My personal learning interests extend beyond my formal academic fields, "
    "reflecting a broader commitment to continuous and self-directed learning."
)
