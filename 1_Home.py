import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime


if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall",ascending=False)
    st.session_state["data"] = df_data

st.markdown('# FIFA23 OFFICIAL DATASET!')
st.sidebar.markdown("Desevolvindo por JhonnataB.")
btn2 = st.sidebar.button("Acesse o Linkedin")
if btn2:
    webbrowser.open_new_tab("https://www.linkedin.com/in/jhonatan-bernardino-94a5712b2/")

btn = st.button("Acessa os dados no Keggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown (" O conjunto de dados de jogadores de futebol de 2017 a 2023 fornece informações abrangentes sobre jogadores profissionais de futebol. O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos, características físicas, estatísticas de jogo, detalhes de contrato e afiliações a clubes. Com mais de **17.000 registros**, este conjunto de dados oferece um recurso valioso para analistas, pesquisadores e entusiastas do futebol interessados ​​em explorar vários aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e desenvolvimento de jogadores ao longo do tempo.")

