# DAY 3 · EXERCICE 1 · Fonctions et return   (10 min)
# Lance avec :  py ex1_fonctions.py
#
# a) Écris pourcentage(note, bareme=20) qui RENVOIE la note convertie sur 100.
#    pourcentage(15) → 75.0      pourcentage(8, bareme=10) → 80.0
#
# b) Écris mention(p) qui RENVOIE :
#    "Très bien" si p >= 80,  "Admis" si p >= 50,  sinon "Ajourné"
#
# c) Utilise les DEUX fonctions ensemble pour afficher la mention d'un 13/20.
#
# ✍️ TON CODE ICI



# ----- Tests : NE PAS MODIFIER -----
assert pourcentage(15) == 75
assert pourcentage(8, bareme=10) == 80
assert mention(85) == "Très bien"
assert mention(50) == "Admis"
assert mention(20) == "Ajourné"
assert mention(pourcentage(13)) == "Admis"
print("✅ Exercice 1 validé")
