from random import choice

def crear_palabra():
    lista = ["ocaso","pajaro","mar","desierto","sol"]
    return choice(lista)

def pedir_letra():
    letra = str(input("Introduzca una letra: ").lower())
    return letra

def letra_valida(letra):
    lista_letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n", "ñ","o","p","q","r",
                    "s","t","u","v","w","x","y","z"]

    if len(letra) > 1:
        return False

    if letra in lista_letras:
        return True
    else:
        return False

def iniciar_juego(palabra):
    lista = []
    for i in palabra:
        lista.append("-")

    return lista

def verificar_letra(palabra, letra):
    if letra in palabra:
        return True
    else:
        return False

def actualizar(palabra, letra, conjunto_ahorcado):
    for i in range(len(palabra)):
        if palabra[i] == letra:
            conjunto_ahorcado[i] = letra

    return conjunto_ahorcado

def verificar_ganador(conjunto_ahorcado):
    if "-" in conjunto_ahorcado:
        return False
    else:
        return True


vidas = 6
palabra = crear_palabra()
conjunto_ahorcado = iniciar_juego(palabra)

while vidas > 0 and verificar_ganador(conjunto_ahorcado) == False:
    print(f"Tienes {vidas} vidas")
    print(conjunto_ahorcado)
    letra = pedir_letra()

    if letra_valida(letra) == False:
        continue

    if verificar_letra(palabra, letra):
        actualizar(palabra, letra, conjunto_ahorcado)
    else:
        vidas -= 1

    verificar_ganador(conjunto_ahorcado)

if vidas == 0:
    print("Game Over")
else:
    print("Enhorabuena, has acertado")
    print(f"{conjunto_ahorcado}")