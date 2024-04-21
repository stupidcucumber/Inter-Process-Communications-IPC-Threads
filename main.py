import argparse
from src import Client


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host-h', type=str, default='127.0.0.1')
    parser.add_argument('--host-g', type=str, default='127.0.0.1')
    parser.add_argument('--port-h', type=int, required=True)
    parser.add_argument('--port-g', type=int, required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    client = Client(
        port_h=args.port_h,
        port_g=args.port_g,
        host_h=args.host_h,
        host_g=args.host_g
    )
    client.start()