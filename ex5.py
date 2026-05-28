i = 0
soma = []

while i < 100:
    numero = int(input("Digite um número: "))
    soma.append(numero)
    i += 1

i = 0
encontrou = False

while i < 100:
    if soma[i] == 30:
        print("Tem 30 na posição:", i)
        encontrou = True
    i += 1

if not encontrou:
    print("Não tem 30 na lista")