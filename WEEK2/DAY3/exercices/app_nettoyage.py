# WEEK 2 · DAY 3 · Application rapide : nettoyer un dataset sale   (3 min)
#
# Ouvre d'abord eleves_sales.csv et repère les 5 problèmes cachés 🕵️
# Écris tes prédictions, PUIS lance :  py app_nettoyage.py
#
# MES PRÉDICTIONS :
# A (taille au départ)                   : ...
# B (nombre de doublons)                 : ...
# C (notes de maths manquantes ou fausses) : ...
# D (villes après nettoyage)             : ...
# E (taille finale)                      : ...

import pandas as pd

df = pd.read_csv("eleves_sales.csv")
print("A :", df.shape)

# 1. Doublons : la même ligne écrite deux fois
print("B :", df.duplicated().sum())
df = df.drop_duplicates()

# 2. Types : "abc" n'est pas une note → on le transforme en NaN (valeur manquante)
df["maths"] = pd.to_numeric(df["maths"], errors="coerce")
print("C :", df["maths"].isna().sum())

# 3. Valeurs manquantes : on enlève les lignes sans note de maths
df = df.dropna(subset=["maths"])

# 4. Valeurs impossibles : une note doit être entre 0 et 20
df = df[(df["maths"] >= 0) & (df["maths"] <= 20)]

# 5. Texte incohérent : espaces et majuscules
df["ville"] = df["ville"].str.strip().str.lower()
print("D :", df["ville"].value_counts().to_dict())

print("E :", df.shape)
print(df)
