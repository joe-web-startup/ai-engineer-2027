# RÉVISION 3 · Compter avec la tirelire 🐷   (10 min)
#
# Rappel :  c = 1      → j'efface et j'écris 1      ❌ pour compter
#           c = c + 1  → j'ajoute 1 à ce qu'il y a  ✅ pour compter
#
# Compte combien de notes sont supérieures ou égales à 10, puis affiche le nombre.
# Résultat attendu : 4

notes = [12, 8, 15, 9, 10, 17]

# ✍️ TON CODE ICI
c = 0 
for note in notes:
    if note >= 10:
        c = c + 1
print(c)