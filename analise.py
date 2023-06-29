import pandas as pd  #importei a biblioteca pandas 
import plotly.express as px #importei a biblioteca plotly, podendo assim criar gráficos

tabela = pd.read_excel("ClientesBanco.xlsx")   #importei a base de dados
tabela = tabela.drop("CLIENTNUM", axis=1)   #exclui uma coluna

print(tabela)

tabela = tabela.dropna() 
print(tabela.info())  #exibi as informações de valores vazios nas colunas e informações adicionais

print(tabela.describe().round(1)) #describe() resumo da base de dados, round(1) deixa as informações com uma casa decimal facilitando a análise 

qtd_categoria = tabela["Categoria"].value_counts()
print(qtd_categoria)


qtd_categoria_perc = tabela["Categoria"].value_counts(normalize=True)
print(qtd_categoria_perc)


for coluna in tabela:  #percorrendo cada coluna da Base de Dados
    grafico = px.histogram(tabela, x= coluna, color= "Categoria")  #criando gráfico
    grafico.show()  #exibindo os gráficos