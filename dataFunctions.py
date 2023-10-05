import streamlit as st
import salesGraphicsFunctions
import profitsGraphicsFunctions
import spentGraphicsFunctions
import calendar
import pandas as pd

def dados_vendas(dados):
    # Certifique-se de que a coluna 'Valor Total' seja do tipo float
    dados['Valor Total'] = dados['Valor Total'].str.replace(',', '.').astype(float)

    # Contagem de frequência dos itens do pedido
    contagem_itens = dados['Item do Pedido'].value_counts()

    item_mais_vendido = contagem_itens.idxmax()
    quantidade_mais_vendida = contagem_itens.max()

    item_menos_vendido = contagem_itens.idxmin()
    quantidade_menos_vendida = contagem_itens.min()

    # Encontre o cliente que mais comprou, quanto gastou e quantas compras fez
    clientes_info = dados.groupby('Código do Cliente').agg({'Valor Total': ['sum', 'count']}).reset_index()
    cliente_mais_comprou = clientes_info.loc[clientes_info['Valor Total', 'sum'].idxmax()]
    cliente_mais_comprou_id = cliente_mais_comprou['Código do Cliente']
    gasto_cliente_mais_comprou = cliente_mais_comprou['Valor Total', 'sum']
    compras_cliente_mais_comprou = cliente_mais_comprou['Valor Total', 'count']

    # Exiba as informações, incluindo o tipo de dado do cliente_mais_comprou_id
    st.write(f"Item mais vendido: {item_mais_vendido} ({quantidade_mais_vendida} unidades vendidas)")
    st.write(f"Item menos vendido: {item_menos_vendido} ({quantidade_menos_vendida} unidades vendidas)")
    st.write(f"Cliente que mais comprou (ID): {cliente_mais_comprou_id}")
    st.write(f"Gasto do cliente que mais comprou: R${gasto_cliente_mais_comprou:.2f}")
    st.write(f"Compras feitas pelo cliente que mais comprou: {compras_cliente_mais_comprou}")

    # Barra de seleção para escolher o gráfico
    opcao_grafico = st.selectbox("Escolha o Gráfico", ["Gráfico de Vendas por mês", "Gráfico de Tipos de Venda"])

    # Mostrar o gráfico selecionado com base na escolha do usuário
    if opcao_grafico == "Gráfico de Vendas por mês":
        salesGraphicsFunctions.plot_vendas_mes(dados)
    elif opcao_grafico == "Gráfico de Tipos de Venda":
        salesGraphicsFunctions.plot_vendas_tipo(dados)

def dados_lucros(dados):
    # Certifique-se de que as colunas 'Valor Total' e 'Custo dos Ingredientes' sejam do tipo float
    dados['Valor Total'] = dados['Valor Total'].str.replace(',', '.').astype(float)
    dados['Custo dos Ingredientes'] = dados['Custo dos Ingredientes'].str.replace(',', '.').astype(float)

    # Agrupe os dados por 'Item do Pedido' e calcule o lucro para cada produto
    lucros_por_produto = dados.groupby('Item do Pedido').apply(
        lambda x: (x['Valor Total'] - x['Custo dos Ingredientes']).sum()
    ).reset_index(name='Lucro')

    # Encontre o produto com o maior lucro
    produto_maior_lucro = lucros_por_produto.loc[lucros_por_produto['Lucro'].idxmax()]

    # Encontre o produto com o menor lucro
    produto_menor_lucro = lucros_por_produto.loc[lucros_por_produto['Lucro'].idxmin()]

    # Exiba os resultados
    st.write(f"Produto com maior lucro: {produto_maior_lucro['Item do Pedido']} (Lucro: R${produto_maior_lucro['Lucro']:.2f})")
    st.write(f"Produto com menor lucro: {produto_menor_lucro['Item do Pedido']} (Lucro: R${produto_menor_lucro['Lucro']:.2f})")

    profitsGraphicsFunctions.plot_lucros(dados)


def dados_gastos(dados):
    st.write("### Itens com Maior e Menor Custo dos Ingredientes")

    # Certifique-se de que a coluna 'Custo dos Ingredientes' seja do tipo float
    dados['Custo dos Ingredientes'] = dados['Custo dos Ingredientes'].str.replace(',', '.').astype(float)

    # Encontre o item com o maior custo dos ingredientes
    item_maior_custo = dados.loc[dados['Custo dos Ingredientes'].idxmax()]

    # Encontre o item com o menor custo dos ingredientes
    item_menor_custo = dados.loc[dados['Custo dos Ingredientes'].idxmin()]

    # Exiba os resultados
    st.write(
        f"Item com Maior Custo dos Ingredientes: {item_maior_custo['Item do Pedido']} (Custo: R${item_maior_custo['Custo dos Ingredientes']:.2f})")
    st.write(
        f"Item com Menor Custo dos Ingredientes: {item_menor_custo['Item do Pedido']} (Custo: R${item_menor_custo['Custo dos Ingredientes']:.2f})")

    spentGraphicsFunctions.plot_gastos(dados)
