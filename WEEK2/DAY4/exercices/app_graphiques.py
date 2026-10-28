# WEEK 2 · DAY 4 · Application rapide : 3 graphiques   (3 min)
#
# Lance :  py app_graphiques.py
# Le programme crée 3 images PNG dans ce dossier. Ouvre-les dans VS Code.
#
# Pour chaque graphique, réponds à la question en le regardant :
# 1_histogramme.png : autour de quelle note se trouvent la plupart des élèves ? ...
# 2_barres.png      : quelle ville a la meilleure moyenne ?                    ...
# 3_nuage.png       : plus on révise, plus la note… monte, baisse, ou rien ?  ...

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("classe.csv")

# 1. HISTOGRAMME : comment les notes sont-elles réparties ?
plt.figure()
plt.hist(df["maths"], bins=8, color="#1f3a6e")
plt.title("Répartition des notes de maths")
plt.xlabel("Note sur 20")
plt.ylabel("Nombre d'élèves")
plt.savefig("1_histogramme.png")

# 2. BARRES : comparer des catégories
plt.figure()
moyennes = df.groupby("ville")["maths"].mean()
plt.bar(moyennes.index, moyennes.values, color="#2c6b4f")
plt.title("Moyenne de maths par ville")
plt.ylabel("Moyenne sur 20")
plt.savefig("2_barres.png")

# 3. NUAGE DE POINTS : y a-t-il un lien entre deux colonnes ?
plt.figure()
plt.scatter(df["heures_revision"], df["maths"], color="#a3283a")
plt.title("Heures de révision et note de maths")
plt.xlabel("Heures de révision")
plt.ylabel("Note sur 20")
plt.savefig("3_nuage.png")

print("✅ 3 graphiques créés : 1_histogramme.png, 2_barres.png, 3_nuage.png")
