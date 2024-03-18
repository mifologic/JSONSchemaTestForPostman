import argparse
import json
import sys

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

# python3 start_schema_generator.py POST https://fakerestapi.azurewebsites.net/api/v1/Activities --body="{\"id\":0,\"title\":\"Activity 14\",\"dueDate\":\"2024-03-17T20:57:04.425Z\",\"completed\":false}"
# python3 start_schema_generator.py GET https://fakerestapi.azurewebsites.net/api/v1/Books

