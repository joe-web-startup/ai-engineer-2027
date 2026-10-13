# EXERCICE 6 · Les fonctions et tes premiers tests (section 9) · 15 min
#
# En bas, des "assert" vérifient les fonctions automatiquement :
#   - si tout est juste, le programme affiche "✅ Tous les tests passent"
#   - sinon, une AssertionError indique la ligne du test raté.
# Lance avec :  py ex06_fonctions.py


def moyenne(notes):
    """Renvoie la moyenne d'une liste de notes."""
    # return RENVOIE le résultat : on peut le ranger dans une variable ou le tester.
    # (print l'afficherait seulement, et les tests ne pourraient pas le vérifier.)
    return sum(notes) / len(notes)


def est_admis(note):
    """Renvoie True si la note est au moins 10, sinon False."""
    # Une comparaison donne déjà True ou False : pas besoin de if.
    return note >= 10


# ----- Les tests : NE PAS MODIFIER -----
assert moyenne([10, 20]) == 15
assert moyenne([12, 15, 9]) == 12
assert est_admis(12) == True
assert est_admis(10) == True
assert est_admis(8) == False
print("✅ Tous les tests passent")
