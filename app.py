import flask
from flask import jsonify, request
import const as constants
import mysql.connector
from views import app

# import stat view blueprints
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

"""
    Get all general information for all players in the database.

    Response:
        The name, position and team of all players in the database.
"""
@app.route("/stats/nfl/players/all", methods = ["GET"])
def get_all_players():
    if "sortby" in request.args:
        cursor.execute("SELECT name, position, team FROM player_info ORDER BY " + request.args["sortby"] + ";")
        results = cursor.fetchall()
            
        return jsonify(results)

    else:
        cursor.execute("SELECT name, position, team FROM player_info")
        results = cursor.fetchall()
            
        return jsonify(results)
    
"""
    Search for players based on general information

    Returns:
        The name, position and team for all players that match the search requirements.
"""
@app.route("/stats/nfl/players", methods = ["GET"])
def get_players():
    query = "SELECT name, position, team from player_info WHERE "
    vals = []
    # formulate query with endpoint arguments
    if "name" in request.args:
        query += "name = %s AND"
        vals.append(request.args["name"])

    if "position" in request.args:
        query += "position = %s AND"
        vals.append(request.args["position"])

    if "team" in request.args:
        query += "team = %s AND"
        vals.append(request.args["team"].upper())

    # remove the last 'AND' and add terminating semicolon
    query = query[:-4] + ";"
    cursor.execute(query, vals)
    results = cursor.fetchall()

    return jsonify(results)

app.run()
