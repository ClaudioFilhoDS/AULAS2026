idade = ""
vezes = 0
while not(idade.isnumeric()) and vezes < 3:
    vezes += 1
    idade = input("qual a sua idade ? \ndigite: ")
    
else:
    if idade.isnumeric():
        print(f"sua idade e {idade} anos, e foram pergutado {vezes} vezes")

    else:
        print("tentativas excedidas ")

