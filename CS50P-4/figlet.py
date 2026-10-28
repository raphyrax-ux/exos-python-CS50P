import sys
import pyfiglet
import random

figlet = pyfiglet.Figlet()
polices_disponibles = figlet.getFonts()
texte = input("Input : ")

if len(sys.argv) == 1:
    police_aleatoire = random.choice(polices_disponibles)
    figlet.setFont(font=police_aleatoire)
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "-font":  
        if sys.argv[2] in polices_disponibles:
            figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Erreur lors de la saisie 1")
else:
    print(len(sys.argv))
    sys.exit("Erreur lors de la saisie 2")

nouv = figlet.renderText(texte)
print(nouv)