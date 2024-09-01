from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from models import db, Admin
from config import Config
from routes.user_routes import user_bp
from routes.admin_routes import admin_bp

app = Flask(__name__)
app.config.from_object(Config)

