print("Neste código, você informará alguns números sobre os time Palmeiras e Corinthians,\ne então o código dirá qual time é maior e melhor.")

corV = int(input("\nQuantas vitórias o Corinthians tem no Derby paulista?: "))
palV = int(input("Quantas vitórias o Palmeiras tem no Derby paulista?: "))
corT = int(input("\nQuantos títlos o Corinthians tem na sua história?: "))
palT = int(input("Quantos títlos o Palmeiras tem na sua história?: "))

maior = ""
melhor = ""

if corV > palV:
    melhor = "Corinthians"
elif corV < palV:
    melhor = "Palmeiras"

if corT > palT:
    maior = "Corinthians"
elif corT < palT:
    maior = "Palmeiras"

if melhor and maior:
    if melhor == maior:
        print(f"\nO {melhor} é o melhor e o maior time! Com um total de {corV if melhor == 'Corinthians' else palV} vitórias e {corT if maior == 'Corinthians' else palT} títulos.")
    else:
        print(f"\nO {maior} é o maior time com {corT if maior == 'Corinthians' else palT} títulos, e o {melhor} é o melhor time com {corV if melhor == 'Corinthians' else palV} vitórias.")
elif corV == palV and corT == palT:
    print(f"\nOs dois times são iguais! Com um total de {corV} vitórias e {corT} títulos.")
elif corV == palV:
    print(f"\nOs dois times estão empatados em vitórias! Mas o {maior} é o maior time com {corT if maior == 'Corinthians' else palT} títulos.")
elif corT == palT:
    print(f"\nOs dois times estão empatados em títulos! Mas o {melhor} é o melhor time com {corV if melhor == 'Corinthians' else palV} vitórias.")
    