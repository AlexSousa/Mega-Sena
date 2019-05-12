import random

lista = []
cont = 0
while True:
    num = random.randint(1, 60)
    if num not in lista:
        lista.append(num)
        cont += 1

    if cont >= 6:
        break

lista.sort()
print("Os numeros Sorteados Foram: ",lista)

