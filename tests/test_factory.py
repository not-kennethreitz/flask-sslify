from flask import Flask
from flask_sslify import SSLify
from pytest import fixture


class AppFactoryContext(object):

    def __init__(self):
        self.sslify = SSLify()
        self.app = None
        self.appctx = None

    def __enter__(self):
        self.app = self.create_app()
        self.appctx = self.app.app_context()
        self.appctx.push()
        return self.appctx

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.appctx.pop()
        self.app = None
        self.appctx = None

    def create_app(self):
        app = Flask(__name__)
        app.config['DEBUG'] = False
        app.config['TESTING'] = False
        app.config['SERVER_NAME'] = 'example.com'
        app.config['SSLIFY_PERMANENT'] = True
        self.sslify.init_app(app)
        app.add_url_rule('/', 'home', self.view_home)
        return app

    def view_home(self):
        return 'home'


@fixture
def app_factory():
    context = AppFactoryContext()
    with context:
        yield context


def test_config(app_factory):
    assert app_factory.sslify.hsts_include_subdomains is False
    assert app_factory.sslify.permanent is True
    assert app_factory.sslify.skip_list is None


def test_redirection(app_factory):
    client = app_factory.app.test_client()
    r = client.get('/')
    assert r.status_code == 301
    assert r.headers['Location'] == 'https://example.com/'


def test_hsts_header(app_factory):
    client = app_factory.app.test_client()
    r = client.get('/', base_url='https://example.com')
    assert r.status_code == 200
    assert r.data.decode('utf-8') == 'home'
    assert r.headers['Strict-Transport-Security'] == 'max-age=31536000'
