# -*- coding: utf-8 -*-

from flask import request, redirect

class SSLify(object):

    def __init__(self, app):

        if app is not None:
            self.app = app
            self.init_app(self.app)
        else:
            self.app = None

    def init_app(self, app):
        app.before_request(self.redirect)

    def redirect(self):

        criteria = [
            request.is_secure,
            self.app.debug,
            request.headers.get('X-Forwarded-Proto', 'http') == 'https'
        ]

        if not any(criteria):
            url = request.url.replace('http://', 'https://')
            r = redirect(url)

            # HSTS policy.
            r.headers['Strict-Transport-Security'] = 'max-age=31536000'

            return r


