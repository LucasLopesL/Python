from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SECRET_KEY"] = '8751bba800902650b5feb5346c908fc3' # secrets.token_hex(16)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projeto.db"

database = SQLAlchemy(app)

from projeto_flask import routes
