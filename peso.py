print("\nDigite sua altura e o código dirá qual seria o seu peso ideal.")

def genero():
    g = input("\nQual é o seu gênero biológico? (m)Masculino (f)Feminino: ")
    h = float(input("Digite a sual altura: "))

    if g == "m":
        peso = (72.7 * h) - 58
        print(f"\nDe acordo com o seu gênero e altura, o seu peso ideal seria: {peso:.1f}")
        exit()
    elif g == "f":
        peso = (62.1 * h) - 44.7
        print(f"\nDe acordo com o seu gênero e altura, o seu peso ideal seria: {peso:.1f}")
        exit()
    else:
        print("\nPor favor, digite um gênero válido.")
        genero()

genero()
