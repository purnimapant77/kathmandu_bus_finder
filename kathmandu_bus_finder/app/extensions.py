from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_mail import Mail
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
migrate = Migrate()

# Temporary user class
class AnonymousUser(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
    # Temporary - returns None since we don't have users yet
    return None

# This prevents the error by allowing anonymous users
login_manager.anonymous_user = AnonymousUser
