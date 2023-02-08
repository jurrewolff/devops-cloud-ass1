#!/usr/bin/env python3

import connexion

from swagger_server import encoder


def main():
    print("Hardcoded URL: http://127.0.0.1:8080/tutorial/1.0.0/ui/")
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Simple Inventory API'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
