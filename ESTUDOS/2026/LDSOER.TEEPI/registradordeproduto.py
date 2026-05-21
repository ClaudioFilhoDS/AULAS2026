print("\n---Registrador de produtos---")
continuar_compra = True
valor_total = 0
itens = 0
while continuar_compra:
    valor_iten = float(input("\nQual o Valor do produto que voce deseja(digite 0 para encerrar)\nDigite: "))
    valor_total +=  valor_iten
    if valor_iten == 0:
        continuar_compra = False
        
    else:
        categoria = int(input("\nCategoria (1 - Informática, 2 - Games, 3 - Acessórios)\nDigite: "))
        if categoria == 1 and valor_iten < 2000:
            desconto = valor_iten* 0.05


        elif categoria == 3 and valor_iten < 100:
            desconto = valor_iten * 0.1
        
        elif categoria > 3:
            print("\nCategoria invalida! Item ignorado")
            continue
if valor_total == 0:
    print("Carrinho vazio")
else:
    pagamento = int(input("\nPagamento (1 - PIX, 2 - Cartão de Crédito)\n"))
    if pagamento == 1:
        desconto = valor_total * 0.1
        print(f"\nValor Total = R${valor_total:.2f}\nValor Final = R${valor_total - desconto}")

    elif pagamento == 2 and valor_total < 500:
        cartao = ((valor_total - desconto) * 1.05) / 10
        print(f"\nValor Total = R${valor_total:.2f}\nValor Final = R${valor_total - desconto}\nCartão 10x:R${cartao}")

        
    else:
        cartao = (valor_total - desconto) / 10
        print(f"\nValor Total = R${valor_total:.2f}\nValor Final = R${valor_total - desconto}\nCartão 10x:R${cartao}")

        

