import matplotlib.pyplot as plt
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

df["valor"] = df["valor"].fillna(
    df.groupby("estado_cliente")["valor"].transform("median")
)
print("--- DATAFRAME PREENCHIDO ---")
print(df)

df["plataforma"] = "Mobile"
print("--- DATAFRAME COM MOBILE ---")
print(df)

df["data_transacao"] = df["data_transacao"].astype(
    "datetime64[ns]"
).dt.tz_localize("America/Sao_Paulo")
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
    ((df["estado_cliente"] == "SP") | (df["estado_cliente"] == "RJ"))
    & (df["valor"] > 5000.0)
    & (df["mes"] == 9)
].copy()
print("--- TRANSAÇÕES COM FILTRO ---")
print(dfFiltrado)

risco_dict = {
    "C100": "Baixo",
    "C101": "Alto",
    "C102": "Médio",
    "C103": "Alto",
    "C104": "Baixo",
}

dfFiltrado["risco"] = dfFiltrado["id_cliente"].map(risco_dict)
print("--- DATAFRAME FILTRADO COM RISCO ---")
print(dfFiltrado)

pivot_risco = pd.pivot_table(
    dfFiltrado,
    values="valor",
    index="mes",
    columns="risco",
    aggfunc="sum",
    margins=True,
    margins_name="Total",
)

print("--- PIVOT TABLE RISCO ---")
print(pivot_risco)


def calcular_zscore_por_estado(
    df, col_valor="valor", col_estado="estado_cliente"
):
    media_estado = df.groupby(col_estado)[col_valor].transform("mean")
    desvio_estado = df.groupby(col_estado)[col_valor].transform("std")
    z_score = (df[col_valor] - media_estado) / desvio_estado
    return z_score


dfFiltrado["z_score"] = calcular_zscore_por_estado(dfFiltrado)
print("--- DATAFRAME FILTRADO COM Z-SCORE ---")
print(dfFiltrado)

anomalias = dfFiltrado[dfFiltrado["z_score"] > 2.5].copy()
print("--- ANOMALIAS ---")
print(anomalias)

df_diario = (
    dfFiltrado.groupby(dfFiltrado["data_transacao"].dt.date)["valor"]
    .sum()
    .reset_index()
)

df_diario["media_movel_7d"] = df_diario["valor"].rolling(7).mean()
print("--- DATAFRAME DIÁRIO COM MÉDIA MÓVEL ---")
print(df_diario)

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(
    df_diario["data_transacao"],
    df_diario["valor"],
    label="Total Diário (R$)",
    color="steelblue",
    alpha=0.7,
    linewidth=1.5,
    marker="o",
)

ax.plot(
    df_diario["data_transacao"],
    df_diario["media_movel_7d"],
    label="Média Móvel (7 dias)",
    color="crimson",
    linewidth=2.5,
)

ax.set_ylim(bottom=0)

ax.set_title(
    "Evolução Diária do Valor de Transações e Média Móvel (7 Dias)",
    fontsize=14,
    pad=15,
)
ax.set_xlabel("Data da Transação", fontsize=12)
ax.set_ylabel("Valor Total (R$)", fontsize=12)
ax.legend(loc="upper left", frameon=True)

ax.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()