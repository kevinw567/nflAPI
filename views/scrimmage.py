from flask import Blueprint, jsonify, request
from views.passing import cursor
import const as constants

scrimmage = Blueprint("scrimmage", __name__, url_prefix = "/stats/nfl/")

@scrimmage.route("scrimmage", methods = ["GET"])
def get_scrimmage():
    select = constants.SELECT
    query = constants.SELECT_SCRIMMAGE
    vals = []
    if "name" in request.args:
        query += "name LIKE %s AND "
        vals.append("%" + request.args["name"] + "%")

    # if '!' is in the position argument, lookup all positions except the passed argument(s)
    if "pos" in request.args:
        if any (sym in request.args["pos"] for sym in ("!")):
            query += """position != %s AND """
            vals.append(request.args["pos"][1:].upper())

        else:
            query += """position = %s AND """
            vals.append(request.args["pos"])

    if "team" in request.args:
        query += "team LIKE %s AND "
        vals.append("%" + request.args["team"] + "%")

    if "tch" in request.args:
        select += constants.SCRIMMAGE_COLUMNS.get("tch") + ", "
        if any (sym in request.args["tch"] for sym in constants.syms):
            query += """touches """
            query += request.args["tch"][:1]
            query += """ %s AND """
            vals.append(request.args["tch"][1:])

        else:
            query += """touches = %s AND """
            vals.append(request.args["tch"])

    if "ypt" in request.args:
        select += constants.SCRIMMAGE_COLUMNS.get("ypt") + ", "
        if any (sym in request.args["ypt"] for sym in constants.syms):
            query += """yards_per_touch """
            query += request.args["ypt"][:1]
            query += """ %s AND """
            vals.append(request.args["ypt"][1:])

        else:
            query += """yards_per_touch = %s AND """
            vals.append(request.args["ypt"])

    if "yds" in request.args:
        select += constants.SCRIMMAGE_COLUMNS.get("yds") + ", "
        if any (sym in request.args["yds"] for sym in constants.syms):
            query += """scrimmage_yards """
            query += request.args["yds"][:1]
            query += """ %s AND """
            vals.append(request.args["yds"][1:])

        else:
            query += """scrimmage_yards = %s AND """
            vals.append(request.args["yds"])

    select = select[:-2]
    query = query[:-4]

    if "orderby" in request.args:
        query += "ORDER BY "
        col = constants.SCRIMMAGE_COLUMNS.get(request.args["orderby"])
        query += col + " DESC"

    if "order" in request.args and request.args["order"] == "asc":
        query = query[:-4]

    query += ";"
    print(select + query)
    print(vals)
    cursor.execute(select + query, vals)
    results = cursor.fetchall()

    return jsonify(results)