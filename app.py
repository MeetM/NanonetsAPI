from flask import Flask
from apis import api
import config
from models import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# Flask Application object
app = Flask(__name__)

# Flask config
app.config.from_object(config.get_config())

# Register flask_restplus APIs with app instance
api.init_app(app)

# Register SQL Alchemy
db.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
