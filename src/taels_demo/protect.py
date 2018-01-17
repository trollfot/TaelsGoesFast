# -*- coding: utf-8 -*-

import asyncio
from concurrent.futures import ProcessPoolExecutor
from cromlech.jwt.components import TokenException


executor = ProcessPoolExecutor(4)


def protected(action):

    async def check_token(request):
        token = request.token
        if token:
            try:
                loop = asyncio.get_event_loop()
                payload = await loop.run_in_executor(
                    executor, request.app.jwt_service.check_token, token)
                if payload is not None:
                    return payload
            except (TokenException, ValueError) as err:
                pass
        return None

    async def jwt_protection(inst, request):
        payload = await check_token(request)
        if payload is None:
            return response.text('Unauthorized', status=401)
        request.app.auth_payload = payload
        return await action(inst, request)

    return jwt_protection
