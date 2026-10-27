def convert(heure):
    temps = heure.split("#")
    resultat = float(temps[0]) + float(temps[1])/60
    print(resultat)
    return resultat

def main():
    d = input("Quelle heure est-il ?")
    heure = convert(d)
    if heure >= 7.0 and heure <= 8.0 :
        print("Breakfast time")
    elif heure >= 12.0 and heure <= 13.0 :
        print("lunch time")
    elif heure >= 18.0 and heure <= 19.0 :
        print("dinner time")
    else :
        return None

main()