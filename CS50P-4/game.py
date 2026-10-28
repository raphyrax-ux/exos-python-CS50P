import random
number = int(input("Level : "))
while number <= 0:
    number = int(input("Level : "))

nb_mystere = random.randint(0, number)
chercher = int(input("Guess : "))
while chercher != nb_mystere:
    if chercher < nb_mystere:
        print("Too small !")
    elif chercher > nb_mystere:
        print("Too large !")
    chercher = int(input("Guess : "))
print("Just right !")