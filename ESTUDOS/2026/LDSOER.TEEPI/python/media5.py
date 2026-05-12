nota = 0
contador = 0
finalizado = 0
nota_maior = 0 
nota_menor = 10

while contador < 5 and finalizado == 0:
    pergunta = input("digite uma nota ou [s] para sair: ")

    if pergunta.isnumeric() and float(pergunta) < 10.01:
        nota = nota + float(pergunta)

        if float(pergunta) > nota_maior:
            nota_maior = float(pergunta)

        elif float(pergunta) < nota_menor:
            nota_menor = float(pergunta)
                
        pergunta = ""
        contador += 1

    elif pergunta.lower() == 's':      
        finalizado += 1    

    else:
        print("valor incorreto, porfavor digite um numero")

else:
    if nota == 0:
       print("nenhuma nota foi informada") 

    else:
         print(f"a media das {contador} notas e {nota / contador}\n a nota maior e {nota_maior}\n e a nota menor e {nota_menor}")
         