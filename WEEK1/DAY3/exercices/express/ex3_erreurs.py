# DAY 3 · EXERCICE 3 · try / except   (15 min)
# Lance avec :  py ex3_erreurs.py
#
# a) Écris trier(textes) qui reçoit une liste de textes et RENVOIE (valides, rejets) :
#    - valides = les textes convertibles en float, convertis (ex : "12" → 12.0)
#    - rejets  = les textes impossibles à convertir, tels quels
#    Utilise try / except ValueError. Interdit d'utiliser if pour tester le texte.
#
# b) Écris lire_ou_vide(chemin) qui RENVOIE le contenu du fichier,
#    ou "" si le fichier n'existe pas (try / except FileNotFoundError).
#
# ✍️ TON CODE ICI



# ----- Tests : NE PAS MODIFIER -----
valides, rejets = trier(["12", "abc", "15.5", "", "8"])
assert valides == [12.0, 15.5, 8.0]
assert rejets == ["abc", ""]
assert lire_ou_vide("ce_fichier_n_existe_pas.txt") == ""
assert lire_ou_vide("notes.txt").startswith("14")
print("✅ Exercice 3 validé")
