import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import unicodedata

st.set_page_config(
    page_title="Dashboard de Analise de Dados",
    layout="wide",
    initial_sidebar_state="expanded"
)

sns.set_theme(style="whitegrid")

st.sidebar.title("Informacoes do Aluno")
st.sidebar.write("**Nome:** Isaac Ramos")
st.sidebar.write("**Numero da Chamada:** 20")
st.sidebar.write("**Turma:** 3B2")

st.title("Dashboard de Visualizacao de Dados - Atividade 06")
st.markdown("---")

def carregar_e_limpar_dados(caminho_csv):
    try:
        dados = pd.read_csv(caminho_csv, encoding="utf-8")
    except UnicodeDecodeError:
        dados = pd.read_csv(caminho_csv, encoding="latin1")

    for col in dados.select_dtypes(include=['object']).columns:
        dados[col] = dados[col].astype(str)
        dados[col] = dados[col].apply(
            lambda x: unicodedata.normalize('NFKD', x).encode('ASCII', 'ignore').decode('utf-8')
        )
        dados[col] = dados[col].str.strip()

    return dados

def graf_linhas():
    dados = carregar_e_limpar_dados('Arquivos/dados_linhas.csv')
    dados['data'] = pd.to_datetime(dados['data'])
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.lineplot(
        data=dados, x="data", y="vendas", hue="loja",
        marker="o", palette=["#2563eb", "#db2777"], linewidth=2, ax=ax
    )
    ax.set_title("Dados de vendas", fontweight="bold")
    ax.set_xlabel("Data")
    ax.set_ylabel("Vendas")
    plt.xticks(rotation=35)
    plt.tight_layout()
    return fig

def graf_barras():
    dados = carregar_e_limpar_dados('Arquivos/dados_barras.csv')
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.barplot(
        data=dados, x="regiao", y="vendas_medias",
        hue="categoria", palette="Set2", errorbar=None, ax=ax
    )
    ax.set_title("Media de vendas por categoria e regiao", fontweight="bold")
    ax.set_ylabel("Media das vendas")
    ax.legend(title="Categoria", fontsize='small')
    plt.tight_layout()
    return fig

def graf_dispersao():
    dados = carregar_e_limpar_dados('Arquivos/dados_dispersao.csv')
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.scatterplot(
        data=dados, x="altura_cm", y="peso_kg",
        hue="sexo", alpha=0.8, ax=ax
    )
    sns.regplot(data=dados, x="altura_cm", y="peso_kg", scatter=False, color="gray", ax=ax)
    ax.set_title("Relacao entre Altura e Peso", fontweight="bold")
    plt.tight_layout()
    return fig

def graf_hist():
    dados = carregar_e_limpar_dados('Arquivos/dados_distribuicao.csv')
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.histplot(
        data=dados, x="idade", bins=15, kde=True,
        color="#2563eb", ax=ax
    )
    ax.set_title("Distribuicao das idades", fontweight="bold")
    plt.tight_layout()
    return fig

def graf_box():
    dados = carregar_e_limpar_dados('Arquivos/dados_boxplot.csv')
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.boxplot(
        data=dados, x="departamento", y="salario",
        palette="Pastel1", ax=ax
    )
    ax.set_title("Salario por Departamento", fontweight="bold")
    plt.xticks(rotation=25)
    plt.tight_layout()
    return fig

def graf_heatmap():
    dados = carregar_e_limpar_dados('Arquivos/dados_heatmap.csv')
    matriz = dados.pivot(
        index="dia_semana", columns="horario", values="movimento_clientes"
    )
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.heatmap(
        matriz, annot=True, fmt=".2f",
        cmap="coolwarm", linewidths=.5, ax=ax
    )
    ax.set_title("Movimento por Horario", fontweight="bold")
    plt.tight_layout()
    return fig

def graf_setor():
    dados = carregar_e_limpar_dados('Arquivos/dados_pizza.csv')
    valores = dados['faturamento'].tolist()
    categorias = dados['canal_venda'].tolist()
    cores = sns.color_palette("Set2")
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.pie(
        valores, labels=categorias, autopct="%1.1f%%",
        startangle=90, colors=cores,
        wedgeprops=dict(width=0.6, edgecolor="white")
    )
    ax.set_title("Faturamento por Categoria", fontweight="bold")
    plt.tight_layout()
    return fig

