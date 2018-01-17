# -*- coding: utf-8 -*-

import os
import taels
import taels_demo
from taels import server
from taels_demo.app import demo_application
from crom import monkey, implicit, configure
from cromlech.jwt.components import JWTHandler, JWTService
from cromlech.i18n import load_translations_directories
from json import loads


def get_key(path):
    if not os.path.isfile(path):
        with open(path, 'w+', encoding="utf-8") as keyfile:
            from cromlech.jwt.components import JWTHandler
            key = JWTHandler.generate_key()
            export = key.export()
            keyfile.write(export)
    else:
        with open(path, 'r', encoding="utf-8") as keyfile:
            from jwcrypto import jwk
            data = loads(keyfile.read())
            key = jwk.JWK(**data)

    return key


async def prepare_crypto(app, loop):
    key = get_key('jwt.key')
    app.jwt_service = JWTService(key, JWTHandler, lifetime=600)

    # Bootstrapping the Crom registry
    monkey.incompat()
    implicit.initialize()

    # Configure
    configure(taels)
    configure(taels_demo)

    print('INITIALIZED !!')
    

if __name__ == '__main__':

    app = taels.Taels('Demo', publisher=demo_application)
    app.register_listener('before_start', prepare_crypto)
    server.run_app(app, host="127.0.0.1", port=8080)
