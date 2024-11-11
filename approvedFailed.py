print("\nOlá! Este código determinará se você é um aluno aprovado ou reprovado.")

materias = ["matérias", "inglês", "matemática", "computação"]
contador = 1

while contador < len(materias):
    provas = 3
    nota = 1
    soma = 0

    while nota < provas:
        valor = float(input(f"\nPor favor, insira sua {nota}ª nota em {materias[contador]}: "))
        soma += valor
        nota += 1

    media = soma / 2

    print(f"\nSua média na matéria {materias[contador-1]} é: {media}")

    if media >= 6:
        print(f"\nParabéns! Você foi aprovado na matéria {materias[contador]}!")
    else:
        print(f"\nDesculpe, você foi reprovado na matéria {materias[contador-1]}!")

    contador += 1
