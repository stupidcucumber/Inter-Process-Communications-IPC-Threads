import socket, time
from .thread import TimedThread


class Client:
    def __init__(self, port_h: int, port_g: int,
                 host_h: str = '127.0.0.1', host_g: str = '127.0.0.1',
                 seconds: float = 5) -> None:
        self.host_h = host_h
        self.host_g = host_g
        self.port_h = port_h
        self.port_g = port_g
        self.seconds = seconds

    def _instantiate_socket(self, host: str, port: int) -> socket.socket:
        result = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result.connect((host, port))
        return result

    def event_loop(self, socket_g: socket.socket, socket_h: socket.socket) -> None:
        value_recieved = False
        while (x := input('Write x: ')) != '':
            thread_h = TimedThread(socket=socket_g, x=x)
            thread_g = TimedThread(socket=socket_h, x=x)
            thread_h.start()
            thread_g.start()
            start_counter = time.perf_counter()
            while thread_g.value is None or thread_h.value is None:
                if (time.perf_counter() - start_counter) > self.seconds:
                    answer = input('Do you want to stop the process? (y/n)').strip()
                    if answer == 'y':
                        socket_h.close()
                        socket_g.close()
                        break
                    else:
                        start_counter = time.perf_counter()
            else:
                value_recieved = True
            if value_recieved:
                result = thread_g.value * thread_h.value
                print(f'Result is {result}')
            else:
                print('Connection has been closed!')
                return

    def start(self) -> None:
        socket_g = self._instantiate_socket(host=self.host_g, port=self.port_g)
        socket_h = self._instantiate_socket(host=self.host_h, port=self.port_h)
        try:
            self.event_loop(
                socket_g=socket_g,
                socket_h=socket_h
            )
        finally:
            socket_g.close()
            socket_h.close()