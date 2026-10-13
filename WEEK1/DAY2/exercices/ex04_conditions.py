# EXERCICE 4 · Décider avec if / elif / else (section 6) · 10 min
#
# C'est exactement ce que fait ExamPredict pour afficher la priorité d'un thème.
#
# Avec la variable score ci-dessous, affiche :
#   "HIGH"    si score >= 80
#   "MEDIUM"  si score >= 50
#   "LOW"     sinon
#
# Teste avec score = 92, puis 65, puis 10 (change la valeur, Ctrl + S, relance).

score = 65

# ✍️ TON CODE ICI

# Python teste les conditions DANS L'ORDRE et s'arrête à la première vraie.
if score >= 80:          # 65 >= 80 ? Non → on passe à la suite
    print("HIGH")
elif score >= 50:        # 65 >= 50 ? Oui → on affiche MEDIUM et on s'arrête
    print("MEDIUM")
else:                    # seulement si AUCUNE condition au-dessus n'était vraie
    print("LOW")

# Pourquoi l'ordre compte : si on testait d'abord >= 50, un score de 92
# afficherait MEDIUM, car 92 >= 50 est vrai aussi.
