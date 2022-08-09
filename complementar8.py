import pandas as pd

df = pd.read_csv("notas_alunos.csv")
df["media"] = (df["notas_1"] + df["notas_2"]) / 2
df.loc[(df["media"] >= 7) & (df["faltas"] <= 5), 'situacao'] = 'Aprovado'
df['situacao'].fillna('Reprovado', inplace=True) 


# maior numero de faltas
maior_num_faltas = df["faltas"].max()
print("Maior numero de faltas: " +str(maior_num_faltas))

# maior media
maior_media = df["media"].max()
print("Maior media: " +str(maior_media))

# media geral das notas dos alunos
media_geral = df["media"].mean()
print("a media geral das notas dos alunos: " +str(media_geral))

df.to_csv("alunos_situacao.csv")