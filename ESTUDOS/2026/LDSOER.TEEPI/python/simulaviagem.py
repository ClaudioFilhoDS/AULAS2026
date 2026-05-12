destino_op = input("Escolha o destino (1 - Nova York, 2 - Paris, 3 - Tóquio): ")
passaporte = input("Possui passaporte válido? (s/n): ").lower()
orcamento = float(input("Qual o seu orçamento disponível (R$)? "))
idade = int(input("Qual a sua idade? "))
duracao_desejada = int(input("Quantos dias pretende ficar? "))
nota_idioma = int(input("Nota de fluência no idioma (0 a 10): "))

destinos = {
    '1': {"nome": "Nova York", "custo_fixo": 10000.0, "idade_min": 16},
    '2': {"nome": "Paris", "custo_fixo": 12000.0, "idade_min": 16},
    '3': {"nome": "Tóquio", "custo_fixo": 15000.0, "idade_min": 18}
}


if destino_op not in destinos:
    exit("VIAGEM CANCELADA. Motivo: Destino inválido.")

dados_destino = destinos[destino_op]
nome_destino = dados_destino["nome"]


if passaporte != 's':
    exit("VIAGEM CANCELADA. Motivo: [Passaporte Inválido].")

if idade < dados_destino["idade_min"]:
    exit(f"VIAGEM CANCELADA. Motivo: [Idade mínima para {nome_destino} não atingida].")


custo_fixo = dados_destino["custo_fixo"]
if orcamento < custo_fixo:
    exit(f"Viagem Negada: Orçamento de R$ {orcamento:.2f} é insuficiente para o custo fixo de {nome_destino} (R$ {custo_fixo:.2f}).")


if nota_idioma >= 8:
    duracao_maxima = 90
elif 5 <= nota_idioma <= 7:
    duracao_maxima = 30
else:
    duracao_maxima = 15

if duracao_desejada > duracao_maxima:
    exit(f"Viagem Negada: Sua fluência (Nota {nota_idioma}) permite apenas {duracao_maxima} dias, mas você solicitou {duracao_desejada} dias.")


saldo_restante = orcamento - custo_fixo
valor_por_dia = saldo_restante / duracao_desejada

if valor_por_dia < 500:
    exit(f"Viagem Negada: Saldo restante (R$ {saldo_restante:.2f}) insuficiente para manter o custo de R$ 500/dia durante {duracao_desejada} dias. (Disponível: R$ {valor_por_dia:.2f}/dia)")


print("-" * 30)
print(f"VIAGEM APROVADA!")
print(f"Destino: {nome_destino}.")
print(f"Duração: {duracao_desejada} dias.")
print(f"Saldo para gastos diários: R$ {valor_por_dia:.2f} por dia.")
print("-" * 30)