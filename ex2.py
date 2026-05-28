media = []
I = 0

while I < 10:
    nota = float(input("Digite a nota do aluno: "))
    media.append(nota)
    I += 1

print(sum(media)/10)
