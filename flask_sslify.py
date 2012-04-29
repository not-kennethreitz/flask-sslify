# -*- coding: utf-8 -*-

from flask import current_app as app
from flask import request, redirect

class SSLify(object):
    def __init__(self, app):
        self.app = app

        self.install_sslify(self.app)

    @classmethod
    def install_sslify(cls, app):

        app.before_request(cls.redirect)

    @staticmethod
    def redirect():
        if (not request.is_secure) and (not app.debug):
            url = request.url.replace('http://', 'https://')
            return redirect(url)