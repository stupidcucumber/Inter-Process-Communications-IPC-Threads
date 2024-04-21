import threading
import socket, struct


class TimedThread(threading.Thread):
    def __init__(self, socket: socket.socket, x: float, name: str = None) -> None:
        super(TimedThread, self).__init__(name=name)
        self.socket = socket
        self.x = x
        self.value = None
    
    def _get_result(self, server: socket.socket, x: float) -> float:
        server.sendall(struct.pack('f', float(x)))
        data = server.recv(1024)
        return struct.unpack('f', data)[0]

    def run(self) -> None:
        self.value = self._get_result(server=self.socket, x=self.x)