import streamlit as st
import pandas as pd
import altair as alt
import streamlit_authenticator as stauth
import streamlit.components.v1 as components
import yaml 
from yaml.loader import SafeLoader

# Função para carregar os dados com cache
@st.cache_data
def load_data(file):
    return pd.read_excel(file)

# Função para obter a URL da imagem com cache
@st.cache_data
def obter_url_imagem(nome_parlamentar, df_img):
    deputado_filtrado = df_img[df_img['Nome do Deputado'] == nome_parlamentar]
    if not deputado_filtrado.empty:
        return deputado_filtrado['Link da Imagem'].iloc[0]
    else:
        return 'https://www.camara.leg.br/tema/assets/images/foto-deputado-sem-foto-peq.png'

# Carregar dados
df_img = load_data('deputados_imagens.xlsx')
df = load_data('camara_deputados_votacoe.xlsx')

st.set_page_config(
     page_title="FattoVote",
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

parlamentares = sorted(df['Votação', 'Parlamentar'].unique())
partidos_unicos = sorted(df['Unnamed: 0_level_0', 'Partido'].unique())

# Carregar imagens e QR code
imagem = "marca_fatto.png"
st.sidebar.image(imagem, use_column_width=False, width=300)
qrcode = "qrcode.png"
st.sidebar.image(qrcode, use_column_width=False, width=300)

st.markdown(
    "<h2 style='text-align: center; background-color: #307c5c; color: white; padding: 16px;'>Votações Nominais na Câmara dos Deputados - 2023</h2>",
    unsafe_allow_html=True
)

projetos = df.columns.get_level_values(0)[2:].unique()
df_projetos = pd.DataFrame(projetos, columns=['projeto'])
df_projetos['projeto_data'] = df_projetos['projeto'].apply(lambda x: x.split("-", 1)[0].strip())
df_projetos['projeto_nome'] = df_projetos['projeto'].apply(lambda x: x.split("-", 1)[1].strip())

projetos_principais = [
    ('Reforma Tributária - 1º Turno', '06/07/2023 21:00:48 - PEC  Nº 45/2019 - SUBSTITUTIVO OFERECIDO PELA COMISSÃO ESPECIAL'),
    ('Reforma Tributária - 2º Turno', '07/07/2023 01:17:05 - PEC  Nº 45/2019 - PROPOSTA DE EMENDA À CONSTITUIÇÃO - 2º TURNO'),
    ('Arcabouço Fiscal', '23/05/2023 23:12:45 - PLP  Nº 93/2023 - SUBSTITUTIVO OFERECIDO PELO RELATOR'),
    ('Arcabouço Fiscal (Emendas vindas do Senado)', '22/08/2023 19:47:31 - PLP  Nº 93/2023 - EMENDAS COM PARECER PELA APROVAÇÃO'),
    ('Marco Temporal das Terras Indígenas', '30/05/2023 20:02:55 - PL   Nº 490/2007 - SUBEMENDA SUBSTITUTIVA'),
    ('MP dos Ministérios', '31/05/2023 22:43:56 - MPV  Nº 1154/2023 - PARECER DA C.M P/ ATEND. DOS PRESSUPOSTOS CONSTITUCIONAIS...'),
    ('Suspensão dos decretos de saneamento emitidos por Lula', '03/05/2023 20:37:16 - PDL  Nº 98/2023 - SUBSTITUTIVO OFERECIDO PELO RELATOR'),
    ('Fundos offshore e exclusivos', '25/10/2023 20:33:29 - PL   Nº 4173/2023 - SUBEMENDA SUBSTITUTIVA'),
    ('Combustível do Futuro', '13/03/2024 19:29:53 - PL   Nº 528/2020 - SUBEMENDA SUBSTITUTIVA')
    ('Suspensão da Dívida do RS', '14/05/2024 23:00:20 - PLP  Nº 85/2024 - SUBSTITUTIVO OFERECIDO'),
    ('Veto Saidinha (SIM mantém o veto)', '28/05/2024 18:50:10 - VETO Nº 8/2024 - DISPOSITIVOS 1 E 2 (SAÍDA TEMPORÁRIA)')
]

primeiros_valores = [tupla[0] for tupla in projetos_principais]

st.subheader('Projeto:')
projeto_selecionado2 = st.selectbox('Selecione o projeto', primeiros_valores)

st.subheader('Partidos:')
if st.checkbox("Todos", value=True):
    partidos_selecionados = partidos_unicos
else:
    partidos_selecionados = st.multiselect('Selecione os partidos', partidos_unicos, default=partidos_unicos)

st.subheader('Parlamentares:')
parlamentares_selecionados = df.loc[df[('Unnamed: 0_level_0', 'Partido')].isin(partidos_selecionados), ('Votação', 'Parlamentar')].unique()
selecionar_parlamentar = st.selectbox('Selecione um parlamentar', ['Todos'] + sorted(parlamentares_selecionados))

if selecionar_parlamentar == 'Todos':
    parlamentar_selecionado = parlamentares
else:
    parlamentar_selecionado = [selecionar_parlamentar]

for tupla in projetos_principais:
    if tupla[0] == projeto_selecionado2:
        projeto_selecionado = tupla[1]
        break

df2 = df[['Unnamed: 0_level_0', 'Votação', projeto_selecionado]]
df_filtrado = df2[
    (df2[('Unnamed: 0_level_0', 'Partido')].isin(partidos_selecionados)) &
    (df2[('Votação', 'Parlamentar')].isin(parlamentar_selecionado))
]

if df_filtrado.empty:
    st.markdown("Nenhum parlamentar encontrado.")

df_filtrado.columns = ["Partido", "Parlamentar", "Voto", "Orientação"]
df_filtrado = df_filtrado[df_filtrado['Voto'] != '-']

# Aplicar a função de URL da imagem
df_filtrado["Imagem"] = df_filtrado["Parlamentar"].apply(lambda x: obter_url_imagem(x, df_img))
df_filtrado = df_filtrado[["Imagem", "Parlamentar", "Partido", "Voto", "Orientação"]]

st.markdown(projeto_selecionado)
st.dataframe(
    df_filtrado,
    column_config={
        "Imagem": st.column_config.ImageColumn(label="", width=20)
    },
    hide_index=True,
    width=800
)

grouped_data = df_filtrado.groupby(["Partido", "Voto"]).size().unstack(fill_value=0)
party_sums = grouped_data.sum(axis=1)
sorted_parties = party_sums.sort_values(ascending=False).index
sorted_data = grouped_data.loc[sorted_parties]

percentages = sorted_data.apply(lambda row: (row / row.sum()) * 100, axis=1).round(2)
df_long = percentages.reset_index().melt(id_vars='Partido', var_name='Voto', value_name='Percentual')

colors = alt.Scale(domain=['Sim', 'Não', 'Não votou', 'Abstenção'],
                   range=['#90EE90', '#FFA07A', '#D3D3D3', '#D2B48C'])

chart = alt.Chart(df_long).mark_bar().encode(
    x='Partido',
    y='Percentual',
    color=alt.Color('Voto', scale=colors),
    tooltip=['Partido', 'Voto', 'Percentual']
).properties(
    width=600,
    height=400
)

st.altair_chart(chart, use_container_width=True)

#elif authentication_status is False:
#    st.error('Username/password is incorrect')
#elif authentication_status is None:
#    st.warning('Please enter your username and password')

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)