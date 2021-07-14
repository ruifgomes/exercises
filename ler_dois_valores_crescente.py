from random import randint

print("1- Inseriar automaticamente numeros")
print("2- Inseriar manualmente numeros")
opcao_escolhida = int(input("Escolha uma opção: "))

if opcao_escolhida == 1:
    numero_aleatorio_1 = randint(0, 100)
    print(numero_aleatorio_1)

    numero_aleatorio_2 = randint(0, 100)
    print(numero_aleatorio_2)

    primeiro_numero = numero_aleatorio_1
    segundo_numero = numero_aleatorio_2
    
    if primeiro_numero < segundo_numero:
        print( primeiro_numero, segundo_numero )
    elif primeiro_numero > segundo_numero:
        print( segundo_numero, primeiro_numero )
        
elif opcao_escolhida == 2: 
    primeiro_numero = input("Insira o primeiro numero: ")
    segundo_numero = input("Insira o segundo numero: ")
    print("")
    
    if primeiro_numero < segundo_numero:
        print( primeiro_numero, segundo_numero )
    elif primeiro_numero > segundo_numero:
        print( segundo_numero, primeiro_numero )

else:
    print("Está alguma merda mal Rui")  