# main file, using the functions in the other files to create the final output

import argparse
from src.interface_adapters.json_to_csv import json_to_csv
from src.interface_adapters.controllers import run_api


def main():
    parser = argparse.ArgumentParser(description='Back End Scrapper Challenge')
    parser.add_argument('mode', choices= ['format-json', 'start-api'],
                        help="format-json: formats the JSON file, start-api: starts the api")
    parser.add_argument('--json', help="URL of json file or JSON local file to format", required=False)
    parser.add_argument('--csv',help="CSV filename to save the formatted JSON", required=False)
    args = parser.parse_args()

    if args.mode == 'format-json':
        try:
            json_to_csv(args.json, args.csv)
        except ValueError as e:
            print(e)

    elif args.mode == 'start-api':
        run_api()


if __name__ == '__main__':
    main()