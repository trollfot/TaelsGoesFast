# -*- coding: utf-8 -*-

from functools import partial
from dawnlight.core import ResolveError
from taels.interfaces import IView
from taels.publisher import Publisher, model_lookup, view_lookup
from cromlech.security import security_check, security_predication
from cromlech.security import unauthenticated_principal as anonymous
from .models import Leaf, Root

from sanic import exceptions


# Root serves as a publication root, for the authenticated users.
# It behaves like a dict, but it will locate objects upon retrieval
# using the `__getitem__` method.
root = Root({
    'green': Leaf('Green leaf', 'A summer leaf'),
    'yellow': Leaf('Yellow leaf', 'An automn leaf'),
})


async def view_lookup_method(request, obj, name):
    return IView(obj, request, name=name, default=None)

publisher = Publisher(model_lookup, view_lookup(view_lookup_method))


async def publish(request, principal):
    request.principal = principal
    try:
        return await publisher(request, root)
    except ResolveError:
        raise exceptions.NotFound('Resource not found.')


async def demo_application(request):
    request.security_policy = (security_predication, security_check)
    response = await publish(request, anonymous)
    return response
