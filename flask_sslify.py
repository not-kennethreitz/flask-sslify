# -*- coding: utf-8 -*-

from flask import request, redirect

class SSLify(object):

    def __init__(self, app, age=31536000, subdomains=False):

        if app is not None:
            self.app = app
            self.hsts_age = age
            self.hsts_include_subdomains = subdomains

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
            hsts_policy = 'max-age={0}'.format(self.hsts_age)

            if self.hsts_include_subdomains:
                hsts_policy += '; includeSubDomains'

            r.headers['Strict-Transport-Security'] = hsts_policy

            return r


