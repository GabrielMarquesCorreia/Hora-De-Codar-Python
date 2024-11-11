print("\nPROMOÇÃO NA LOJA REMI du FROMAGE! CADA PC GAMER POR APENAS R$3600.\nO GERENTE FICOU MALUCO! PODE PARCELAR EM ATÉ 15 VEZES SEM JUROS!")

def parcelas():
    count = 1
    p = int(input("\nInforme por quantas vezes você gostaria de parcelar o produto: "))

    if p > 0 and p <= 15:
        while count < p:
            valor = 3600
            r = valor / p
            count += 1
    else:
        print("\nPor favor, informe uma quantidade de parcelas válidas.")
        parcelas()

    print(f"\nVocê decidiu parcelar o produto em {p} vezes, logo você pagará R${r:.2f} por mês.")
    exit()

parcelas()
