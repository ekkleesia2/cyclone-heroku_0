#!/usr/bin/env python
# coding: utf-8
import cyclone.web
import sys
import os

from twisted.internet import reactor
from twisted.python import log


class MainHandler(cyclone.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


if __name__ == "__main__":
    application = cyclone.web.Application([
        (r"/", MainHandler)
    ])

    #log.startLogging(sys.stdout)
    reactor.listenTCP(os.environ.get("PORT", 5000), application)
    reactor.run()
