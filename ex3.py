media = []
acima = 0
abaixo = 0
I = 0

while I < 10:
    nota = float(input("Digite a nota do aluno: "))
    media.append(nota)
    I += 1
    if nota >= 6:
        acima += 1
    else:
        abaixo += 1

print(
    "A média do aluno é: ",
    (sum(media) / 10),
    "Notas a cima ou igual a 6: ",
    acima,
    "Notas abaixo de 6: ",
    abaixo,
)
