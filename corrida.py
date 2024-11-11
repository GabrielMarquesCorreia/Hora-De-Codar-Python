print("A equipe Mercedes deseja calcular o número mínimo de litros que deverá colocar no tanque de seu carro\npara que ele possa percorrer um determinado número de voltas até o primeiro reabastecimento.")

pista = float(input("\nEscreva o tamanho da pista: "))
voltas = float(input("\nEscreva qauntas votas o piloto tem que fazer para ser campeão: "))
tanque = float(input("\nEscreva quantas vezes o piloto e a equipe pretendem reabastesser\no tanque durante a corrida: "))
gasosa = float(input("\nEscreva quantos litros de gasolina o carro gastou: "))

totalKm = (pista * voltas) * 1000
lMinimo = (totalKm / tanque) * gasosa
lTotal = totalKm * gasosa

print(f"\nO tamanho total deste circuito em Km é de {totalKm}Km.")
print(f"Caso o carro abasteça o tanque a cada volta, o carro gastará no\nmínimo {lMinimo} litros de gasolina por volta.")
print(f"O total de litros que o carro necessitará para completar o circuito é de {lTotal} litros.")
