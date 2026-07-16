taxa_jovem = 0
desconto_experiente = 0
print("---Sistema de Cotação e Aprovação de Seguro Auto---\n")


idade = int(input("\nQual a Idade do condutor ? \nDigite: "))
acidentes = int(input("\nQuantos acidentes o condutor teve no ultimo ano w \nDigite: "))
if acidentes < 3 and idade > 17:
    fipe = float(input("\nqual o valor do veiculo ?\nDigite: "))
    cnh = int(input("\nquantos anos voce tem a sua CNH ?\nDigite: "))
    carro = int(input("\nUso do Veículo (1 - Passeio, 2 - Aplicativo/Trabalho) ?\nDigite: "))
    base_cotação = fipe * 0.05
    if idade < 25 and cnh < 3:
        taxa_jovem = base_cotação * 1.2
    
    elif idade < 25 and cnh >= 3:
        taxa_jovem = base_cotação * 1.1

    elif idade > 60:
        desconto_experiente = base_cotação * 0.15
    
    if carro == 2:
        taxa_de_uso = 800
    
    else:
        taxa_de_uso = 0

    print("\n---Calculo Final---\n")
    print(f"\nValor Base:R${base_cotação}\nTaxa Jovem:R${taxa_jovem}\nDesconto Experiente:R${desconto_experiente}\nTaxa de uso:R${taxa_de_uso}\nPreço final em 12xR${(desconto_experiente + taxa_de_uso +taxa_jovem + base_cotação) / 12 }")
    

    

else:
    print("\nreprovado por falta de experiencia\n")

    