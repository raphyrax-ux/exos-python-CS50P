def main():
    taqueira = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    commande = {}
    while True:
        try:
            plat = input("Entrez un plat : ").title()
            print(f"Total : {taqueira[plat]:.2f}$")
        except KeyError:
            plat = input("Entrez un plat : ").title()
        except EOFError:
            cout_total(commande)
            break
        else:
            commande[plat] = taqueira[plat]


def cout_total(d):
    total = 0
    for prix in d.values():
        total += prix
    print(f"Total : {total:.2f}$")
    


main()
