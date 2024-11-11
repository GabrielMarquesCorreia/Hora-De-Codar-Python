print("\nOlá! Este código exibirá o maior dos três números que você inserir!")

n1 = float(input("\nDigite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print(f"\nO maior número é: {n1}")
elif n2 > n3 and n2 > n1:
    print(f"\nO maior número é: {n2}")
else: 
    print(f"\nO maior número é: {n3}")
