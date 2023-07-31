import streamlit as st

st.set_page_config(
     page_title="FattoVote - Sobre",
     page_icon="📝",
     layout="wide",
     initial_sidebar_state="expanded",
)

imagem = "marca_fatto.png"
st.sidebar.image(imagem, use_column_width=False, width=100)

st.header("📝 Sobre")

texto = """
    <p style="text-align: justify;">
    
    </p>
    """
    
st.markdown(texto, unsafe_allow_html=True)


