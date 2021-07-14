pin = 3456
result = 0

for i in range (4):
    gess = int(input("Please make your guess: "))
    if gess == pin:
        print("That was corrett!")
        print()
        break
    elif gess != pin:
        print("Sorry that was wrong.")
        print()
        result = result + 1
if result == 4:
    print("You reached the limit of tries! ")