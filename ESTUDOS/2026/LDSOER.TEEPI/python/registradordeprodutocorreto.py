print("\n--- Registrador de produtos ---")
continuar_compra = True
valor_total = 0

while continuar_compra:
    valor_item = float(input("\nQual o Valor do produto? (digite 0 para encerrar): R$ "))
    
    if valor_item == 0:
        continuar_compra = False
    else:
        categoria = int(input("Categoria (1 - Informática, 2 - Games, 3 - Acessórios): "))
        
        # 1. Filtramos o erro primeiro (sem precisar de continue)
        if categoria < 1 or categoria > 3:
            print("\nCategoria inválida! Item ignorado.")
            
        else:
            # 2. Calculamos o desconto do ITEM (Note o sinal de MAIOR >)
            if categoria == 1 and valor_item > 2000:
                desconto_item = valor_item * 0.05
                valor_item = valor_item - desconto_item # Aplica o desconto no item
                print(f"Desconto de 5% aplicado no item!")

            elif categoria == 3 and valor_item > 100:
                desconto_item = valor_item * 0.10
                valor_item = valor_item - desconto_item # Aplica o desconto no item
                print(f"Desconto de 10% aplicado no item!")
            
            # 3. AGORA SIM nós somamos no carrinho (já com desconto, se tiver)
            valor_total += valor_item


# --- FECHAMENTO DO CAIXA ---
if valor_total == 0:
    print("\nCarrinho vazio.")
else:
    print(f"\nSubtotal da compra: R$ {valor_total:.2f}")
    pagamento = int(input("Pagamento (1 - PIX, 2 - Cartão de Crédito): "))
    
    if pagamento == 1:
        # Desconto do PIX
        desconto_pix = valor_total * 0.10
        valor_final = valor_total - desconto_pix
        print(f"\nValor Total = R$ {valor_total:.2f}")
        print(f"Valor Final com PIX = R$ {valor_final:.2f}")

    elif pagamento == 2:
        if valor_total < 500:
            # Juros de 5%
            juros = valor_total * 0.05
            valor_final = valor_total + juros
            print(f"\nValor Total = R$ {valor_total:.2f}")
            print(f"Valor Final com Juros (Cartão) = R$ {valor_final:.2f}")
        else:
            # Parcelado em 10x sem juros
            valor_final = valor_total
            cartao = valor_final / 10
            print(f"\nValor Total = R$ {valor_total:.2f}")
            print(f"Valor Final = R$ {valor_final:.2f}")
            print(f"Cartão 10x de: R$ {cartao:.2f}")