print("\nEscreva 10 núemros e o código irá mostrar a soma destes núemros.")

num = 11
count = 1
soma = 0

while count < num:
    valor = float(input(f"\nEscreva o {count}° número: "))
    soma += valor
    count += 1

    r = soma

print(f"\nA soma dos números é igual a: {r}")