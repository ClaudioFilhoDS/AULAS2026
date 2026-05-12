categoria = input("Qual a categoria do carro? (Sport, SUV Luxury e Eletric)\n").lower()
renda = float(input("Qual a renda mensal do condutor em R$)?\n"))
idade = int(input("Qual a idade do condutor? (em anos)\n"))
tempo = int(input("Qual o tempo de CNH do condutor? (em anos)\n"))
pontuacao = int(input("Quantos pontos o condutor tem atualmente?\n"))
valor_carro = float(input("Qual o valor do carro?\n"))

aprovado = True

if categoria == "sport":
    if idade < 25 or tempo < 5:
        print("Assinatura Negada: Experiência insuficiente para a categoria selecionada.")
        aprovado = False
        exit()
elif categoria == "suv luxury" or categoria == "eletric":
    if idade < 21 or tempo < 2:
        print("Assinatura Negada: Experiência insuficiente para a categoria selecionada.")
        aprovado = False
        exit()
else:
    print("Categoria não existente no catálogo")
    aprovado = False
    exit()

if categoria == "eletric":
    if pontuacao > 10:
        print("Assinatura Negada: Pontuação na CNH excede o limite de segurança")
        aprovado = False
        exit()
elif categoria == "suv luxury" or categoria == "sport":
    if pontuacao > 20:
        print("Assinatura Negada: Pontuação na CNH excede o limite de segurança")
        aprovado = False
        exit()

if renda <= 5000:
    limite = 80000
elif renda <= 10000:
    limite = 150000
elif renda > 10000:
    limite = 300000

if valor_carro > limite:
    print("Assinatura Negada: Valor do veículo incompatível com a renda mensal.")
    aprovado = False
    exit()

mensalidade = valor_carro * 0.015

if mensalidade > 0.3 * renda:
    print("Assinatura Negada: Mensalidade excede o limite de 30% da renda.")
    aprovado = False
    exit()

if aprovado:
    print(f"CONTRATO LIBERADO! Categoria: {categoria}. Carro: R$ {valor_carro}. Mensalidade: R$ {mensalidade}. Aproveite seu veículo!")