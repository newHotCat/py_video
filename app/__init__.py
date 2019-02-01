from flask import Flask
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint
from app.models import db,Role,Admin

def createApp():
    app = Flask(__name__)
    app.register_blueprint(home_blueprint)
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@10.165.0.106:3306/video'
    db.init_app(app)
    db.create_all(app=app)
    addrole(app)
    
    return app

def addrole(app):
    with app.app_context():
        # role = Role(
        #     name="超级管理员",
        #     auths=""
        # )
        # db.session.add(role)
        # db.session.commit()
        # from werkzeug.security import generate_password_hash
        # admin = Admin(
        #     name="imoocvideo_now",
        #     pwd=generate_password_hash('imoocvideo_now'),
        #     is_super=0,
        #     role_id=3
        # )
        # db.session.add(admin)
        # db.session.commit()
        for item in Admin.query.all():
            print(item.addtime)
