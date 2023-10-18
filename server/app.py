from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from server.resources.user_resource import UserResource
from server.config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

api.add_resource(UserResource, '/users', '/users/<int:user_id>')

if __name__ == '__main__':
    app.run()
