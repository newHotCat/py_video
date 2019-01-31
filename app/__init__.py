from flask import Flask
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

def createApp():
    app = Flask(__name__)
    app.register_blueprint(home_blueprint)
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@10.165.0.106:3306/video'
    return app
