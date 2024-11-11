print("\nOlá, este programa irá receber 10 valores e informar a média desses valores.")

contador = 1
n = 11
soma = 0

while contador < n:
    valor = float(input(f"\nDigite o {contador}º número: "))
    soma += valor
    contador += 1

media = soma / 10
print(f"\nA média dos números é: {media}")
