from flask import Blueprint, jsonify, request
from views import db, cursor
import const as constants
import mysql.connector

players = Blueprint("players", __name__, url_prefix= "/stats/nfl/players/")

@players.route("all", methods = ["GET"])
#TODO: add sortby and order
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
#TODO: add sortby and order
@players.route("", methods = ["GET", "POST"])
def get_players():
    query = "SELECT name, position, team from player_info WHERE "
    vals = []
    # formulate query with endpoint arguments
    if "name" in request.args:
        query += "name LIKE %s AND"
        vals.append("%" + request.args["name"] + "%")

    if "position" in request.args:
        query += "position = %s AND"
        vals.append(request.args["position"])

    if "team" in request.args:
        query += "team = %s AND"
        vals.append(request.args["team"].upper())

    if "year" in request.args:
        query += "year = %s AND"
        vals.append(request.args["year"])

    # remove the last 'AND' and add terminating semicolon
    query = query[:-4] + ";"
    cursor.execute(query, vals)
    results = cursor.fetchall()

    return jsonify(results)