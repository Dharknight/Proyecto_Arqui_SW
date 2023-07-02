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
    message = b'00010sinitcomas'
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
            logging.info ("Comparando Asistencia ...")
            data = data.decode().split()
            logging.info(data)
            try:
                opcion = data[1]
                NivelEducativo1 = data[2]
                NivelEducativo2 = data[3]
                FechaDesde = data[4]
                FechaHasta = data[5]
                largo = len(NivelEducativo1+NivelEducativo2+FechaDesde+FechaHasta+opcion) + 10
                message = '000{}datas {} {} {} {} {}'.format(largo,opcion,NivelEducativo1,NivelEducativo2,FechaDesde,FechaHasta).encode()
                logging.info ('sending to bbdd {!r}'.format (message))
                sock.sendall(message)
                algo = sock.recv(4096).decode()
                if algo:
                    if 'cursos' in algo:
                        message = '00011comascursos'.encode()
                    elif 'fechas' in algo:
                        message = '00011comaserfchas'.encode()
                    elif 'exito' in algo:
                        message = '00010comasexito {}'.format(algo).encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)
            except:
               pass
            logging.info('-------------------------------')

finally:
    logging.info ('closing socket')
    sock.close ()