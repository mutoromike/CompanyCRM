from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from .config import Config

# database handle
db = SQLAlchemy(session_options={"autoflush": False})

# encryptor handle
bcrypt = Bcrypt()

# manage user login
login_manager = LoginManager()

# function name of the login route that
# tells the path which facilitates authentication
login_manager.login_view = 'users.login'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.url_map.strict_slashes = False
    app.jinja_env.globals.update(zip=zip)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # include the routes
    # from crm import routes
    from crm.main.routes import main
    from crm.users.routes import users
    from crm.leads.routes import leads
    from crm.accounts.routes import accounts
    from crm.contacts.routes import contacts
    from crm.deals.routes import deals
    from crm.settings.routes import settings
    from crm.reports.routes import reports

    # register routes with blueprint
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(settings)
    app.register_blueprint(leads)
    app.register_blueprint(accounts)
    app.register_blueprint(contacts)
    app.register_blueprint(deals)
    app.register_blueprint(reports)

    return app


