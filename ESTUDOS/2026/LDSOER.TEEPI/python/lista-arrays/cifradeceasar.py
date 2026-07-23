def cifra_de_ceasar():
    texto = input("Qual o texto para ser cifrado? ")
    chave = int(input("Qual a chave para chifrar? "))

    chave_real = chave % 26

    texto_criptografado = ""

    for char in texto:
        if char.isalpha():

            if char.isupper():
                base_ascii = ord('A') 
            else:
                base_ascii = ord('a') 

            posicao_alfabeto = ord(char) - base_ascii
            nova_posicao = (posicao_alfabeto + chave_real) % 26
            novo_char = chr(nova_posicao + base_ascii)
            
            texto_criptografado += novo_char
            
        else:
            texto_criptografado += char

    print(f"\nTexto criptografado: {texto_criptografado}")

cifra_de_ceasar()