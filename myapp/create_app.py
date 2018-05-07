from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Inisialisasi FLASK app
app = Flask(__name__)

app.config['IP_ADDRESS'] = "127.0.0.1"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:b1sm1llah@localhost/weekend'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["ENV"] = 'development'

db = SQLAlchemy(app=app)

migrate = Migrate(app=app, db=db)
