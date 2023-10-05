import streamlit as st
import pandas as pd
import plotly.express as px
import calendar


def plot_gastos(dados):
    st.write("### Gráfico de Gastos por Mês")

    # Certifique-se de que a coluna 'Data da Venda' seja do tipo datetime
    dados['Data da Venda'] = pd.to_datetime(dados['Data da Venda'], format='%d/%m/%Y')

    # Crie uma nova coluna 'Mês' para extrair o mês da data de venda
    dados['Mês'] = dados['Data da Venda'].dt.month

    # Remova as linhas que contêm valores ausentes na coluna 'Custo dos Ingredientes'
    dados = dados.dropna(subset=['Custo dos Ingredientes'])

    # Remova as linhas correspondentes ao mês de dezembro (Mês 12)
    dados = dados[dados['Mês'] != 12]

    # Certifique-se de que a coluna 'Mês' seja do tipo int antes de continuar
    dados['Mês'] = dados['Mês'].astype(int)

    # Calcule os gastos mensais
    gastos_mensais = dados.groupby('Mês')['Custo dos Ingredientes'].sum().reset_index()

    # Mapeie os números de mês para nomes completos
    gastos_mensais['Mês'] = gastos_mensais['Mês'].apply(lambda x: calendar.month_name[x])

    # Encontre o mês com o maior e o menor gasto
    mes_maior_gasto = gastos_mensais.loc[gastos_mensais['Custo dos Ingredientes'].idxmax()]
    mes_menor_gasto = gastos_mensais.loc[gastos_mensais['Custo dos Ingredientes'].idxmin()]

    # Crie um gráfico de barras empilhadas usando Plotly Express
    fig = px.bar(gastos_mensais, x='Mês', y='Custo dos Ingredientes', title='Gastos por Mês')
    fig.update_xaxes(title_text='Mês')
    fig.update_yaxes(title_text='Gastos')

    # Mostrar o gráfico
    st.plotly_chart(fig)

    # Exibir o mês com o maior e o menor gasto abaixo do gráfico
    st.write(
        f"Mês com maior gasto: {mes_maior_gasto['Mês']} (Gasto: R${mes_maior_gasto['Custo dos Ingredientes']:.2f})")
    st.write(
        f"Mês com menor gasto: {mes_menor_gasto['Mês']} (Gasto: R${mes_menor_gasto['Custo dos Ingredientes']:.2f})")
