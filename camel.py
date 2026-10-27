def main():
    texte = input("Entrer du texte en CamelCase : ")
    resultat = ""
    for lettre in texte:
        if lettre.isupper():
            resultat += "_" + lettre.lower()
        else:
            resultat += lettre
    print(texte)


main()
