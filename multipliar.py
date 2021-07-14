repetition = int(input("Insert the number os numberes do you want to sum: "))
result = 0

for i in range(0, repetition):
    num = int(input("Insert a positive number: "))
    result = result + num 
print("The sum is number: " + str(result))