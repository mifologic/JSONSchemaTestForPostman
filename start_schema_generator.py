import argparse
import json

from get_data_for_schema_generation import get_data_for_schema_generation


def start_generator(method, url, body):
    print(get_data_for_schema_generation(method, url, body))


parser = argparse.ArgumentParser(description='Arguments for json-schema generator')
parser.add_argument('method', type=str, help='Name of method')
parser.add_argument('url', type=str, help='Request url')
parser.add_argument(
    '--body',
    type=str,
    default=None,
    help='Request body'
)
args = parser.parse_args()

data = None

if args.body:
    data = json.loads(args.body)

if __name__ == '__main__':
    start_generator(args.method, args.url, data)
