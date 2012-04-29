Flask-SSLify
============

This is a simple Flask extension that configures your Flask application to redirect
all incoming requests to ``https``.

Redirects only occur when ``app.debug`` is ``False``.

Usage
-----

Usage is pretty simple::

    from flask import Flask
    from flask_sslify import SSLify

    app = Flask(__name__)
    sslify = SSLify(app)


If you make an HTTP request, it will automatically redirect::

    $ curl http://127.0.0.1:5000
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>Redirecting...</title>
    <h1>Redirecting...</h1>
    <p>You should be redirected automatically to target URL: <a href="https://127.0.0.1:5000/">https://127.0.0.1:5000/</a>.  If not click the link.%


Install
-------

Installation is simple too::

    $ pip install Flask-SSLify