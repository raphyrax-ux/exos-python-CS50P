def main():
    x, y = entrer()
    resultat = division(x,y)
    if resultat <= 1:
        print("E")
    elif resultat >= 99:
        print("F")
    else:
        print(f"{resultat}%")

def division(X,Y):
    while True:
        try:
            x = int(X)
            y = int(Y)
        except ValueError:
            X, Y = entrer()
        if x <= y and x > 0 and y > 0:
            try:
                division = x/y
            except ZeroDivisionError:
                X, Y = entrer()
            else:
                resultat = round(division * 100)
                return resultat
        else:
            X, Y = entrer()

def entrer():
    fuel = input("Fraction : ")
    x, y = fuel.split("/")
    return x, y

main()