import streamlit as st

st.set_page_config(
     page_title="FattoVote - Contato",
     page_icon="📞",
     layout="wide",
     initial_sidebar_state="expanded",
)

imagem = "marca_fatto.png"
st.sidebar.image(imagem, use_column_width=False, width=300)

qrcode = "qrcode.png"
st.sidebar.image(qrcode, use_column_width=False, width=300)

st.header("📞 Contato")

st.markdown("#### Arthur Santos Lira, analista político")

st.markdown("[![WhatsApp](https://img.shields.io/badge/WhatsApp-green)](https://contate.me/arthurrslira)")
st.markdown("[![Linkedin](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/in/arthur-santos-lira-084292145/)")
st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-gray)](https://github.com/arthurrslira/)")

st.markdown("#### Bernardo Livramento, analista político")

st.markdown("[![WhatsApp](https://img.shields.io/badge/WhatsApp-green)](https://contate.me/bernardolivramento)")

st.markdown("#### Bruno Rizzi, sales e relacionamento com o cliente")

st.markdown("[![WhatsApp](https://img.shields.io/badge/WhatsApp-green)](https://contate.me/brunorizzi)")
st.markdown("[![Linkedin](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/in/brunocenturion/?originalSubdomain=br)")