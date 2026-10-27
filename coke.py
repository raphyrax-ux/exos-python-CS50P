price = [5,10,25]
amount = 0
while amount < 50:
    coin = int(input("Insert a coin : "))
    if coin in price :
        amount += coin
        print(f"Amount Due : {amount}")
    else:
        print("Please enter a valid coin")
print(f"Change Owed : {amount - 50}")