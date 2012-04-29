Flask-SSLify
============

This is a simple Flask extension that configures your Flask application to redirect
all incoming requests to HTTPS.

Redirects only occur when ``app.debug`` is ``False``.

Usage
-----

Usage is pretty simple::

    from flask import Flask
    from flask_sslify import SSLify

    app = Flask(__name__)
    sslify = SSLify(app)


If you make an HTTP request, it will automatically redirect::

    $ curl -I http://secure-samurai.herokuapp.com/
    HTTP/1.1 302 FOUND
    Content-length: 281
    Content-Type: text/html; charset=utf-8
    Date: Sun, 29 Apr 2012 21:39:36 GMT
    Location: https://secure-samurai.herokuapp.com/
    Server: gunicorn/0.14.2
    Strict-Transport-Security: max-age=31536000
    Connection: keep-alive


HTTP Strict Transport Security
------------------------------

Flask-SSLify also provides your application with an HSTS policy.

By default, HSTS is set for on year (31536000 seconds).

You can change the duration by passing the `age` parameter::

    sslify = SSLify(app, age=300)

If you'd like to include subdomains in your HSTS policy, set the `subdomains` parameter::

    sslify = SSLify(app, subdomains=True)


Install
-------

Installation is simple too::

    $ pip install Flask-SSLify