from flask import Flask
from flask_sslify import SSLify
from pytest import fixture


@fixture
def sslify():
    app = Flask(__name__)
    app.config['DEBUG'] = False
    app.config['TESTING'] = False
    app.config['SERVER_NAME'] = 'example.com'
    sslify = SSLify(app)

    @app.route('/')
    def home():
        return 'home'

    return sslify


def test_default_config(sslify):
    assert sslify.hsts_include_subdomains is False
    assert sslify.permanent is False
    assert sslify.skip_list is None


def test_redirection(sslify):
    client = sslify.app.test_client()
    r = client.get('/')
    assert r.status_code == 302
    assert r.headers['Location'] == 'https://example.com/'


def test_hsts_header(sslify):
    client = sslify.app.test_client()
    r = client.get('/', base_url='https://example.com')
    assert r.status_code == 200
    assert r.data.decode('utf-8') == 'home'
    assert r.headers['Strict-Transport-Security'] == 'max-age=31536000'
