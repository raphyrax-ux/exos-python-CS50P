import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1]) as fichier_in, open(sys.argv[2], "w", newline="") as fichier_out:
        lecture = csv.DictReader(fichier_in)
        ecriture = csv.DictWriter(fichier_out, fieldnames=["first", "last", "house"])
        ecriture.writeheader()
        for ligne in lecture:
            last, first = ligne["name"].split(", ")
            ecriture.writerow({"first": first, "last": last, "house": ligne["house"]})
except (KeyError, ValueError, UnicodeDecodeError):
    sys.exit(f"ERROR: {sys.argv[1]} is not in a good format (csv)")
except FileNotFoundError:
    sys.exit(f"Could not find {sys.argv[1]}")
