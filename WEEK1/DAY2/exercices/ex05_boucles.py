# EXERCICE 5 · Les boucles et les listes (sections 7 et 8) · 12 min

notes = [12, 7, 15, 9, 18, 11]

# A. Avec une boucle for, affiche chaque note sur une ligne.
# ✍️ TON CODE ICI
for note in notes:       # « note » prend la valeur 12, puis 7, puis 15...
    print(note)


# B. Calcule la SOMME des notes avec une boucle (sans utiliser sum).
# ✍️ TON CODE ICI
total = 0                # la tirelire commence vide
for note in notes:
    total = total + note # à chaque tour, on met la note dans la tirelire
print("Somme :", total)  # 72


# C. Compte combien de notes sont >= 10 (réponse attendue : 4).
# ✍️ TON CODE ICI
compteur = 0
for note in notes:
    if note >= 10:              # on ne compte que les notes qui passent le test
        compteur = compteur + 1
print("Notes >= 10 :", compteur)  # 4


# D. Affiche la moyenne avec sum(notes) / len(notes).
# ✍️ TON CODE ICI
# sum = la somme de toute la liste, len = le nombre d'éléments.
print("Moyenne :", sum(notes) / len(notes))  # 12.0
