import os
class Usuario:
    def __init__(self, usuario, password, nombre, curp, ciudad):
        self.usuario = usuario
        self.password = password
        self.rol = 'Cliente'
        self.nombre = nombre
        self.curp = curp
        self.ciudad = ciudad

# Lista para almacenar usuarios registrados
listOfUsers = []

stateOfMenu = True
usuarioAdmin = Usuario(usuario='admin',password='123',ciudad='Desconocido', curp='No existente', nombre='Administrador')
listOfUsers.append(usuarioAdmin)
while stateOfMenu:
    optionMenu = int(input('Ingrese la opción:\n1- Registro\n2- Inicio de sesión\n3- Salida'))
    
    if optionMenu == 1:
        curpUser = input('Ingresa tu CURP: ')
        user_exists = False
        for user in listOfUsers:
            if user.curp == curpUser:
                print('Usuario ya existente')
                user_exists = True
                break
        
        if not user_exists:
            usuarioData = Usuario(
                input('Ingresa tu usuario: '),
                input('Ingresa tu contraseña: '),
                input('Ingresa tu nombre: '),
                curpUser,
                input('Ingresa tu ciudad: ')
            )
            listOfUsers.append(usuarioData)
            print('Usuario registrado exitosamente!')

    elif optionMenu == 2:
        nickName = input('Ingresa tu usuario: ')
        password = input('Ingresa tu contraseña: ')
        
        logged_in = False
        for user in listOfUsers:
            if usuarioAdmin.usuario == nickName and usuarioAdmin.password == password:
                os.system("clear")
                for userItem in listOfUsers:
                    print('Nombre de usuario: ', userItem.nombre)
                    print('CURP: ', userItem.curp)
                    print('Ciudad: ', userItem.ciudad)
                    print('Rol: ', userItem.rol)
                break
            elif user.usuario == nickName and user.password == password:
                os.system("clear")
                print('Sesión iniciada como', user.usuario)
                print('Nombre de usuario: ', user.nombre)
                print('CURP: ', user.curp)
                print('Ciudad: ', user.ciudad)
                print('Rol: ', user.rol)
                logged_in = True
                break  
        
        if not logged_in:
            print('datos incorrectos')

    elif optionMenu == 3:
        stateOfMenu = False
    else:
        print('Opción no válida. Por favor, elige una opción válida.')

print('Finalizacion del programa.')
