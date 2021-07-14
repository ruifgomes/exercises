from random import randint

player_number = int(input("Tipe a number beetwen 1 and 10: "))
machine_number = randint(1, 10)
print(machine_number)

if player_number == machine_number:
    print("\ Congrats, you won :D /")
else:
    print("/ I'm sorry, but you lost \ ")