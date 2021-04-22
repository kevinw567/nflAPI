import flask
import mysql.connector

# create flask app and configure
app = flask.Flask(__name__, instance_relative_config = True)
app.config["DEBUG"] = True
app.config.from_object("config")
app.config.from_pyfile("config.py")

# connect to database 
db = mysql.connector.connect(
    host = app.config["HOST"],
    user = app.config["USER"],
    password = app.config["PASSWORD"],
    database = app.config["DATABASE"]
)

# represent the database results as a dictionary for use as JSON
cursor = db.cursor(dictionary = True)