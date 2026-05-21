#desafio antes da prova do olsen
print("\n---Programa para ajudar treinador de basquetes---\n")
Pessoas = int(input("Quantas pessoas seram analisadas?\nDigite: "))
loop1 = True
contador = 0
maior_altura = -999
menor_altura = 999
maisde19 = 0 
alturas = 0
while loop1:
    if  Pessoas == contador:
        loop1 = False
        
    else:
        altura = float(input("\nInforme a altura"))
        if altura < 0.5 and altura > 2.5:
            print("ERRO, Altura invalida!\nDigite uma altura novamente que seja correta")
        
        else:
                
            if maior_altura < altura:
                maior_altura = altura
                
            elif menor_altura > altura:
                menor_altura = altura
            if altura > 1.9:
                maisde19 += 1 
            
            alturas += altura
            contador += 1
if contador == 0:
    print("\nnenhum valor informado")
else:
    print(f"\nMaior altura = {maior_altura}\nMenor altura = {menor_altura}\nMedia das {Pessoas} alturas = {alturas / Pessoas}\nCandidatos com mais de 1.9m = {maisde19}")