import socket
import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Create a TCP/IP socket
sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
logging.info ('connecting to {} port {}'.format (*server_address))
sock.connect (server_address)
try:
    # Send data
    message = b'00010sinitupdal'
    logging.info ('sending {!r}'.format (message))
    sock.sendall (message)
    while True:
        # Look for the response
        logging.info ("Waiting for Update transaction")
        amount_received = 0
        amount_expected = int(sock.recv(5))
        while amount_received < amount_expected:
            data = sock.recv (amount_expected - amount_received)
            amount_received += len (data)
            logging.info('received {!r}'.format(data))
            logging.info ("Actualizando Alumno...")
            data = data.decode().split()
            try:
                opcion = data[1]
                Rut = data[2]
                Nombre = data[3]
                Apellido = data[4]
                FechaNacimiento = data[5]
                NombreJardin = data[6]
                CursoID = data[7]
                
                largo = len(Rut+Nombre+Apellido+FechaNacimiento+NombreJardin+CursoID+opcion) + 13
                message = '000{}datos {} {} {} {} {} {} {}'.format(largo,opcion,Rut,Nombre,Apellido,FechaNacimiento,NombreJardin,CursoID).encode()
                logging.info ('sending to bbdd {!r}'.format (message))
                sock.sendall(message)

                data = sock.recv(4096).decode()
                if 'exito' in data:
                    message = '00010updalexito'.encode()
                elif 'alumnonoexistente' in data:
                    message = '00027updalfallidoalumnonoexistente'.encode()
                elif 'jardinnoexistente' in data:
                    message = '00029updalfallidojardinnoexistente'.encode()
                else:
                    message = '00012updalfallido'.encode()
                
                logging.info ('sending {!r}'.format (message))
                sock.sendall(message)

            except:
                pass
            logging.info('-------------------------------')

finally:
    logging.info ('closing socket')
    sock.close ()