import json
from flask import Flask
from nerd_names_api.config import Config


# Application factory
def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)
	
	# Register database
	from nerd_names_api import db
	db.init_app(app)
	
	# Register blueprints
	from nerd_names_api.main_routes.routes import main
	app.register_blueprint(main)
	return app
