# WEEK 2 · DAY 2 · Application rapide Pandas   (3 min)
#
# Ouvre d'abord eleves.csv pour voir le tableau.
# Écris tes prédictions, PUIS lance :  py app_pandas.py
#
# MES PRÉDICTIONS :
# A (taille du tableau) : ...
# B (moyenne en maths)  : ...
# C (élèves avec maths >= 12) : ...
# D (meilleure moyenne générale) : ...

import pandas as pd

df = pd.read_csv("eleves.csv")
print(df)                                   # le tableau entier
print("A :", df.shape)                      # (lignes, colonnes)
print("B :", df["maths"].mean())            # une colonne → sa moyenne
print("C :", df[df["maths"] >= 12]["nom"].tolist())   # filtrer les lignes
df["moyenne"] = (df["maths"] + df["physique"]) / 2    # créer une colonne
print("D :", df["moyenne"].max())
