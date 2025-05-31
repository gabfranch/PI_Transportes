# python -m streamlit run dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu


st.set_page_config(page_title='Emissão por Transporte', page_icon='🏭', layout='wide')

df = pd.read_excel('base_transportes_unificado.xlsx')


# Menu

with st.sidebar:
        selecionado = option_menu(
            menu_title='Menu',
            options=['Gráficos'],
            default_index=0
        )

        #Filtro por Meio de Transporte
        meio_transporte = st.sidebar.multiselect(
        #Opções filtro
            "Meio de Transporte", 
            options = df['Meio de Transporte'].unique(),
        #Opção que vem por padrão no filtro
            default = df['Meio de Transporte'].unique(),
        #Chave única
            key="meio_transporte"
        )

        #Filtro por combustivel
        combustivel = st.sidebar.multiselect(
        #Opções filtro
            "Combustivel", 
            options = df['Combustivel'].unique(),
        #Opção que vem por padrão no filtro
            default = df['Combustivel'].unique(),
        #Chave única
            key="combustivel"
        )

        #Filtro por Tipo de Transporte
        tipo_transporte = st.sidebar.multiselect(
        #Opções filtro
            "Tipo de Transporte", 
            options = df['Tipo de Transporte'].unique(),
        #Opção que vem por padrão no filtro
            default = df['Tipo de Transporte'].unique(),
        #Chave única
            key="tipo_transporte"
        )

        #Filtro por Atividade
        atividade = st.sidebar.multiselect(
        #Opções filtro
            "Atividade", 
            options = df['Atividade'].unique(),
        #Opção que vem por padrão no filtro
            default = df['Atividade'].unique(),
        #Chave única
            key="atividade"
        )

        #Filtro por Estado
        estado = st.sidebar.multiselect(
        #Opções filtro
            "Estado", 
            options = df['Estado'].unique(),
        #Opção que vem por padrão no filtro
            default = df['Estado'].unique(),
        #Chave única
            key="estado"
        )

df_filtrado = df.query('`Meio de Transporte` in @meio_transporte and Combustivel in @combustivel and `Tipo de Transporte` in @tipo_transporte and Atividade in @atividade and Estado in @estado')

# Metricas

def graficos():

    st.title('🚢 Emissões de CO2e por Transporte de Carga Rodoviário, Ferroviário e Hidroviário')

    # metrica1, metrica2, metrica3 = st.columns(3)

    # with metrica1:
    #     st.metric('titulo', value=valor)
    # with metrica2:
    #     st.metric('titulo', value=valor)
    # with metrica3:
    #     st.metric('titulo', value=valor)


    df_co2 = df_filtrado[df_filtrado['Gás'] == 'CO2e (t) GWP-AR6']

    # graf1
    graf_comb = px.bar(
        df_co2.groupby('Combustivel')['Emissão Total'].sum().reset_index(),
        x='Combustivel',
        y='Emissão Total',
        text='Emissão Total',
        text_auto=True,
        title='Emissão Total por Combustível',
        color='Combustivel'
    )

    graf_comb.update_traces(textposition='outside')
    graf_comb.update_layout(height=550, xaxis={'categoryorder': 'total descending'})
    

    #graf2
    df_estados = df_co2[df_co2['Estado'] != 'Não Alocado']


    emissao_estado_5 = px.bar(
        df_estados.groupby('Estado')['Emissão Total'].sum().sort_values(ascending=False).head(5).reset_index(),
        x="Estado",
        y="Emissão Total",
        color="Estado",
        text='Emissão Total',
        title="Top 5 Estados com Mais Emissão"
    )

    emissao_estado_5.update_traces(textposition='outside')
    emissao_estado_5.update_layout(height=550, xaxis={'categoryorder': 'total descending'})

    #graf3


    #graf4


    #graf5
    

    fig_line = px.line(
         df_co2.groupby(['Ano', 'Meio de Transporte'])['Emissão Total'].sum().reset_index(),
         x='Ano',
         y='Emissão Total',
         color='Meio de Transporte',
         title='Emissão Total por Ano',
         labels = {
              'Emissão Total': 'CO2e (t) GWP-AR6'
         }
    )

    st.plotly_chart(graf_comb, use_container_width=True)
    st.plotly_chart(emissao_estado_5, use_container_width=True)
    # st.plotly_chart(graf3, use_container_width=True)
    # st.plotly_chart(graf4, use_container_width=True)
    st.plotly_chart(fig_line, use_container_width=True)

def side_bar():
    if selecionado == 'Gráficos':
        graficos()

side_bar()

