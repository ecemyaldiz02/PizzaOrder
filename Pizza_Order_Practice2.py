print("Welcome to Pizza Station")
size = input("What size pizza do you want? S,M or L")
extra = input("Would you like extra toppings on your pizza? Y/N")
extra_souce = input("Would you like extra souce on your pizza? Y/N")
extra_drink = input("Would you like extra drink on your pizza? Y/N")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Wrong inputs !!")
if extra == "Y":
    if size == "S":
        bill += 4
    else:
        bill += 7
if extra_souce == "Y":
    bill += 2
if extra_drink == "Y":
    bill += 4
print(f"Your final bill is : {bill} $")
