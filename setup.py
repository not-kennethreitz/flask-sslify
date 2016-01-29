"""
Flask-SSLify
------------

This is a simple Flask extension that configures your Flask application to redirect
all incoming requests to ``https``.

Redirects only occur when ``app.debug`` is ``False``.
"""

from setuptools import setup

setup(
    name='Flask-SSLify',
    version='0.1.6',
    url='https://github.com/kennethreitz/flask-sslify',
    license='BSD',
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    description='Force SSL on your Flask app.',
    long_description=__doc__,
    py_modules=['flask_sslify'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
