import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
     page_title="FattoVote",
     page_icon="https://i.ibb.co/x1Y9wJh/Monograma-Verde.png",
     layout="wide",
     initial_sidebar_state="expanded",
)

df = pd.read_excel('votacoes_senado.xlsx', header=[0])
senadores = sorted(df['Parlamentar'].unique())
partidos_unicos = sorted(df['Partido'].unique())

imagem = "marca_fatto.png"
st.sidebar.image(imagem, use_column_width=False, width=300)

qrcode = "qrcode.png"
st.sidebar.image(qrcode, use_column_width=False, width=300)

st.markdown(
"<h2 style='text-align: center; background-color: #307c5c; color: white; padding: 16px;'>Votações Nominais no Senado Federal - 2023</h2>",
unsafe_allow_html=True
)

projetos = df.columns.get_level_values(0)[3:].unique()
df_projetos = pd.DataFrame(projetos, columns=['projeto'])

projetos_principais = [
    ('Arcabouço Fiscal', 'PLP 93-2023'),
    ('MP dos Ministérios', 'MPV 1154-2023'),
    ('Lei Geral do Esporte', 'PL 1825-2022')
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

parlamentares_selecionados = df.loc[df[('Partido')].isin(partidos_selecionados), ('Parlamentar')].unique()
selecionar_parlamentar = st.selectbox('Selecione um parlamentar', ['Todos'] + sorted(parlamentares_selecionados))
parlamentar_selecionado = [selecionar_parlamentar]

if selecionar_parlamentar == 'Todos':
    parlamentar_selecionado = senadores
else:
    parlamentar_selecionado = [selecionar_parlamentar]

for tupla in projetos_principais:
    if tupla[0] == projeto_selecionado2:
        projeto_selecionado = tupla[1]
        break

df2 = df[['Partido', 'Parlamentar', 'UF', projeto_selecionado]]

df_filtrado = df2[
    (df2[('Partido')].isin(partidos_selecionados)) &
    (df2[('Parlamentar')].isin(parlamentar_selecionado))
]

if not parlamentar_selecionado:
    st.markdown("Nenhum parlamentar encontrado.")

df_filtrado.columns = ["Partido", "Parlamentar", "UF", "Voto"]

st.markdown(projeto_selecionado)
st.dataframe(df_filtrado,
                hide_index=True,
    width=800
)

grouped_data = df_filtrado.groupby(["Partido", "Voto"]).size().unstack(fill_value=0)

party_sums = grouped_data.sum(axis=1)
sorted_parties = party_sums.sort_values(ascending=False).index

sorted_data = grouped_data.loc[sorted_parties]

percentages = sorted_data.apply(lambda row: (row / row.sum())*100, axis=1).round(2)

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