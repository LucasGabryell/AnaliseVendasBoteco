import streamlit as st
import plotly.express as px
import pandas as pd
import calendar

def plot_vendas_mes(dados):
    # Certifique-se de que a coluna 'Data da Venda' seja do tipo datetime
    dados['Data da Venda'] = pd.to_datetime(dados['Data da Venda'], format='%d/%m/%Y')

    # Crie uma nova coluna 'Mês' para extrair o mês da data de venda
    dados['Mês'] = dados['Data da Venda'].dt.month

    # Contagem de vendas por mês
    vendas_por_mes = dados['Mês'].value_counts().reset_index()
    vendas_por_mes.columns = ['Mês', 'Quantidade de Vendas']

    # Mapear números de mês para nomes completos
    vendas_por_mes['Mês'] = vendas_por_mes['Mês'].apply(lambda x: calendar.month_name[int(x)])

    # Identificar o mês com mais vendas
    mes_mais_vendido_idx = vendas_por_mes['Quantidade de Vendas'].idxmax()
    mes_mais_vendido = vendas_por_mes.loc[mes_mais_vendido_idx]

    # Identificar o mês com menos vendas
    mes_menos_vendido_idx = vendas_por_mes['Quantidade de Vendas'].idxmin()
    mes_menos_vendido = vendas_por_mes.loc[mes_menos_vendido_idx]

    # Crie um gráfico de barras interativo usando Plotly Express
    fig = px.bar(vendas_por_mes, x='Mês', y='Quantidade de Vendas', title='Vendas por Mês')
    fig.update_xaxes(title_text='Mês')
    fig.update_yaxes(title_text='Quantidade de Vendas')

    # Mostrar o gráfico
    st.plotly_chart(fig)

    # Exibir os meses com mais e menos vendas
    st.write(
        f"Mês com mais vendas: {mes_mais_vendido['Mês']} com {mes_mais_vendido['Quantidade de Vendas']} vendas")
    st.write(
        f"Mês com menos vendas: {mes_menos_vendido['Mês']} com {mes_menos_vendido['Quantidade de Vendas']} vendas")
    return fig

def plot_vendas_tipo(dados):
    # Certifique-se de que a coluna 'Data da Venda' seja do tipo datetime
    dados['Data da Venda'] = pd.to_datetime(dados['Data da Venda'], format='%d/%m/%Y')

    # Crie uma nova coluna 'Mês' para extrair o mês da data de venda
    dados['Mês'] = dados['Data da Venda'].dt.month

    # Contagem de vendas por mês e tipo de venda
    vendas_por_mes_tipo = dados.groupby(['Mês', 'Tipo de Venda']).size().reset_index(name='Quantidade de Vendas')

    # Mapear números de mês para nomes completos
    vendas_por_mes_tipo['Mês'] = vendas_por_mes_tipo['Mês'].apply(lambda x: calendar.month_name[int(x)])

    # Crie um gráfico de barras interativo usando Plotly Express
    fig = px.bar(vendas_por_mes_tipo, x='Mês', y='Quantidade de Vendas', color='Tipo de Venda',
                 title='Vendas por Mês e Tipo de Venda')
    fig.update_xaxes(title_text='Mês')
    fig.update_yaxes(title_text='Quantidade de Vendas')

    # Mostrar o gráfico
    st.plotly_chart(fig)

    # Identificar o tipo de venda mais usado
    tipo_mais_usado = vendas_por_mes_tipo.groupby('Tipo de Venda')['Quantidade de Vendas'].sum().idxmax()
    quantidade_mais_usado = vendas_por_mes_tipo.groupby('Tipo de Venda')['Quantidade de Vendas'].sum().max()

    # Identificar o tipo de venda menos usado
    tipo_menos_usado = vendas_por_mes_tipo.groupby('Tipo de Venda')['Quantidade de Vendas'].sum().idxmin()
    quantidade_menos_usado = vendas_por_mes_tipo.groupby('Tipo de Venda')['Quantidade de Vendas'].sum().min()

    # Exibir o tipo de venda mais usado e menos usado
    st.write(f"Tipo de venda mais usado: {tipo_mais_usado} com {quantidade_mais_usado} vendas")
    st.write(f"Tipo de venda menos usado: {tipo_menos_usado} com {quantidade_menos_usado} vendas")