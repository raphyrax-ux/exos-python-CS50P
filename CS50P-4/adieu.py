import inflect

p = inflect.engine()
liste = []

while True:
    try:
        nom = input()
        liste.append(nom)
    except EOFError:
        phrase = p.join(liste)
        print(f"Adieu {phrase}")
        break
