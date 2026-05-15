soma_bruto = 0
soma_deducoes = 0
soma_IPRF = 0
IPRF_devido = 0
Iprf = 0

print(" Calculadora de Ajuste Anual de IR e INSS ")

mes = 1
while mes <= 12:
    print(f"\nMês {mes}:")
    bruto = float(input("Digite o Recebido Bruto: R$ "))
    deducoes = float(input("Digite o valor de Deduções/Isentos: R$ "))
    Iprf = float(input("Digite o valor do Iprf (Imposto Retido na Fonte): R$ "))
    
    soma_bruto += bruto
    soma_deducoes += deducoes
    soma_IPRF += Iprf
    
    mes += 1

inss_anual = 0

if soma_bruto <= 18216.00:
    inss_anual = soma_bruto * 0.075

elif soma_bruto <= 33600.00:
    inss_anual = (18216.00 * 0.075) + ((soma_bruto - 18216.00) * 0.09)

elif soma_bruto <= 48000.00:
    inss_anual = (18216.00 * 0.075) + ((33600.00 - 18216.00) * 0.09) + ((soma_bruto - 33600.00) * 0.12)

else:
    inss_anual = (18216.00 * 0.075) + ((33600.00 - 18216.00) * 0.09) + ((48000.00 - 33600.00) * 0.12) + ((soma_bruto - 48000.00) * 0.14)

base_calculo = soma_bruto - inss_anual - soma_deducoes

if base_calculo < 0:
    base_calculo = 0

if base_calculo <= 27110.40:
    IPRF_devido = 0
elif base_calculo <= 33919.80:
    IPRF_devido = (base_calculo * 0.075) - 2033.28
elif base_calculo <= 45012.60:
    IPRF_devido = (base_calculo * 0.15) - 4577.28
elif base_calculo <= 55976.16:
    IPRF_devido = (base_calculo * 0.225) - 7953.24
else:
    IPRF_devido = (base_calculo * 0.275) - 10752.00

saldo_final = IPRF_devido - soma_IPRF

print("\n" + "="*45)
print("             RESUMO DO ANO")
print("="*45)
print(f"Renda Bruta Acumulada:   R$ {soma_bruto:.2f}")
print(f"Total de Deduções:       R$ {soma_deducoes:.2f}")
print(f"INSS Total Descontado:   R$ {inss_anual:.2f}")
print(f"Base de Cálculo do IRPF: R$ {base_calculo:.2f}")
print(f"Imposto de Renda Devido: R$ {IPRF_devido:.2f}")
print(f"IPRF Total Já Pago:      R$ {soma_IPRF:.2f}")
print("-" * 45)


if saldo_final > 0:
    print(f"Situação: IMPOSTO A PAGAR")
    print(f"Valor: R$ {saldo_final:.2f}")
elif saldo_final < 0:
    print(f"Situação: RESTITUIÇÃO A RECEBER")
    print(f"Valor: R$ {saldo_final * -1:.2f}")
else:
    print("Situação: IMPOSTO QUITADO (Não há saldo a pagar ou restituir)")
print("="*45)