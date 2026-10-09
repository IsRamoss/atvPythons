import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def graf_linhas():
    dados = pd.read_csv('Arquivos/dados_linhas.csv', encoding="latin1")
    dados['data'] = pd.to_datetime(dados['data'])
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(8, 8))
    sns.lineplot(
        data=dados,
        x="data", y="vendas", hue="loja",
        marker="o", palette=["#2563eb", "#db2777"], linewidth=2, ax=ax
    )
    ax.set_title("Dados de vendas", fontweight="bold")
    ax.set_xlabel("Data")
    ax.set_ylabel("Vendas")
    plt.tight_layout()
    plt.show()

def graf_barras():
    dados = pd.read_csv('Arquivos/dados_barras.csv', encoding="latin1")
    fig, ax = plt.subplots(figsize=(8, 8))

    sns.barplot(
        data=dados, x="regiao", y="vendas_medias",
        hue="categoria", palette="Set2", errorbar=None, ax=ax
    )

    ax.set_title("Média das vendas por categoria e região", fontweight="bold")
    ax.set_ylabel("Média das vendas")
    ax.legend(title="Categoria de produto")

    plt.tight_layout()
    plt.show()
def graf_dispersao():
    dados = pd.read_csv('Arquivos/dados_dispersao.csv', encoding="latin1")
    fig, ax = plt.subplots(figsize=(8, 8))

    sns.scatterplot(
        data=dados, x="altura_cm", y="peso_kg",
        hue="sexo", alpha=0.8, ax=ax
    )
    sns.regplot(data=dados, x="altura_cm", y="peso_kg", scatter=False, color="gray", ax=ax)

    ax.set_title("Relação entre Altura da Pessoa e o Peso", fontweight="bold")
    plt.tight_layout()
    plt.show()
def graf_hist():
    dados = pd.read_csv('Arquivos/dados_distribuicao.csv', encoding="latin1")
    fig, ax = plt.subplots(figsize=(8, 8))
    sns.histplot(
        data=dados, x="idade",
        bins=15, kde=True,
        color="#2563eb", ax=ax
    )

    ax.set_title("Distribuição das idades", fontweight="bold")
    plt.tight_layout()
    plt.show()
def graf_box():
    dados = pd.read_csv('Arquivos/dados_boxplot.csv', encoding="latin1")
    fig, ax = plt.subplots(figsize=(8, 8))

    sns.boxplot(
        data=dados, x="departamento", y="salario",
        palette="Pastel1", ax=ax
    )

    ax.set_title("Dispersão do Valor do Salário por Departamento", fontweight="bold")
    plt.tight_layout()
    plt.show()

def graf_heatmap():
    dados = pd.read_csv('Arquivos/dados_heatmap.csv', encoding="latin1")
    fig, ax = plt.subplots(figsize=(8, 8))

    sns.heatmap(
        dados, annot=True, fmt=".2f",
        cmap="coolwarm", linewidths=.5, ax=ax
    )

    ax.set_title("Matriz de Correlação Numérica", fontweight="bold")
    plt.tight_layout()
    plt.show()

def graf_setor():
    dados = pd.read_csv('Arquivos/dados_pizza.csv', encoding="latin1")
    valores = dados['faturamento'].tolist()
    categorias = dados['canal_venda'].tolist()
    cores = sns.color_palette("Set2")
    fig, ax = plt.subplots(figsize=(8, 8))

    ax.pie(
        valores, labels=categorias, autopct="%1.1f%%",
        startangle=90, colors=cores,
        wedgeprops=dict(width=0.6, edgecolor="white")
    )

    ax.set_title("Distribuição de Faturamento por Categoria", fontweight="bold")
    plt.tight_layout()
    plt.show()

    
grafico = ""
while grafico != "0":
    print("Insira o Número do gráfico que você quer rodar:")
    grafico = input("0-Encerrar\n1-Linhas\n2-Barras\n3-Dispersao\n4-Histograma\nResposta: ")
    match grafico:
        case "1":
            graf_linhas()
        case "2":
            graf_barras()
        case "3":
            graf_dispersao()
        case "4":
            graf_hist()
        case "5":
            graf_box()
        case "6":
            graf_heatmap()
        case "7":
            graf_setor()
        case "0":
            print("Encerrando...")
        case _:
            print("Opção inválida") 





