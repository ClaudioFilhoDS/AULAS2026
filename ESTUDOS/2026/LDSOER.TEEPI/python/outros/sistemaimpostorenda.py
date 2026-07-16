print("informe o salario de cada mes começando de janeiro ate dezembro")
mes = 1 
salario_total = 0
imposto_pago = 0
while mes <= 12:
    salario_total = float(input(f"informe o salario que voce recebeu no mes {mes}\ndigite: "))
    imposto_pago = float(input(f"informe o imposto que voce pagou no mes {mes}\ndigite: "))
    mes += 1


