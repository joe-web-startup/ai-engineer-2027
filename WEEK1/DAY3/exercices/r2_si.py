# RÉVISION 2 · if / elif / else   (10 min)
#
# Rappel : if = SI    elif = SINON, SI    else = SINON
#          deux-points ":" à la fin, 4 espaces dessous
#
# Avec la variable temperature, affiche :
#   "manteau"   SI temperature est plus petite que 10
#   "pull"      SINON, SI temperature est plus petite que 20
#   "t-shirt"   SINON
#
# Teste avec 5, puis 15, puis 25 (change la valeur, Ctrl + S, relance).
# Attendu : 5 → manteau · 15 → pull · 25 → t-shirt

temperature = 15

# ✍️ TON CODE ICI
if  temperature <= 10:
    print("manteau") 
elif temperature <= 20:
    print("pull")
else: 
    print("t-shirt")  
