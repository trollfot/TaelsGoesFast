# -*- coding: utf-8 -*-

from loader import Configuration


with Configuration('config.json') as config:

    from taels import Taels

    app = Taels(__name__)
    app.run(host="0.0.0.0", port=8080)
