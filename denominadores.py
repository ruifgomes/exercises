select_number = int(input("Insert a positive number: "))
select_number_2 = int(input("Insert a second number: " ))

denominador = 0

if select_number <= 0 or select_number_2 <= 0:
    print("Numero invalido, tem que ser positivo")

elif select_number < select_number_2:
     variavel = select_number
        
elif select_number_2 < select_number:
    variavel = select_number_2

for i in range(1, variavel+1):
    if select_number%i == 0 and select_number_2%i == 0:
        resultado = denominador + i

print(str(resultado) + " é denominador")
