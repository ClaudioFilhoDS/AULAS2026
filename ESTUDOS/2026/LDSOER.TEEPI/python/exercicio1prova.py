loop = True
contador = 0
valor_total = 0
critica = 0
while loop:
    pergunta = 0
    contador += 1
    pergunta = float(input(f"qual a {contador} temperatura?"))
    if pergunta < 0:
        print("acabou a contagem")
        loop = False


    elif pergunta >= 100:
        critica += 1
        valor_total += pergunta 
    else: 
        valor_total += pergunta 

print(f"a quantidade total de temperatura foi de {contador}")
print(f"a media das temperaturas e de {valor_total / contador}")
print(f"foram registradas {critica} temperaturas criticas")        
    