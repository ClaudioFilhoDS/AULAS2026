regiao = 1
reg1 = 0
reg2 = 0
reg3 = 0
while regiao < 4:
    pergunta = 1
    while pergunta <     6:
        voto = int(input(f"Digite 1 para sim ou 0 para nao. A regiao e a {regiao} e voto e o {pergunta}      "))
        if voto == 0 or voto == 1:
            
            if regiao == 1:
                reg1 += voto
                pergunta += 1
        
            elif regiao == 2:
                reg2 += voto
                pergunta += 1

            elif regiao == 3:
                reg3 += voto
                pergunta += 1

    regiao += 1

print(f"total de votos sim e {reg1 + reg2 + reg3} e os de votos nao {15 - (reg1 + reg2 + reg3)}")
if reg1 > reg2 and reg1 > reg3:
    print(f"A regiao com mais votos e a 1 com  {reg1} votos")
elif reg2 > reg1 and reg2 > reg3:
    print(f"A regiao com mais votos e a 2 com  {reg2} votos")
elif reg3 > reg1 and reg3 > reg2:
    print(f"A regiao com mais votos e a 3 com  {reg3} votos")

        


