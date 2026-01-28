import streamlit as st
from pathlib import Path

# Configuration de la page
st.set_page_config(
    page_title="K-Store KR — Landing page",
    layout="wide"
)

# Lire les fichiers HTML et CSS
html_path = Path("index.html")
css_path = Path("style.css")

html = html_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# Afficher la landing page avec le CSS injecté
st.components.v1.html(
    f"""
    <style>
    {css}
    </style>
    {html}
    """,
    height=1600,
    scrolling=True
)
