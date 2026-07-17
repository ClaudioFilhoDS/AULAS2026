principal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
par = []
impar = []


for elemento in principal:
    if ord(elemento) % 2 == 0:
        par.append(elemento)
    else:
        impar.insert(0, elemento)

print(f"par: {par}")
print(f"impar: {impar}")
        
 