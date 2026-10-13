# EXERCICE 2 · Les types (section 3) · 8 min
#
# Ce programme PLANTE. C'est fait exprès.
# 1. Lance-le :  python ex02_types.py
# 2. Lis l'erreur DE BAS EN HAUT : quel type d'erreur ? quelle ligne ?
# 3. Corrige UNE SEULE ligne pour que le programme affiche 30.
#    Indice : "25" est un texte. Comment le transformer en nombre ?

age_dans_fichier = "25"
# CORRECTION : "25" est du TEXTE (un dessin sur un papier).
# int(...) le transforme en VRAI nombre, avec lequel on peut calculer.
age_plus_5 = int(age_dans_fichier) + 5
print(age_plus_5)

# 4. À TOI : affiche le type de 3.5, de "3.5" et de True avec print(type(...))
# ✍️ TON CODE ICI
print(type(3.5))    # <class 'float'> : nombre à virgule
print(type("3.5"))  # <class 'str'>   : guillemets = texte
print(type(True))   # <class 'bool'>  : vrai ou faux


