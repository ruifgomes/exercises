    
for i in range (7):
    from random import randint
    random = randint(0, 10)
    for j in range(i):
        print(random, end = "")
    print()