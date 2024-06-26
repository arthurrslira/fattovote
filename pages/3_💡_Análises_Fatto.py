import streamlit as st
import streamlit_authenticator as stauth
import yaml 
from yaml.loader import SafeLoader

st.set_page_config(
     page_title="FattoVote - Análises Fatto",
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

#name, authentication_status, username = authenticator.login('Login', 'main')

#if authentication_status:
    
#st.sidebar.write(f'Bem-vindo *{name}*')
#authenticator.logout('Logout', 'sidebar')

imagem = "marca_fatto.png"
st.sidebar.image(imagem, use_column_width=False, width=300)

qrcode = "qrcode.png"
st.sidebar.image(qrcode, use_column_width=False, width=300)



st.header("💡 Análises Fatto")
    
texto = """
    <p style="text-align: justify;">
    Através do dashboard e dos gráficos que podem ser gerados a partir dos filtros, podemos perceber uma distribuição partidária bem interessante:\n
    1) A pauta econômica (reforma tributária, arcabouço fiscal) recebeu apoio dos partidos de centro e centro-direita, como PP, PSD, Republicanos e União Brasil; \n
    2) No entanto, o marco temporal das terras indígenas dividiu a Câmara entre direita e esquerda e mesmo partidos com ministérios no governo Lula votaram a favor do projeto, o qual o governo se posicionou contra;\n
    3) Entre os partidos com ministérios no governo, o PSOL, partido mais à esquerda com representação parlamentar, foi o que proporcionalmente menos apoiou a reforma tributária.\n

    P.S.: Neste momento, é equivocado atribuir a partidos como PP e Republicanos a etiqueta de 'governo' por conta do percentual de suas votações favoráveis aos projetos do Executivo — ainda mais se tratando apenas de votações em Plenário. Esses partidos ganharam  um espaço no governo, mas ainda se comportam como partidos independentes. A métrica de votos é importante, mas não suficiente para analisar todo o processo.
    </p>
    """
    
st.markdown(texto, unsafe_allow_html=True)
#elif authentication_status is False:
#    st.error('Username/senha está incorreta')
#elif authentication_status is None:
#    st.warning('Por favor insira seu nome de usuário e senha')

#    try:
#        if authenticator.register_user('Primeiro Login', preauthorization=True):
#            st.success('User registered successfully')
#    except Exception as e:
#        st.error(e)

# Saving config file
#with open('config.yaml', 'w') as file:
#    yaml.dump(config, file, default_flow_style=False)