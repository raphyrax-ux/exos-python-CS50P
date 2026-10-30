import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python File")

try:
    with open(sys.argv[1]) as fichier:
        compteur = 0
        for ligne in fichier:
            if not ligne.strip() == "" and not ligne.lstrip().startswith("#"):
                compteur += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(compteur)