print("Neste código, você informará 3 números, o código então dirá\nqual o maior, o menor, e a soma entres os números.")

num = 4
count = 1
sum = 0
maior = None
menor = None

while count < num:

    valor = float(input(f"\nEscreva o {count}° número: "))
    sum += valor

    if maior is None or valor > maior:
        maior = valor
    if menor is None or valor < menor:
        menor = valor

    count += 1

print(f"\nO maior número informado foi {maior}.")
print(f"O menor número informado foi {menor}.")
print(f"A soma entre os núemros é igual a: {sum}.")
