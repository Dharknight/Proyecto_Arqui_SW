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
    message = b'00010sinitlogin'
    logging.info ('sending {!r}'.format (message))
    sock.sendall (message)
    while True:
        # Look for the response
        logging.info ("Waiting for transaction Login")
        amount_received = 0
        amount_expected = int(sock.recv(5))
        while amount_received < amount_expected:
            data = sock.recv (amount_expected - amount_received)
            amount_received += len (data)
            logging.info('received {!r}'.format(data))
            logging.info ("Processing login...")
            data = data.decode().split()
            try:
                opcion = data[1]
                Rut = data[2]
                Contrasena = data[3]
                
                largo = len(Rut + Contrasena) + 8
                message = '000{}datos {} {} {}'.format(largo,opcion,Rut,Contrasena).encode()
                logging.info ('sending to bbdd {!r}'.format (message))
                sock.sendall(message)
                algo = sock.recv(4096)
                if algo:
                    message = '00010loginexito {}'.format(algo.decode().split()[1]).encode()
                    logging.info ('sending {!r}'.format (message))
                    sock.send(message)
            except:
                pass
            logging.info('-------------------------------')

finally:
    logging.info ('closing socket')
    sock.close ()