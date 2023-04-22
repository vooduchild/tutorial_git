def ingresar_numeros():
    numero = float(input('Ingrese un número '))
    return numero

def main():

    numero = 0

    while numero >= 0:

        numero = ingresar_numeros()
        print(numero)

if __name__ == '__main__':
    main()