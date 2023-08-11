import streamlit as st
import streamlit_authenticator as stauth
import yaml 
from yaml.loader import SafeLoader

st.set_page_config(
     page_title="FattoVote - Configurações",
     page_icon="https://i.ibb.co/x1Y9wJh/Monograma-Verde.png",
     layout="wide",
     initial_sidebar_state="expanded",
)

# -- AUTHENTICATOR --

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Página de Login

name, authentication_status, username = authenticator.login('Login', 'main')

# Condicional para acesso

if authentication_status: # ==True ou is True

    st.header("⚙️ Configurações")
    try:
        if authenticator.reset_password(username, 'Alterar senha'):
            st.success('Senha alterada com sucesso')
    except Exception as e:
        st.error(e)
    st.sidebar.write(f'Bem-vindo *{name}*')
    authenticator.logout('Logout', 'sidebar')

    imagem = "marca_fatto.png"
    st.sidebar.image(imagem, use_column_width=False, width=300)

    qrcode = "qrcode.png"
    st.sidebar.image(qrcode, use_column_width=False, width=300)
elif authentication_status is False:
    st.error('Username/senha está incorreta')
elif authentication_status is None:
    st.warning('Por favor insira seu nome de usuário e senha')

# Saving config file
with open('config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)
