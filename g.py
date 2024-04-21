from src import Server
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default='127.0.0.1',
                        help='Host of the socket.')
    parser.add_argument('-p', '--port', type=int, required=True,
                        help='Port of the socket')
    return parser.parse_args()


def g(x: float) -> float:
    return x * 2


if __name__ == '__main__':
    args = parse_arguments()
    server = Server(host=args.host, port=args.port)
    server.start(function=g)