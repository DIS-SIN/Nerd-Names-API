from nerd_names_api import create_app

application = app = create_app()

if __name__ == '__main__':
	app.run(host='0.0.0.0')
