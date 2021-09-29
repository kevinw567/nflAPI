import flask
from flask import jsonify, request
import const as constants
from views import app

from views.passing import passing, cursor, db
from views.rushing import rushing
from views.receiving import receiving
from views.defense import defense
from views.scrimmage import scrimmage
from views.kicking import kicking
from views.returns import returns
from views.scoring import scoring
from views.players import players

# register all stat category blueprints
app.register_blueprint(passing)
app.register_blueprint(rushing)
app.register_blueprint(receiving)
app.register_blueprint(defense)
app.register_blueprint(scrimmage)
app.register_blueprint(kicking)
app.register_blueprint(returns)
app.register_blueprint(scoring)
app.register_blueprint(players)

def create_app():
    app = flask.Flask(__name__, instance_relative_config = True)
    app.config["DEBUG"] = True
    app.config.from_object("config")
    app.config.from_pyfile("config.py")

    return app

# route for the homepage, place holder for now
@app.route("/", methods = ["GET"])
def home():
    return "<h1> NFL Stats API <h1>"

app.run()