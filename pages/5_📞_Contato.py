import streamlit as st

st.set_page_config(
     page_title="FattoVote - Contato",
     page_icon="📞",
     layout="wide",
     initial_sidebar_state="expanded",
)

imagem = "marca_fatto.png"
st.sidebar.image(imagem, use_column_width=False, width=300)

st.header("📞 Contato")

st.markdown("#### Arthur Lira")
st.markdown("[![Linkedin](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/in/arthur-santos-lira-084292145/)")
st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-gray)](https://github.com/arthurrslira/)")

