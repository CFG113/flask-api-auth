from flask import Flask
from dotenv import load_dotenv
from config.config import Config
from utils.extensions import db, bcrypt
from controllers.auth_controller import auth_bp

def create_app():
    # Load environment variables from .env file
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()  

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
