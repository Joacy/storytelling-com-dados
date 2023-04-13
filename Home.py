import streamlit as st

st.set_page_config(
    page_title="Storytelling com dados",
    page_icon="📈",
    layout="wide"
)

col1, col2 = st.columns([2, 10], gap="medium")

col1.image("./assets/images/capa.jpg", caption=None, use_column_width=True)
col2.markdown(
    "# Storytelling com dados: Um guia sobre visualização de dados para profissionais de negócios")
