# -*- coding: utf-8 -*-

import logging
from zope.i18nmessageid import MessageFactory


i18n = MessageFactory("taels")
logger = logging.getLogger('taels')


def log(message, summary='', severity=logging.DEBUG):
    logger.log(severity, '%s %s', summary, message)
