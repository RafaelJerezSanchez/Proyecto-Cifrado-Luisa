def descifrar_texto(texto_cifrado, desplazamiento):
    texto_descifrado = ""

    for caracter in texto_cifrado:
        if caracter.isalpha():
            mayuscula = caracter.isupper()
            codigo = ord(caracter.upper())
            codigo_descifrado = (codigo - 65 - desplazamiento + 26) % 26 + 65
            caracter_descifrado = chr(codigo_descifrado)
            if mayuscula:
                texto_descifrado += caracter_descifrado
            else:
                texto_descifrado += caracter_descifrado.lower()
        else:
            texto_descifrado += caracter

    return texto_descifrado

# Pedir al usuario que ingrese el texto cifrado y el valor de desplazamiento
texto_cifrado = input("Ingrese el texto cifrado que desea descifrar: ")
valor_desplazamiento = int(input("Ingrese la clave para descifrar: "))

# Llamar a la función para descifrar el texto ingresado
texto_descifrado = descifrar_texto(texto_cifrado, valor_desplazamiento)

# Mostrar el texto descifrado
print("Texto cifrado:", texto_cifrado)
print("Texto descifrado:", texto_descifrado)
