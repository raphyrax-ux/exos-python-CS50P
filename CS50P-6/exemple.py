# Programme d'exemple pour tester lines.py

import random


def lancer_de():
    """
    Lance un dé à 6 faces.
    Les 4 lignes de ce docstring comptent comme du code.
    """
    # commentaire indenté : ne compte pas
    return random.randint(1, 6)


resultat = lancer_de()   # commentaire en fin de ligne : la ligne compte
print(f"Tu as fait {resultat}")