#   Desarrollo de talento especializado 2021-2: Ciberseguridad
#   Python y Linux
#   Proyecto final - socket_servidor
#   Nayeli Gissel Larios Pérez
import logging
import socket

logging.basicConfig(format='DEBUG : %(message)s',
                    level=logging.DEBUG)


class SocketServer:
    def __init__(self):
        # atributos de la clase SocketServer
        # Crea el socket de comunicacion de tipo stream
        self.connection = None
        self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Se especifica la ip y el puerto de conexion
        self.port_and_ip = ('127.0.0.1', 12345)
        # Atributo donde se almacena la respuesta
        self.resp = ""

    def bind(self):
        # El socket solo se puede ver desde la misma maquina
        self.node.bind(self.port_and_ip)

    def listen(self):
        # Se especifica cuantas solictudes max se pondran en la cola
        self.node.listen(5)

    def accept(self):
        # Acepta conexiones
        self.connection, addr = self.node.accept()

    # Metodo que cierra el socket
    def close(self):
        self.node.shutdown(socket.SHUT_RDWR)
        self.node.close()

    # Metodo que envia el mensaje por el socket
    def send_sms(self, sms):
        self.connection.send(sms.encode())

    # Metodo que procesa la informacion que se va a mandar
    def write(self):
        logging.debug("<<:{}".format(self.resp))
        self.send_sms(self.resp)

    # Metodo que procesa los datos que se reciben por el socket
    def read(self):
        msg = ""
        while msg != "exit":
            # Se indica que recibira mensajes de tamano 20
            msg = self.connection.recv(20).decode()
            logging.debug(">>{}".format(msg))
            # self.resp = str(int(msg) + 14)


if __name__ == '__main__':
    server = SocketServer()
    server.bind()
    server.listen()
    server.accept()
    server.read()
    server.close()
    logging.debug("FIN")
