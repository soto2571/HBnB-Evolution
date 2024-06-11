from flask import Flask
from api import user_routes, place_routes
from config import SECRET_KEY

def create_app():
    my_app = Flask(__name__)

    # Load configuration settings from config.py
    my_app.config.from_pyfile('config.py')

    # Registering blueprints from the api package
    my_app.register_blueprint(user_routes.blueprint)
    my_app.register_blueprint(place_routes.blueprint)
    
    return my_app

if __name__ == '__main__':
    my_app = create_app()
    my_app.run(debug=True, host='0.0.0.0')

