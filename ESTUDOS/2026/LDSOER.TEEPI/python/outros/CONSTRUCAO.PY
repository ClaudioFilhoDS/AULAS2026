tipo = input("Qual o tipo do projeto? (QUADRADO / RETANGULO / CIRCULO)\n").lower()
if tipo == "quadrado":
    lado = float(input("Qual o lado do quadrado em metros?\n"))
    area = lado * lado
elif tipo == "retangulo":
    comprimento = float(input("Qual o comprimento do retangulo em metros?\n"))
    largura = float(input("Qual a largura do retangulo em metros?\n"))
    area = comprimento * largura
elif tipo == "circulo":
    raio = float(input("Qual o raio do circulo em metros?\n"))
    area = 3.14 * (raio * raio)
else:
    print("Forma geometrica não encontrada. Projeto negado!")
    exit()

orcamento_total = float(input("Qual o orçamento total para a contrução? (em reais)\n"))
material = input("Qual o tipo de material que vai ser usado na contrução? (BASICO / PREMIUM)\n").lower()

if material == "basico":
    if area < 50:
        valor_metro = 150
    elif area >= 50:
        valor_metro = 120

if material == "premium":
    if area < 50:
        valor_metro = 250
    elif area >= 50:
        valor_metro = 200

custo_base = area * valor_metro

if tipo == "circulo":
    custo_base = custo_base + custo_base * 0.15

if custo_base <= orcamento_total:
    print(f"Área total: {area} metros quadrados")
    print(f"Custo final da obra: {custo_base} REAIS")
    print("PROJETO APROVADO!")
    exit()
elif custo_base > orcamento_total:
    if custo_base % orcamento_total < 0.15 * orcamento_total:
        print("Projeto em Análise: Necessário pequeno ajuste de verba.")
        exit()
elif custo_base % orcamento_total > 0.15 * orcamento_total:
    print("PROJETO REPROVADO. Orçamento insuficiente")
    exit()