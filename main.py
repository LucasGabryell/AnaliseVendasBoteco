import streamlit as st
import pandas as pd
import dataFunctions

# Substitua 'seu_arquivo.csv' pelo caminho real do seu arquivo CSV
dadosCSV = 'boteco_da_ana_maria_braga.csv'

# Use o método 'read_csv' do pandas para ler o arquivo CSV
dados = pd.read_csv(dadosCSV, sep=";")


# Adicione um título no topo da tela
st.title("Boteco da Ana Maria Braga")

# Crie uma variável para armazenar a opção selecionada
opcao_selecionada = st.radio("Selecione uma opção:", ["Lucros", "Gastos", "Vendas"])

# Exiba as informações com base na opção selecionada
if opcao_selecionada == "Lucros":
    dataFunctions.dados_lucros(dados)
elif opcao_selecionada == "Gastos":
    dataFunctions.dados_gastos(dados)
elif opcao_selecionada == "Vendas":
    dataFunctions.dados_vendas(dados)
