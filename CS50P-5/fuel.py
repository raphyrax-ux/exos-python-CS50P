def main():
    while True:
        try:
            pourcentage = convert(input("Fraction: "))
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(gauge(pourcentage))


def convert(fraction):
    x, y = fraction.split("/")   # ValueError si le format n'est pas X/Y
    x = int(x)                   # ValueError si ce n'est pas un entier
    y = int(y)

    if y == 0:
        raise ZeroDivisionError
    if x < 0 or y < 0 or x > y:
        raise ValueError

    return round(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    return f"{percentage}%"


if __name__ == "__main__":
    main()