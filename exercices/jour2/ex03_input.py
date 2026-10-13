# EXERCICE 3 · print et input (section 4) · 10 min
#
# Écris un programme qui :
#   1. demande le prénom de l'élève
#   2. demande sa note de maths (sur 20)
#   3. demande sa note de physique (sur 20)
#   4. affiche :  "Joseph, ta moyenne est 13.5"   (avec une f-string)
#
# Rappel : input() renvoie TOUJOURS du texte. Pense à float(...).
# Lance avec :  py ex03_input.py
#
# ✍️ TON CODE ICI

# input() pose la question et attend que l'utilisateur tape une réponse.
prenom = input("Ton prénom ? ")

# input() renvoie du texte ("14"). float(...) le transforme en nombre (14.0),
# sinon on ne pourrait pas faire de calcul (c'est le piège de l'exercice 2).
note_maths = float(input("Note de maths ? "))
note_physique = float(input("Note de physique ? "))

# Les parenthèses forcent l'addition AVANT la division.
moyenne = (note_maths + note_physique) / 2

# f-string : tout ce qui est entre { } est remplacé par sa valeur.
print(f"{prenom}, ta moyenne est {moyenne}")
