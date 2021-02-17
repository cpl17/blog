from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_gravatar import Gravatar




app = Flask(__name__)

app.config.from_object('config.settings')

Bootstrap(app)
db = SQLAlchemy(app)
ckeditor = CKEditor(app)
gravatar = Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False, use_ssl=False, base_url=None)


# Login Manager

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404



from app.mod_auth.controllers import mod_auth as auth_module
from app.mod_home.controllers import mod_home as home_module
from app.mod_admin.controllers import mod_admin as admin_module

app.register_blueprint(auth_module)
app.register_blueprint(home_module)
app.register_blueprint(admin_module)

db.create_all()