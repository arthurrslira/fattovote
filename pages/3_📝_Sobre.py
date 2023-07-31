import streamlit as st

st.set_page_config(
     page_title="FattoVote - Sobre",
     page_icon="https://i.ibb.co/x1Y9wJh/Monograma-Verde.png",
     layout="wide",
     initial_sidebar_state="expanded",
)

imagem = "marca_fatto.png"
st.sidebar.image(imagem, use_column_width=False, width=300)

qrcode = "qrcode.png"
st.sidebar.image(qrcode, use_column_width=False, width=300)

st.header("📝 Sobre")

texto = """
    <p style="text-align: justify;">Dashboard da <strong>Fatto Inteligência Política</strong> sobre votações nominais na Câmara dos Deputados. Acesso restrito para clientes.
    </p>
    """

st.markdown(texto, unsafe_allow_html=True)

st.header("🎲 Origem dos Dados")

st.subheader("Dataset")

texto2 = """
    <p style="text-align: justify;">
    Os dados foram extraídos através do site da <strong>Câmara dos Deputados</strong>. (<a href="https://www2.camara.leg.br/atividade-legislativa/plenario/relatorios-da-atividade-legislativa/dados-de-votacoes-nominais" target="_blank">link</a>)
    </p>
    """

st.markdown(texto2, unsafe_allow_html=True)

st.subheader("Imagens dos Parlamentares")

texto3 = """
    <p style="text-align: justify;">
    As imagens dos parlamentares foram extraídas diretamente do site da Câmara dos Deputados. (<a href="https://www.camara.leg.br/deputados/quem-sao">link</a>)
    </p>
    """

st.markdown(texto3, unsafe_allow_html=True)


