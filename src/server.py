import socket, struct
from typing import Callable
from .model import ServerStatus


class Server:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    def start(self, function: Callable) -> ServerStatus:    
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((self.host, self.port))
            server.listen()
            connection, _ = server.accept()
            with connection:
                while True:
                    data = connection.recv(1024)
                    if not data:
                        break
                    x = struct.unpack('f', data)[0]
                    y = function(x)
                    connection.sendall(struct.pack('f', float(y)))
        return ServerStatus.SUCCESSFULL