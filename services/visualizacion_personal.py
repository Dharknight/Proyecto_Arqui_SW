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
    message = b'00010sinitasipe'
    logging.info ('sending {!r}'.format (message))
    sock.sendall (message)
    while True:
        # Look for the response
        logging.info ("Waiting for register transaction")
        amount_received = 0
        amount_expected = int(sock.recv(5))
        while amount_received < amount_expected:
            data = sock.recv (amount_expected - amount_received)
            amount_received += len (data)
            logging.info('received {!r}'.format(data))
            logging.info ("Visualización de Asistencia por Personal ...")
            data = data.decode().split()
            try:
                opcion = data[1]
                PersonalRut = data[2]
                Fecha = data[3]
                #FechaDesde = data[4]
                #FechaHasta = data[5]
                
                largo = len(PersonalRut+Fecha+opcion) + 8
                message = '000{}datas {} {} {}'.format(largo,opcion,PersonalRut,Fecha).encode()
                logging.info ('sending to bbdd {!r}'.format (message))
                sock.sendall(message)
                algo = sock.recv(4096).decode() 
                if algo:
                    if 'rut' in algo:
                        message = '00011asiperut'.encode()
                    elif 'fecha' in algo:
                        message = '00011asipefecha'.encode()
                    else:
                        message = '00010asipeexito {}'.format(algo).encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)
            except:
                pass
            logging.info('-------------------------------')

finally:
    logging.info ('closing socket')
    sock.close ()