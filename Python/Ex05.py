valor = int(input("Digite o valor da prestação: "))
taxa = int(input("Digite a taxa de juros da prestação: "))
tempo = int(input("Digite o numero de dias atrasados: "))

prestação = valor + (valor * (taxa/100)* tempo)

print("O valor da prestação em atraso é de:",prestação)