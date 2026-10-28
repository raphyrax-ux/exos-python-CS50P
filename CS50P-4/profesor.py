import random
def main():
    L = ["1", "2", "3"]
    n = input("Niveau : ")
    points = 0
    if not n in L:
        while True:
            n = input("Niveau : ")
            if n in L:
                break
    if n == "1":
        points = addition(0,9)
    elif n == "2":
        points = addition(10,99)
    else:
        points = addition(100,999)
    print(f"Score final : {points}/10")


def addition(min,max):
    liste = []
    score_final = 0
    for i in range(10):
        liste.append([random.randint(min,max), random.randint(min,max)])
    for nb1, nb2 in liste:
        score = jeu(nb1, nb2)
        score_final += score
    return score_final

def jeu(nb1, nb2):
    resultat = nb1 + nb2
    print(f"{nb1} + {nb2}")
    essai = test()
    nb_tentatives = 0
    score = 0
    while True:
        if essai == resultat:
            score += 1
            break
        elif essai != resultat:
            nb_tentatives += 1
            print("EEE")
            while nb_tentatives < 3:
                essai = test()
                if essai == resultat:
                    score += 1
                    break
                print("EEE")
                nb_tentatives += 1
            if nb_tentatives > 3:
                print(f"{nb1} + {nb2} = {resultat}")
        break
    return score

def test():
    while True:
        try:
            essai = int(input())
        except ValueError:
            continue
        else:
            break
    return essai

main()



