from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

# 数据库初始化
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.app = app
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/main')

    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')

    return app
