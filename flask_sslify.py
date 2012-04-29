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

        criteria = [
            request.is_secure,
            app.debug,
            request.headers.get('X-Forwarded-Proto', 'http') == 'https'
        ]

        if not any(criteria):
            url = request.url.replace('http://', 'https://')
            return redirect(url)