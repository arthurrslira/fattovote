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

texto = """
    <p style="text-align: justify;">
    Analista Político
    +55 81 993587944
    </p>
    """

st.markdown(texto, unsafe_allow_html=True)
st.markdown("[![Linkedin](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/in/arthur-santos-lira-084292145/)")
st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-gray)](https://github.com/arthurrslira/)")

st.markdown("#### Bruno Rizzi")

texto = """
    <p style="text-align: justify;">
    Sales e Relacionamento com o Cliente 
    +55 11 97208 9616
    </p>
    """

st.markdown(texto, unsafe_allow_html=True)