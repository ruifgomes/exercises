from random import randint
numero_aleatorio = randint(0, 100)
print(numero_aleatorio )

from random import randint
numero_aleatorio1 = randint(0, 100)
print(numero_aleatorio1)

primeiro_numero = numero_aleatorio
segundo_numero = numero_aleatorio1

if primeiro_numero < segundo_numero:
    print(segundo_numero)
else:
    print(primeiro_numero)