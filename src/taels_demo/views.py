# -*- coding: utf-8 -*-

import crom
from sanic.response import text
from taels.interfaces import IView, IRequest, IResponseFactory
from zope.interface import implementer
from .models import Leaf


@crom.adapter
@crom.name('index')
@crom.target(IView)
@crom.sources(Leaf, IRequest)
@implementer(IResponseFactory)
class LeafIndex:

    def __init__(self, context, request):
        self.context = context
        self.request = request
    
    def update(self):
        pass

    def render(self):
        return 'YEAH.'

    async def __call__(self):
        self.update()
        return text(self.render())
