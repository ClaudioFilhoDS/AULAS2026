Sistolica = 0
Diastolica = 0
Maior_sistolica = 0
Menor_Sistolica = 999
Maior_Diastolica = 0
Menor_Distolica = 999
Contador = 1
Loop1 = True

while Loop1:
    Pergunta = input(f"\nDigite a {Contador} pressão Sistolica (Digite qualquer letra para cancelar):  ")

    if Pergunta.isnumeric():
        if Maior_sistolica < int(Pergunta):
            Maior_sistolica = int(Pergunta)

        if Menor_Sistolica > int(Pergunta):
            Menor_Sistolica = int(Pergunta)
        
        Sistolica += int(Pergunta)

        Pergunta = input(f"\nDigite a {Contador} pressão Diastolica:  ")
        Loop2 = True
        while Loop2:
            if Pergunta.isnumeric():
                if Menor_Distolica > int(Pergunta):
                    Menor_Distolica = int(Pergunta)

                if Maior_Diastolica < int(Pergunta):
                    Maior_Diastolica = int(Pergunta)
                
                Loop2 = False
                Diastolica += int(Pergunta)
                Contador += 1

            else:
                 Pergunta = input(f"\nErro! Digite um numero e nao uma letra\nDigite a {Contador} pressão Diastolica:  ")

    else:
        Loop1 = False
        print("\nCancelando a contagem...")

Total_Medicoes = Contador - 1

if Total_Medicoes == 0:
    Media_Sistolica = 0
    Media_Diastolica = 0
else:
    Media_Sistolica = Sistolica / Total_Medicoes
    Media_Diastolica = Diastolica / Total_Medicoes

print(f"\na maior medição sistolica foi {Maior_sistolica} e a menor sistolica é {Menor_Sistolica}")
print(f"\na maior medição diastolica foi {Maior_Diastolica} e a menor diastolica é {Menor_Distolica}")
print(f"\na media das medições de sistolica e diastolica é: {int(Media_Sistolica)}/{int(Media_Diastolica)}")