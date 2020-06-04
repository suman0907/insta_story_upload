from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config




db= SQLAlchemy()
migrate = Migrate()



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    #Config.init_app(WebApp)
    db.init_app(app)
    import WebApp.MyStory.models
    migrate.init_app(app, db)

    from WebApp.MyStory.views import test as my_route
    app.register_blueprint(my_route, url_prefix='/story')




    return app
