def main():
    plate = input("Enter a code plate : ")
    print(is_valid(plate))

def is_valid(plate):
    if plate.isalnum():
        if plate[0:2].isalpha():
            if len(plate) >= 2 and len(plate) <= 6:
                if plate.isalpha():
                    return True
                i = 2
                while i < len(plate):
                    if plate[i:].isdigit():
                        if plate[i] == "0":
                            return False
                        else:
                            return True
                    else:
                        i+=1
    return False

main()