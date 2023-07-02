import socket
import time
import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def obtenerRut():
    while True:
        rut = input("Ingrese el Rut sin puntos y con guion: ")

        rut = rut.lower()
        rut = rut.replace(".", "")
        rut = rut.replace("-", "")
        cuerpo, dv = rut[:-1], rut[-1]
        
        if not cuerpo.isdigit() or dv not in '0123456789k':
            print("* * * Ingrese un rut valido * * *")
        else:
            reverse_cuerpo = cuerpo[::-1]
            factor = 2
            suma = 0
            for c in reverse_cuerpo:
                suma += factor * int(c)
                factor = factor + 1 if factor < 7 else 2

            res = suma % 11
            dvr = 'k' if 11 - res == 10 else str(11 - res)
            if (dv == dvr):
                return rut

def obtenerNumero():
    while True:
        Telefono = input("Ingrese el numero telefonico: ")
        if not Telefono.isdigit() and (len(Telefono)!=8):
            print("* * * Porfavor ingrese un numero valido * * *")
        else:
            return Telefono

def respuestaLogin():
    time.sleep(2)
    data = sock.recv(4096).decode()
    print("recibido")
    if 'exito' in data:
        #print(data.split()[1])
        rol = int(data.split()[1])
        return True,rol
    return False

def respuesta():
    time.sleep(2)
    data = sock.recv(4096).decode()
    print("recibido")
    print(data.split()[1].replace('-',' '))
    
def respuesta_registro_alumno():
    time.sleep(2)
    data = sock.recv(4096).decode()
    print("hola")
    logging.info("Datos sexuales {!r}".format(data))
    print("Datos sexuales {!r}".format(data))

def respuesta_registro_alumno():
    time.sleep(2)
    data = sock.recv(4096).decode()

    if 'exito' in data: print('** Registro Alumno exitoso.')
    elif 'alumnoexistente' in data: print('** Error de Registro: Alumno ya existente en la base de datos.')
    elif 'jardinnoexistente' in data: print('** Error de Registro: El jardin no se encuentra registrado en la base de datos.')
    else: print('** Error de Registro Desconocido.')

def respuesta_actualizar_alumno():
    time.sleep(2)
    data = sock.recv(4096).decode()

    if 'exito' in data: print('** Actualización Alumno exitosa.')
    elif 'alumnonoexistente' in data: print('** Error de Actualización: Alumno no existente en la base de datos.')
    elif 'jardinnoexistente' in data: print('** Error de Actualización: El jardin no se encuentra registrado en la base de datos.')
    else: print('** Error de Actualización Desconocida.')

def respuesta_control_asistencia():
    time.sleep(2)
    data = sock.recv(4096).decode()

    if 'exito' in data: print('** Control asistencia exitosa.')
    else: print('** Control asistencia fallida.')

def respuesta_borrar_alumno():
    time.sleep(2)
    data = sock.recv(4096).decode()

    if 'exito' in data: print('** Eliminación Alumno exitosa.')
    elif 'alumnonoexistente' in data: print('** Error de Eliminación: Alumno no existente en la base de datos.')
    else: print('** Error de Eliminación Desconocida.')

def respuesta_asistencia_jardin():
    time.sleep(2)
    data = sock.recv(4096).decode()
    #print(data)
    if 'exito' in data:
        # Separar la cadena por los corchetes externos
        cadena_sin_corchetes = data.split("[")[1].split("]")[0]

        # Separar los elementos dentro de la lista
        elementos = cadena_sin_corchetes.split(",")
        
        # Convertir los elementos a su tipo de dato correspondiente
        elementos_convertidos = []
        for elemento in elementos:
            elemento = elemento.strip()

            # Comprobar si el elemento es una tupla
            if elemento.startswith("(") and elemento.endswith(")"):
                elemento = eval(elemento)
            # Comprobar si el elemento es un entero
            elif elemento.isdigit():
                elemento = int(elemento)

            elementos_convertidos.append(elemento)

        return True, elementos_convertidos
    elif 'jardin' in data:
        #print('jardin')
        return True, 1
    elif 'fechas' in data:
        #print('fechas')
        return True, 2

