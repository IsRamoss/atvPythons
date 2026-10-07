import pandas as pd

df = pd.read_csv("transacoes.csv", encoding="latin1")
print("--- DATAFRAME ORIGINAL ---")
print(df)

dfNulos = df[df["valor"].isna()]
print("--- DATAFRAME VALORES NULOS ---")
print(dfNulos)

medianas = df.groupby("estado_cliente")["valor"].median()
print("\n--- MEDIANAS POR ESTADO ---")
print(medianas)

df["valor"] = df["valor"].fillna(df.groupby("estado_cliente")["valor"].transform("median"))
print("--- DATAFRAME PREENCHIDO ---")
print(df)

df["plataforma"] = 'Mobile'
print("--- DATAFRAME COM MOBILE ---")
print(df)

df["data_transacao"]= df["data_transacao"].astype('datetime64[ns]').dt.tz_localize("America/Sao_Paulo")
print("--- DATAFRAME MODIFICADO A TIMEZONE ---")
print(df)

df["dia_semana"] = df["data_transacao"].dt.weekday
df["mes"] = df["data_transacao"].dt.month
print("--- DATAFRAME COM DIA DA SEMANA E MÊS ---")
print(df)

duplicadas = df[df.duplicated()]
print("--- TRANSAÇÕES DUPLICADAS ---")
print(duplicadas)

df = df.drop_duplicates(keep="first")
print("--- DATAFRAME SEM AS DUPLICADAS ---")
print(df)

dfFiltrado = df[
    ((df['estado_cliente'] == 'SP') | (df['estado_cliente'] == 'MG')) &
    (df['valor'] > 5000.0)
]
print("--- TRANSAÇÕES COM FILTRO ---")
print(dfFiltrado)

risco_dict = {
    'C100': 'Baixo',
    'C101': 'Alto', 
    'C102': 'Médio',
    'C103': 'Alto',
    'C104': 'Baixo'}

dfFiltrado["Risco"] = dfFiltrado["id_cliente"].map(risco_dict)
print(dfFiltrado)

tabela_agrupada = dfFiltrado.pivot_table(
    index="mes",               # Linhas: Mês
    columns="risco",     # Colunas: Nível de Risco
    values="valor",            # Valores: Coluna 'valor'
    aggfunc="sum",             # Agregação: Soma
    fill_value=0,              # Preenche os sem dados com 0 em vez de NaN
    margins=True,              # Inclui as linhas e colunas de subtotais
    margins_name="Total"       # Nome do rótulo do subtotal
)

print("--- TABELA AGRUPADA POR MÊS E RISCO ---")
print(tabela_agrupada)