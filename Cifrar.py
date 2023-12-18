def cifrar_texto(texto, desplazamiento):
    texto_cifrado = ""

    for caracter in texto:
        if caracter.isalpha():
            if caracter.islower():
                codigo = ord('a')
            else:
                codigo = ord('A')

            codigo_cifrado = (ord(caracter) - codigo + desplazamiento) % 26 + codigo
            texto_cifrado += chr(codigo_cifrado)
        else:
            texto_cifrado += caracter

    return texto_cifrado

# Pedir al usuario que ingrese el texto y el desplazamiento
texto_original = input("Ingrese el texto que desea cifrar: ")
desplazamiento = int(input("Ingrese la clave: "))

# Llamar a la función para cifrar el texto ingresado
texto_cifrado = cifrar_texto(texto_original, desplazamiento)

# Mostrar el texto cifrado
print("Texto original:", texto_original)
print("Texto cifrado:", texto_cifrado)
