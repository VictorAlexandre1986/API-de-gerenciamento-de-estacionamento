import os

from flask import Flask

from flaskr.db import config_sql_alchemy, db_instance
from flaskr.init_db import init_load_data
from flaskr.migrate import load_migrate
from flaskr.routes import config_app_routes
from flaskr.schema import config_marshmallow
from flaskr.security import config_app_cors, config_jwt_token
from flaskr.swagger_docs import config_swagger
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['BUNDLE_ERRORS'] = True
app.config['DEBUG'] = int(os.environ.get('FLASK_DEBUG', '0')) == 1

# Config SQLAlchemy
config_sql_alchemy(app)

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_load_data()
    print('Initialized the database.')

# Config Marshmallow
config_marshmallow(app)

# Config Flask JWT Extended
jwt = config_jwt_token(app)

# Config App CORS
config_app_cors(app)

# Config Swagger Documentation
docs = config_swagger(app)

# Config Flask Restful
api = config_app_routes(app, docs)


# Load Flask Migrate
migrate = load_migrate(db_instance, app)


if __name__ == '__main__':
    app.run()