def respuesta_comparacion_asistencia():
    time.sleep(2)
    data = sock.recv(4096).decode()
    #print(data)
    if 'exito' in data:
        # Separar la cadena por los corchetes externos
        cadena_sin_corchetes = data.split("[")[1].split("]")[0]

        # Separar los elementos dentro de la lista
        elementos = cadena_sin_corchetes.split(",")
        
        # Convertir los elementos a su tipo de dato correspondiente
        elementos_convertidos = []
        for elemento in elementos:
            elemento = elemento.strip()

            # Comprobar si el elemento es una tupla
            if elemento.startswith("(") and elemento.endswith(")"):
                elemento = eval(elemento)
            # Comprobar si el elemento es un entero
            elif elemento.isdigit():
                elemento = int(elemento)

            elementos_convertidos.append(elemento)

        return True, elementos_convertidos
    elif 'cursos' in data:
        #print('jardin')
        return True, 1
    elif 'fechas' in data:
        #print('fechas')
        return True, 2    

def respuesta_visualizacion_Asistencia_Personal():
    time.sleep(2)
    data = sock.recv(4096).decode()
    #print(data)
    if 'exito' in data:
        # Separar la cadena por los corchetes externos
        cadena_sin_corchetes = data.split("[")[1].split("]")[0]

        # Separar los elementos dentro de la lista
        elementos = cadena_sin_corchetes.split(",")
        
        # Convertir los elementos a su tipo de dato correspondiente
        elementos_convertidos = []
        for elemento in elementos:
            elemento = elemento.strip()

            # Comprobar si el elemento es una tupla
            if elemento.startswith("(") and elemento.endswith(")"):
                elemento = eval(elemento)
            # Comprobar si el elemento es un entero
            elif elemento.isdigit():
                elemento = int(elemento)

            elementos_convertidos.append(elemento)

        return True, elementos_convertidos
    elif 'rut' in data:
        #print('jardin')
        return True, 1
    elif 'fecha' in data:
        #print('fechas')
        return True, 2
    
