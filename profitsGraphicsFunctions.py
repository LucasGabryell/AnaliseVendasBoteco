import plotly.express as px
import pandas as pd
import streamlit as st
import calendar


def plot_lucros(dados):
    # Certifique-se de que a coluna 'Data da Venda' seja do tipo datetime
    dados['Data da Venda'] = pd.to_datetime(dados['Data da Venda'], format='%d/%m/%Y')

    # Crie uma nova coluna 'Mês' para extrair o mês da data de venda e trate os valores ausentes
    dados['Mês'] = dados['Data da Venda'].dt.month.fillna(-1).astype(int)

    # Calcule os lucros mensais
    dados['Lucro Mensal'] = dados['Valor Total'] - dados['Custo dos Ingredientes']

    # Exclua os meses não informados (-1)
    dados = dados[dados['Mês'] != -1]

    # Agrupe os dados por mês e calcule o lucro total de cada mês
    lucros_mensais = dados.groupby('Mês')['Lucro Mensal'].sum().reset_index()

    # Mapeie os números de mês para nomes completos
    lucros_mensais['Mês'] = lucros_mensais['Mês'].apply(lambda x: calendar.month_name[x])

    # Encontre o mês com o maior lucro
    mes_maior_lucro = lucros_mensais.loc[lucros_mensais['Lucro Mensal'].idxmax()]

    # Encontre o mês com o menor lucro
    mes_menor_lucro = lucros_mensais.loc[lucros_mensais['Lucro Mensal'].idxmin()]

    # Crie um gráfico de barras empilhadas usando Plotly Express
    fig = px.bar(lucros_mensais, x='Mês', y='Lucro Mensal', title='Lucros por Mês')
    fig.update_xaxes(title_text='Mês')
    fig.update_yaxes(title_text='Lucro Mensal')

    # Mostrar o gráfico
    st.plotly_chart(fig)

    # Exibir o mês com o maior e o menor lucro
    st.write(f"Mês com maior lucro: {mes_maior_lucro['Mês']} (Lucro: R${mes_maior_lucro['Lucro Mensal']:.2f})")
    st.write(f"Mês com menor lucro: {mes_menor_lucro['Mês']} (Lucro: R${mes_menor_lucro['Lucro Mensal']:.2f})")
