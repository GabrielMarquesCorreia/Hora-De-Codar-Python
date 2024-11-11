print("\nOlá! Digite um número e o programa irá mostrar se o número é maior, menor ou igual a 0.")

n = float(input("\nDigite o número: "))

if n > 0:
    print(f"\nO número {n} é maior que 0!")
elif n < 0:
    print(f"\nO número {n} é menor que 0!")
else:
    print(f"\nO número {n} é igual a 0!")
