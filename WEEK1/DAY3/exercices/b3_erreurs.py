# BLOC 3 · Gestion des erreurs (fiche F2.DAY3.WEEK1, sections 1 à 8)
# Lance avec :  py b3_erreurs.py

# 3.B : écris ta prédiction, PUIS décommente pour vérifier.
# MA PRÉDICTION : ...
# try:
#     x = int("7")
#     y = int("sept")
#     print("A")
# except ValueError:
#     print("B")
# print(x)


# 3.C : en_nombre(texte) renvoie le nombre, ou None si la conversion échoue
# ✍️ TON CODE ICI


# 3.D : moyenne_sure(notes) renvoie la moyenne, ou 0 si la liste est vide (sans if)
# ✍️ TON CODE ICI


# 3.E : lire_texte(chemin) renvoie le contenu du fichier, ou "" s'il n'existe pas
#       (Méthode 5.1)
# ✍️ TON CODE ICI


# ----- Tests : décommente-les au fur et à mesure -----
# assert en_nombre("12.5") == 12.5
# assert en_nombre("abc") is None
# assert moyenne_sure([10, 20]) == 15
# assert moyenne_sure([]) == 0
# assert lire_texte("fichier_qui_n_existe_pas.txt") == ""
# print("✅ Bloc 3 validé")
