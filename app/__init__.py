from flask import Flask
from .config import get_config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from redis import Redis
import time
from sqlalchemy.exc import OperationalError

# Extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
redis_client = None

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))

    # Retry DB connection
    for _ in range(5):
        try:
            db.init_app(app)
            break
        except OperationalError as e:
            print("Database connection failed, retrying...")
            time.sleep(2)

    migrate.init_app(app, db)
    jwt.init_app(app)

    global redis_client
    redis_client = Redis.from_url(app.config['REDIS_URL'])

    from .api.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

