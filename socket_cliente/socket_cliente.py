#   Desarrollo de talento especializado 2021-2: Ciberseguridad
#   Python y Linux
#   Proyecto final - socket_cliente
#   Nayeli Gissel Larios Pérez
import logging
import socket

logging.basicConfig(format='DEBUG : %(message)s',
                    level=logging.DEBUG)


class SocketClient:
    def __init__(self):
        # atributos de la clase SocketClient
        # Crea el socket de comunicacion de tipo stream
        self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Se especifica la ip y el puerto de conexion
        self.port_and_ip = ('127.0.0.1', 12345)
        logging.debug(">>CLIENTE socket creado")

    def connect(self):
        # Conecta el socket a la direccion especificada
        try:
            self.node.connect(self.port_and_ip)
        except ConnectionRefusedError:
            logging.debug(">>CLIENTE socket servidor en {} no esta activo".format(self.port_and_ip[0]))
        logging.debug(">>CLIENTE socket conectado a {}".format(self.port_and_ip[0]))

    # Metodo que cierra el socket
    def close(self):
        self.node.shutdown(socket.SHUT_RDWR)
        self.node.close()
        logging.debug(">>CLIENTE socket cerrado")

    # Metodo que envia el mensaje por el socket
    def send_sms(self, sms):
        self.node.send(sms.encode())

    # Metodo que procesa la informacion que se va a mandar
    def write(self, text):
        message = text
        logging.debug(">>:{}".format(text))
        self.send_sms(message)

    # Metodo que procesa los datos que se reciben por el socket
    def read(self):
        msg = ""
        while msg == "":
            # Se indica que recibira mensajes de tamano
            msg = self.node.recv(2).decode()
            if msg != "":
                logging.debug("<<:{}".format(msg))

    def comunicacion(self):
        message = ""
        while message != "exit":
            message = input("> ")
            self.write(message)
            # client.read()
        client.close()


if __name__ == '__main__':
    client = SocketClient()
    client.connect()
    client.comunicacion()
