def ingresa_password()->str:
    password = input('Ingresa tu contraseña ')

    return password


def login():

    PASSWORD = 'RealMadrid2023'

    password = ingresa_password()

    password_correcto = False

    while password_correcto == False:
        if password == PASSWORD:
            password_correcto = True
            print('Ingreso exitoso')

        else:
            print('Contraseña incorrecta, intenta de nuevo ')
            password = ingresa_password()


if __name__ == '__main__':
    login()



            
        
