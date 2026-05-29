regiao = 0
produtor = 0
votos_regiao1 = 0
votos_regiao2 = 0
votos_regiao3 = 0

while regiao < 3:
    produtor = 0
    while produtor < 5:
        print(f"regiao: {regiao} produtor: {produtor}")
        

        voto = int(input("Digite 1 para sim e 0 para não: "))

        if voto == 1 or voto == 0:
            if regiao == 0:
              votos_regiao1 += voto
        elif regiao == 1:
             votos_regiao2 += voto
        elif regiao == 2:
             votos_regiao3 += voto
        produtor += 1


    
        

    regiao += 1

print(f"Votos região 1: {votos_regiao1}\nVotos região 2: {votos_regiao2}\nVotos região 3: {votos_regiao3}")
if votos_regiao1 > votos_regiao2 and votos_regiao1 > votos_regiao3:
    print("Região 1 é a mais produtiva")
elif votos_regiao2 > votos_regiao1 and votos_regiao2 > votos_regiao3:
    print("Região 2 é a mais produtiva")
elif votos_regiao3 > votos_regiao1 and votos_regiao3 > votos_regiao2:
    print("Região 3 é a mais produtiva")
else:
    print("Houve um empate entre as regiões")