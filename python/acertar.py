import random
valor = random.randint(1, 100)
miNumero = int(input('dame un numero entre 1 y 100 '))
while miNumero != valor:
    if miNumero > valor:
        print("mi numero es mayor")
    else:
        print("mi numero es menor")
    miNumero = int(input('dame un numero entre 1 y 100 '))
print("acertaste")
