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
    df[['ano', 'valor']] = pd.melt(df, value_vars=[2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])

    fig_line = px.line(
         df[df['Gás'] == 'CO2e (t) GWP-AR5'],
         x='ano',
         y='valor',
         color='Meio de Transporte'

    )

    # st.plotly_chart(graf1, use_container_width=True)
    # st.plotly_chart(graf2, use_container_width=True)
    # st.plotly_chart(graf3, use_container_width=True)
    # st.plotly_chart(graf4, use_container_width=True)
    st.plotly_chart(fig_line, use_container_width=True)

def side_bar():
    if selecionado == 'Gráficos':
        graficos()

side_bar()