while True:
    # Create a TCP/IP socket
    sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 5000)
    print ('connecting to {} port {}'.format (*server_address))
    sock.connect (server_address)

    print("Menu Principal")
    print("0 - Salir")
    print("1 - Login")
    opcion = input("¿Que desea hacer?")
    try:
        if opcion == '0':
            print("Saliendo...")
        
        # Login
        if opcion == '1':
            Rut = obtenerRut()
            Contrasena = input("Ingrese la Contrasena:")
            largo = len(Rut+Contrasena+opcion)+13
            message = '000{}login {} {} {}'.format(largo,opcion,Rut,Contrasena).encode()
            print ('sending {!r}'.format (message))
            sock.sendall (message)
            loginState, rol = respuestaLogin()

            if loginState == True and rol == 1: #Director
                print("Login de director realizado correctamente")
                
                while True:
                    print("1 - Actualización Alumno")
                    print("2 - Borrar Alumno")
                    print('3 - Registo Personal')
                    print("4 - Control Asistencia")
                    print("5 - Asistencia por Jardin")
                    print("6 - Comparación Asistencia")
                    print("7 - Visualización Asistencia de Personal")
                    opcion = input("¿Que desea hacer? ")
                    try:
                        if opcion == '1':
                            # Actualización Alumno - updal
                            Rut = obtenerRut()
                            Nombre = input("Ingrese el Nombre: ")
                            Apellido = input("Ingrese el Apellido: ")
                            FechaNacimiento = input("Ingrese el Fecha de Nacimiento (YYYY-MM-DD): ")
                            NombreJardin = input("Ingrese el nombre del Jardin: ").replace(" ", "-")
                            CursoID = input("Ingrese el ID del Curso: ")

                            largo = len( Rut+Nombre+Apellido+FechaNacimiento+NombreJardin+CursoID ) + 13 + 1

                            message = '000{}updal {} {} {} {} {} {} {}'.format( largo,4,Rut,Nombre,Apellido,FechaNacimiento,NombreJardin,CursoID ).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )

                            respuesta_actualizar_alumno()
                    
                        # Borrar Alumno - delal
                        elif opcion == '2':
                            Rut = obtenerRut()

                            largo = len( Rut ) + 13 + 1

                            message = '000{}delal {} {}'.format( largo,5,Rut ).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )

                            respuesta_borrar_alumno()

                        #Registrar Personal - newpe
                        elif opcion == '3':
                            Rut = obtenerRut()
                            Jardin = input("Ingrese el nombre del jardin: ")
                            Nombre = input("Ingrese el nombre del personal: ")
                            Apellido = input("Ingrese el apellido del personal: ")
                            Cargo = input("Ingrese el cargo del personal: ")
                            FechaNacimiento = input("Ingrese la fecha de nacimiento del personal (YYYY-MM-DD): ")

                            largo = len( Rut+Jardin+Nombre+Apellido+Cargo+FechaNacimiento ) + 15

                            message = '000{}newpe {} {} {} {} {} {} {}'.format( largo,opcion,Rut,Jardin,Nombre,Apellido,Cargo,FechaNacimiento ).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )
                            if respuesta():
                                print("Personal registrado correctamente")

                        # Control Asistencia - conas
                        elif opcion == '4':
                            Rut = obtenerRut()
                            Fecha = input("Ingrese la Fecha (YYYY-MM-DD): ")
                            Estado = input("Asiste (1-SI 0-NO) ")

                            largo = len( Rut+Fecha+Estado ) + 13 + 1

                            message = '000{}conas {} {} {} {}'.format( largo,6,Rut,Fecha,Estado ).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )

                            respuesta_control_asistencia()

                        # Asistencia por jardin - asija
                        elif opcion == '5':
                            NombreJardin = input("Ingrese Nombre de Jardin: ")
                            FechaDesde = input("Ingrese Fecha desde (YYYY-MM-DD): ")
                            FechaHasta = input("Ingrese Fecha hasta (YYYY-MM-DD): ")
                            
                            largo = len(NombreJardin+FechaDesde+FechaHasta) + 10 + 2

                            message = '000{}asija {} {} {} {}'.format(largo,14,NombreJardin,FechaDesde,FechaHasta).encode()
                            #print ('sending {!r}'.format (message))
                            sock.sendall(message)
                            a,resultado = respuesta_asistencia_jardin()
                            if a == True and resultado != 1 and resultado != 2:
                                print("Asistencia presentada a continuación")
                                print(resultado)
                            elif a == True and resultado == 1:
                                print('Jardín no existente')
                            elif a == True and resultado == 2:
                                print('No existen asistencias registradas en el jardin en ese rango de fechas')

                        # Comparación Asistencia - comas
                        elif opcion == '6':
                            NivelEducativo1 = input("Ingrese Nivel Educativo 1: ")
                            NivelEducativo2 = input("Ingrese Nivel Educativo 2: ")
                            FechaDesde = input("Ingrese Fecha desde (YYYY-MM-DD): ")
                            FechaHasta = input("Ingrese Fecha hasta (YYYY-MM-DD): ")
                            
                            largo = len(NivelEducativo1+NivelEducativo2+FechaDesde+FechaHasta) + 10 + 2

                            message = '000{}comas {} {} {} {} {}'.format(largo,15,NivelEducativo1,NivelEducativo2,FechaDesde,FechaHasta).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )
                            a,resultado = respuesta_comparacion_asistencia()
                            if a == True and resultado != 1 and resultado != 2:
                                print("Asistencia presentada en el servicio correspondiente")
                                print(resultado)
                            elif a == True and resultado == 1:
                                print('No hay asistencias registradas a los cursos')
                            elif a == True and resultado == 2:
                                print('No existen asistencias registradas a los cursos en el rango de fechas')

                        # Visualización Asistencia de Personal - asipe
                        elif opcion == '7':
                            PersonalRut = input('Ingrese rut sin punto ni guión: ')
                            Fecha = input("Ingrese Fecha (YYYY-MM-DD): ")
                            
                            largo = len(PersonalRut+Fecha) + 10 + 2

                            message = '000{}asipe {} {} {}'.format(largo,16,PersonalRut,Fecha).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )
                            a,resultado =respuesta_visualizacion_Asistencia_Personal() 
                            if a == True and resultado != 1 and resultado != 2:
                                print("Asistencia de personal a continuación")
                                print(resultado)
                            elif a == True and resultado == 1:
                                print('Rut de personal no registrado')
                            elif a == True and resultado == 2:
                                print('No existe asistencia del personal correspondiente a la fecha')

                    except:
                        pass
            
            elif loginState == True and rol == 2: #Administrador
                print("Login de administrador realizado correctamente")
                while True:
                    print("1 - Registro Usuario")
                    print('2 - Eliminar Usuario')
                    print("3 - Creacion Jardín")
                    print("4 - Actualización Jardín")
                    print("5 - Eliminar Jardín")
                    print("6 - Estadísticas Jardín")
                    opcion = input("¿Que desea hacer? ")
                    try:
                        # Registro
                        if opcion == '1':
                            Roles = {
                                'Director':1,
                                'Administrador':2,
                                'Usuario':3
                            }
                            Nombre = input("Ingrese el Nombre:")
                            Rut = obtenerRut()
                            Correo = input("Ingrese el Correo:")
                            Contrasena = input("Ingrese la Contrasena:")
                            Telefono = obtenerNumero()
                            Rol = input("Ingrese el Rol (Director - Usuario):")
                            Jardin  = input("Ingrese el Jardin :")
                            Rol = Roles[Rol]
                            largo = len(Nombre+Rut+Correo+Contrasena+Telefono+Rol+Jardin) + 13 + 1

                            message = '000{}regis {} {} {} {} {} {} {} {}'.format(largo,2,Nombre,Rut,Correo,Contrasena,Telefono,Rol,Jardin).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall (message)
                            if respuesta():
                                print("Registro realizado correctamente")

                        #Eliminar usuario - delus
                        elif opcion == '2': 
                            Rut = obtenerRut()

                            largo = len( Rut ) + 10 + 2

                            message = '000{}delus {} {}'.format( largo,11,Rut ).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )
                            if respuesta():
                                print("Usuario eliminado correctamente")
                    
                        # Creacion Jardin - newja
                        elif opcion == '3':
                            NombreJardin = input("Ingrese el nombre del jardín a crear: ").replace(' ','-')
                            Direccion = input("Ingrese la dirección del jardín: ").replace(' ','-')
                            Telefono = obtenerNumero()

                            largo = len(NombreJardin+Direccion+Telefono) + 12 + 1

                            message = '000{}newja {} {} {} {}'.format( largo,7,NombreJardin,Direccion,Telefono ).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message)
                            respuesta()
                    
                        # Actualizar Jardin - updja
                        elif opcion == '4':
                            Nombre1 = input("Ingrese el nombre del jardín a actualizar: ")
                            Nombre2 = input("Ingrese el nuevo nombre para este jardin: ").replace(' ','-')
                            Direccion = input("Ingrese la nueva dirección: ").replace(' ','-')
                            Telefono = obtenerNumero()

                            largo = len( Nombre1+Nombre2+Direccion+Telefono ) + 13 + 1

                            message = '000{}updja {} {} {} {} {}'.format( largo,8,Nombre1,Nombre2,Direccion,Telefono ).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )
                            respuesta()
                    
                        # Eliminar Jardin - delja
                        elif opcion == '5':
                            Nombre = input("Ingrese el nombre del jardín a eliminar: ").replace(' ','-')

                            largo = len( Nombre ) + 10 + 1

                            message = '000{}delja {} {}'.format( largo,9,Nombre ).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )
                            respuesta()

                        # Estadisticas Jardin - estja
                        elif opcion == '6':
                            Nombre = input("Ingrese el nombre del jardín para consultar estadisticas: ").replace(' ','-')
                            
                            largo = len( Nombre ) + 10 + 2

                            message = '000{}estja {} {}'.format( largo,10,Nombre ).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )
                            respuesta()

                    except:
                        pass

            elif loginState == True and rol == 3: #Usuario
                print("Login de usuario realizado correctamente")
                while True:
                    print("1 - Registro Alumno")
                    print('2 - Actualizar Usuario')
                    opcion = input("¿Que desea hacer? ")
                    try:
                        # Registro Alumno - newal
                        if opcion == '1':
                            Rut = obtenerRut()
                            Nombre = input("Ingrese el Nombre: ")
                            Apellido = input("Ingrese el Apellido: ")
                            FechaNacimiento = input("Ingrese el Fecha de Nacimiento (YYYY-MM-DD): ")
                            NombreJardin = input("Ingrese el nombre del Jardin: ").replace(" ", "-")
                            CursoID = input("Ingrese el ID del Curso: ")

                            largo = len(Rut+Nombre+Apellido+FechaNacimiento+NombreJardin+CursoID) + 13 + 1

                            message = '000{}newal {} {} {} {} {} {} {}'.format(largo,3,Rut,Nombre,Apellido,FechaNacimiento,NombreJardin,CursoID).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )

                            respuesta_registro_alumno()
                            
                        #Actualizacion de usuario - updus
                        elif opcion == '2':
                            Rut = obtenerRut()
                            Nombre = input("Ingrese el nuevo nombre: ")
                            Correo = input("Ingrese el nuevo correo: ")
                            Contrasena = input("Ingrese la nueva contraseña: ")
                            Telefono = obtenerNumero()
                            Rol = input("Ingrese el nuevo rol: ")
                            Jardin = input("Ingrese el nuevo jardin: ")

                            largo = len( Nombre+Rut+Correo+Contrasena+Telefono+Rol+Jardin ) + 16 + 1

                            message = '000{}updus {} {} {} {} {} {} {} {}'.format( largo,12,Nombre,Rut,Correo,Contrasena,Telefono,Rol,Jardin ).encode()
                            print ('sending {!r}'.format (message))
                            sock.sendall( message )
                            respuesta()

                    except:
                        pass
        
    finally:
        sock.close ()
