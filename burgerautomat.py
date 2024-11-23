
print("Welcome to Burger Automat.")
bill = 0 

burger = input("Do you want a burger? (Y/N): ").upper()
if burger == "Y":
    size = input("Choose your size for Burger: S, M, XL: ").upper()
    if size == "S":
        bill += 5
    elif size == "M":
        bill += 10
    elif size == "XL":
        bill += 15
    else:
        print("Invalid burger size. Please choose S, M, or XL.")
        exit()  
else:
    bill += 0  


fries = input("Do you want fries? (Y/N): ").upper()
if fries == "Y":
    size = input("Choose your size for Fries: S, M, XL: ").upper()
    if size == "S":
        bill += 3
    elif size == "M":
        bill += 5
    elif size == "XL":
        bill += 7
    else:
        print("Invalid fries size. Please choose S, M, or XL.")
        exit()  

beverage = input("Do you want a beverage? (Y/N): ").upper()
if beverage == "Y":
    size = input("Choose your size for Beverage: S, M, XL: ").upper()
    if size == "S":
        bill += 2
    elif size == "M":
        bill += 3
    elif size == "XL":
        bill += 4
    else:
        print("Invalid beverage size. Please choose S, M, or XL.")
        exit()  


lime = input("Do you want lime for your beverage? (Y/N): ").upper()
if lime == "Y":
    bill += 1  
elif lime != "N":
    print("Invalid lime input. Please enter Y or N.")
    exit()  


cheese = input("Do you want cheese? (Y/N): ").upper()
if cheese == "Y":
    quantity = int(input("How many slices of cheese would you like? "))
    bill += quantity  
elif cheese != "N":
    print("Invalid cheese input. Please enter Y or N.")
    exit()  


onion = input("Do you want onion? (Y/N): ").upper()
if onion == "Y":
    pass 

tomato = input("Do you want tomato? (Y/N): ").upper()
if tomato == "Y":
    pass  

pickle = input("Do you want pickle? (Y/N): ").upper()
if pickle == "Y":
    pass  

print(f"Your total bill is: ${bill}")
