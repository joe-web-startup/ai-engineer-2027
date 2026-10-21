# DAY 3 · EXERCICE 2 · Lire un fichier, écrire du JSON   (15 min)
# Lance avec :  py ex2_fichiers_json.py   (depuis le dossier express)
#
# a) Écris lire_nombres(chemin) qui lit notes.txt (un nombre par ligne,
#    certaines lignes vides) et RENVOIE la liste des nombres (float).
#
# b) Écris sauver_stats(nombres, chemin) qui écrit dans un fichier JSON :
#    {"nb": <nombre de notes>, "moyenne": <moyenne arrondie à 2 décimales>}
#    Indice : round(x, 2)   et   json.dump(dico, f, indent=2)
#
# c) Écris relire(chemin) qui RENVOIE le dictionnaire relu depuis le JSON.

import json

# ✍️ TON CODE ICI



# ----- Tests : NE PAS MODIFIER -----
notes = lire_nombres("notes.txt")
assert notes == [14.0, 9.5, 17.0, 12.0, 8.0, 15.5]
sauver_stats(notes, "stats.json")
assert relire("stats.json") == {"nb": 6, "moyenne": 12.67}
print("✅ Exercice 2 validé")
