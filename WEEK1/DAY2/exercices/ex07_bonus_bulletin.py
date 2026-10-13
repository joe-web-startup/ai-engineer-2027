# EXERCICE 7 · BONUS · Mini-projet « bulletin »
#
# Affiche ce rapport :
#
#   === BULLETIN ===
#   Notes : [12, 7, 15, 9, 18]
#   Moyenne : 12.2
#   Admis : 3 / 5
#   Meilleure note : 18
#   Résultat : ADMIS
#
# (Résultat = ADMIS si la moyenne est >= 10, sinon AJOURNÉ.)

# On RÉUTILISE les fonctions de l'exercice 6 au lieu de les réécrire.
# C'est le principe d'un module : écrire une fois, utiliser partout.
from ex06_fonctions import moyenne, est_admis

notes = [12, 7, 15, 9, 18]

# Compréhension (fiche F2.DAY1) : la liste des notes admises, puis on la compte.
nb_admis = len([n for n in notes if est_admis(n)])
moy = moyenne(notes)

print("=== BULLETIN ===")
print(f"Notes : {notes}")
print(f"Moyenne : {moy}")
print(f"Admis : {nb_admis} / {len(notes)}")
print(f"Meilleure note : {max(notes)}")
# Condition écrite sur une ligne : valeur_si_vrai if condition else valeur_si_faux
print(f"Résultat : {'ADMIS' if moy >= 10 else 'AJOURNÉ'}")
