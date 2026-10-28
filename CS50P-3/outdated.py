def main():
    mois = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    d = 0
    y = 0
    try:
        date_input = input()
        m, d, y = date_input.split("/")
    except ValueError:
        date, y = date_input.split(", ")
        m, d = date.split(" ")
        while True:
            try:
                int(d)
            except ValueError:
                date, y = input().split(", ")
                m, d = date.split(" ")
            else:
                break
        for i in range(len(mois)):
            if m == mois[i]:
                m = i+1
        formatage(y,m,d)
        
    else:
        formatage(y,m,d)
        
def formatage(y,m,d):
    if int(m) > 9 and int(d) < 10:
        print(f"{y}-{m}-0{d}")
    elif int(d) > 9 and int(m) < 10:
        print(f"{y}-0{m}-{d}")
    elif int(d) > 9 and int(m) > 9:
        print(f"{y}-{m}-{d}")
    else:
        print(f"{y}-0{m}-0{d}")

main()