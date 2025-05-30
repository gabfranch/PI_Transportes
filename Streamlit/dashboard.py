# python -m streamlit run dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu


st.set_page_config(page_title='Dashboard do Limpa Brasil!', page_icon='🚚', layout='wide')

df = pd.read_excel('base_transportes.xlsx')


# Menu

with st.sidebar:
        selecionado = option_menu(
            menu_title='Menu',
            options=['Gráficos'],
            default_index=0
        )


# Metricas

def graficos():

    st.title('🚢 Análise Comparativa das Emissões de GEE nos Transporte de Carga Rodoviário, Ferroviário e Aquaviário no Brasil')

    # metrica1, metrica2, metrica3 = st.columns(3)

    # with metrica1:
    #     st.metric('titulo', value=valor)
    # with metrica2:
    #     st.metric('titulo', value=valor)
    # with metrica3:
    #     st.metric('titulo', value=valor)


    # graf1


    #graf2


    #graf3


    #graf4


    #graf5


    # st.plotly_chart(graf1, use_container_width=True)
    # st.plotly_chart(graf2, use_container_width=True)
    # st.plotly_chart(graf3, use_container_width=True)
    # st.plotly_chart(graf4, use_container_width=True)
    # st.plotly_chart(graf5, use_container_width=True)

def side_bar():
    if selecionado == 'Gráficos':
        graficos()

side_bar()

