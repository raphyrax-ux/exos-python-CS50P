import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    name = sys.argv[1].split(".")

try:
    with open(sys.argv[1]) as fichier:
        d = csv.DictReader(fichier)
        print(tabulate(d, headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File not found")

