print("\nEscreva a sua idade e o código dirá se você tem o não tem idade suficiente para votar.")

idade = int(input("\nEscreva o seu ano de nascimento: "))
conta = 2024 - idade

if conta >= 18:
    print(f"\nVocê nasceu no ano de {idade}, ou seja, você atualmente tem {conta} anos.\nVocê já tem idade suficiente para votar!")
elif conta >= 16:
    print(f"\nVocê nasceu no ano de {idade}, ou seja, você atualmente tem {conta} anos.\nVocê já tem idade suficiente para votar caso tenha permissão dos pais!")
else:
    print(f"\nVocê nasceu no ano de {idade}, ou seja, você atualmente tem {conta} anos.\nVocê ainda não tem idade suficiente para votar!")
