import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def graf_linhas():
    dados = pd.read_csv('Arquivos/dados_linhas.csv', encoding="latin1")
    dados['data'] = pd.to_datetime(dados['data'])
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(20, 10))
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
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
        data=dados, x="regiao", y="vendas_medias",
        hue="categoria", palette="Set2", errorbar=None, ax=ax
    )

    ax.set_title("Média das vendas por categoria e região", fontweight="bold")
    ax.set_ylabel("Média das vendas")
    ax.legend(title="Categoria de produto")

    plt.tight_layout()
    plt.show()
graf_linhas()
graf_barras()