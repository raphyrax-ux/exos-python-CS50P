def main():
    grocery = {}
    while True:
        try:
            item = input()
            grocery[item] += 1
        except KeyError:
            grocery[item] = 1
        except EOFError:
            afficher(grocery)
            break

def afficher(grocery):
    for item in grocery:
        print(f"{grocery[item]} {item.upper()}")


main()