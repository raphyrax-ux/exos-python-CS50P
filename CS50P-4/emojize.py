import emoji

e = input()
resultat = emoji.emojize(f"{e}", language="alias")
print(resultat)

