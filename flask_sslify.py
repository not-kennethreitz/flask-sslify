# -*- coding: utf-8 -*-

from flask import request, redirect

YEAR_IN_SECS = 31536000


class SSLify(object):
    """Secures your Flask App."""

    def __init__(self, app, age=YEAR_IN_SECS, subdomains=False):
        if app is not None:
            self.app = app
            self.hsts_age = age
            self.hsts_include_subdomains = subdomains

            self.init_app(self.app)
        else:
            self.app = None

    def init_app(self, app):
        """Configures the configured Flask app to enforce SSL."""
        app.before_request(self.redirect_to_ssl)
        app.after_request(self.set_hsts_header)

    @property
    def hsts_header(self):
        """Returns the proper HSTS policy."""
        hsts_policy = 'max-age={0}'.format(self.hsts_age)

        if self.hsts_include_subdomains:
            hsts_policy += '; includeSubDomains'

        return hsts_policy

    def redirect_to_ssl(self):
        """Redirect incoming requests to HTTPS."""
        # Should we redirect?
        criteria = [
            request.is_secure,
            self.app.debug,
            request.headers.get('X-Forwarded-Proto', 'http') == 'https'
        ]

        if not any(criteria):
            if request.url.startswith('http://'):
                url = request.url.replace('http://', 'https://', 1)
                r = redirect(url)

                return r

    def set_hsts_header(self, response):
        """Adds HSTS header to each response."""
        if request.is_secure:
            response.headers.setdefault('Strict-Transport-Security', self.hsts_header)
        return response



