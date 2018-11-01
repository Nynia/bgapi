import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'skks'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:admin@127.0.0.1/dcn'
    SQLALCHEMY_BINDS = {
        'ismp': 'mysql://root:admin@127.0.0.1/ismp'
    }


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:admin@192.168.114.139/havefun'


config = {
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': TestingConfig
}