def graf_frequencia():
    dados = carregar_e_limpar_dados('Arquivos/dados_frequencia.csv')
    agrupado = dados["tipo_atendimento"].value_counts()
    valores = agrupado.values
    cores = sns.color_palette("Set2")
    fig, ax = plt.subplots(figsize=(5, 4))
    rotulos = [f"{categoria} ({qtd})" for categoria, qtd in agrupado.items()]
    ax.pie(
        valores, labels=rotulos, autopct="%1.1f%%",
        startangle=90, colors=cores,
        wedgeprops=dict(width=0.6, edgecolor="white")
    )
    ax.set_title("Chamados por Categoria", fontweight="bold")
    plt.tight_layout()
    return fig

def graf_regressao():
    dados = carregar_e_limpar_dados('Arquivos/dados_regressao.csv')
    dados['renda_mensal'] = pd.to_numeric(dados['renda_mensal'], errors='coerce')
    dados['gasto_mensal'] = pd.to_numeric(dados['gasto_mensal'], errors='coerce')
    dados = dados.dropna(subset=['renda_mensal', 'gasto_mensal'])

    fig, ax = plt.subplots(figsize=(5, 4))
    sns.scatterplot(
        data=dados, x="renda_mensal", y="gasto_mensal",
        alpha=0.8, ax=ax
    )
    sns.regplot(data=dados, x="renda_mensal", y="gasto_mensal", scatter=False, color="gray", ax=ax)
    ax.set_title("Renda vs Gasto Mensal", fontweight="bold")
    plt.tight_layout()
    return fig

col1, col2, col3 = st.columns(3)

with col1:
    st.pyplot(graf_linhas())
    st.info("**Analise:** O grafico de linhas acompanha a evolucao temporal das vendas por loja, permitindo identificar tendencias de crescimento, sazonalidades e periodos de maior volume comercial.")

with col2:
    st.pyplot(graf_barras())
    st.info("**Analise:** O grafico de barras compara a media de vendas de diferentes categorias de produtos agrupadas por regiao, destacando quais regioes possuem maior desempenho em produtos especificos.")

with col3:
    st.pyplot(graf_dispersao())
    st.info("**Analise:** O grafico de dispersao mostra a correlacao entre a altura e o peso dos individuos, divididos por sexo. A linha de regressao cinza evidencia uma tendencia positiva entre as variaveis.")

st.markdown("---")

col4, col5, col6 = st.columns(3)

with col4:
    st.pyplot(graf_hist())
    st.info("**Analise:** O histograma exibe a frequencia e distribuicao etaria do publico amostrado. A curva de densidade (KDE) ajuda a identificar a faixa de idade com maior concentracao de dados.")

with col5:
    st.pyplot(graf_box())
    st.info("**Analise:** O boxplot apresenta a variacao salarial entre diferentes departamentos, permitindo visualizar a mediana, a amplitude interquartil e a ocorrencia de possiveis valores discrepantes (outliers).")

with col6:
    st.pyplot(graf_heatmap())
    st.info("**Analise:** O mapa de calor avalia a intensidade de fluxo de clientes de acordo com o dia da semana e o horario, identificando com precisao os horarios de pico e de menor movimento.")

st.markdown("---")

col7, col8, col9 = st.columns(3)

with col7:
    st.pyplot(graf_setor())
    st.info("**Analise:** O grafico de rosca ilustra a participacao percentual de cada canal de venda no faturamento total da empresa, facilitando a visualizacao dos canais mais lucrativos.")

with col8:
    st.pyplot(graf_frequencia())
    st.info("**Analise:** Apresenta a proporcao percentual e a contagem total de chamados recebidos por tipo de atendimento, auxiliando na alocacao de recursos e suporte ao cliente.")

with col9:
    st.pyplot(graf_regressao())
    st.info("**Analise:** A analise de regressao exibe a relacao entre a renda mensal e o gasto mensal dos consumidores. A tendencia mostra como o aumento do rendimento afeta diretamente os gastos.")