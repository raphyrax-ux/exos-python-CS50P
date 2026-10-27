voyelles = ["A", "E", "I", "O", "U", "Y"]
texte = input("Entrez du texte : ")
for lettre in texte.upper():
    if lettre in voyelles:
        texte = texte.replace(lettre.lower(), "")
        texte = texte.replace(lettre, "")
print(texte)