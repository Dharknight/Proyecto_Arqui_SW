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
    #Send data
    message = b'00010sinitupdus'
    logging.info ('sending {!r}'.format (message))
    sock.sendall (message)
    while True:
        #Look for the response
        logging.info ("Waiting for control transaction")
        amount_received = 0
        amount_expected = int(sock.recv(5))
        while amount_received < amount_expected:
            data = sock.recv (amount_expected - amount_received)
            amount_received += len (data)
            logging.info('received {!r}'.format(data))
            logging.info ("Actualización de Usuario...")
            data = data.decode().split()
            try:
                opcion = data[1]
                Nombre = data[2]
                Rut = data[3]
                Email = data[4]
                Contrasena = data[5]
                Telefono = data[6]
                Rol = data[7]
                Jardin = data[8]

                largo = len(Nombre+Rut+Email+Contrasena+Telefono+Rol+Jardin+opcion) + 16
                message = '000{}datos {} {} {} {} {} {} {} {}'.format(largo,opcion,Nombre,Rut,Email,Contrasena,Telefono,Rol,Jardin).encode()
                logging.info ('sending to bbdd {!r}'.format (message))
                sock.sendall(message)

                data = sock.recv(4096).decode()
                largo = 16 + len(data.split()[1])

                if data:
                    message = '000{}updusexito {}'.format(largo,data.split()[1]).encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)
            except:
                pass
            logging.info('-------------------------------')
finally:
    logging.info ('closing socket')
    sock.close ()