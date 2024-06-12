from flask import Flask
from app.api.user_routes import user_routes
from app.api.place_routes import place_routes
from config import SECRET_KEY

def create_app():
    my_app = Flask(__name__)

    # Load configuration settings from config.py
    my_app.config.from_pyfile('config.py')

    # Registering blueprints from the api package
    my_app.register_blueprint(user_routes) # removed blueprint from user_route
    my_app.register_blueprint(place_routes) # same as above
    
    return my_app

if __name__ == '__main__':
    my_app = create_app()
    my_app.run(debug=True, host='0.0.0.0')
