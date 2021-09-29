from flask import Blueprint, jsonify, request
from views.passing import cursor
import const as constants

rushing = Blueprint("rushing", __name__, url_prefix = "/stats/nfl/")

@rushing.route("rushing", methods = ["GET"])
def get_rushing():
    select = constants.SELECT
    query = constants.SELECT_RUSHING
    vals = []
    if "name" in request.args:
        query += "name LIKE %s AND "
        vals.append("%" + request.args["name"] + "%")
        if len(request.args) == 1 and request.args["name"] is not None:
            select = "SELECT *  "

    if "pos" in request.args:
        if any (sym in request.args["pos"] for sym in ("!")):
            query += """position != %s AND """
            vals.append(request.args["pos"][1:].upper())

        else:
            query += """position = %s AND """
            vals.append(request.args["pos"])

    if "team" in request.args:
        query += "team = %s AND "
        vals.append(request.args["team"])

    if "year" in request.args:
        query += "year = %s AND"
        vals.append(request.args["year"])

    if "att" in request.args:
        select += constants.RUSHING_COLUMNS.get("att") + ", "
        if any (sym in request.args["att"] for sym in constants.syms):
            query += """attempts """
            query += request.args["att"][:1]
            query += """ %s AND """
            vals.append(request.args["att"][1:])
        
        else:
            query += "pass_attempts = %s AND "
            vals.append(request.args["att"])
    
    if "yds" in request.args:
        select += constants.RUSHING_COLUMNS.get("yds") + ", "
        if any (sym in request.args["yds"] for sym in constants.syms):
            query += """yards """
            query += request.args["yds"][:1]
            query += """ %s AND """
            vals.append(request.args["yds"][1:])
        
        else:
            query += "yards = %s AND "
            vals.append(request.args["yds"])

    if "td" in request.args:
        select += constants.RUSHING_COLUMNS.get("td") + ", "
        if any (sym in request.args["td"] for sym in constants.syms):
            query += """touchdowns """
            query += request.args["td"][:1]
            query += """ %s AND """
            vals.append(request.args["td"][1:])
        
        else:
            query += "touchdown = %s AND "
            vals.append(request.args["td"])

    if "fd" in request.args:
        select += constants.RUSHING_COLUMNS.get("fd") + ", "
        if any (sym in request.args["fd"] for sym in constants.syms):
            query += """first_downs """
            query += request.args["fd"][:1]
            query += """ %s AND """
            vals.append(request.args["fd"][1:])
        
        else:
            query += "first_downs = %s AND "
            vals.append(request.args["fd"])

    if "lng" in request.args:
        select += constants.RUSHING_COLUMNS.get("lng") + ", "
        if any (sym in request.args["lng"] for sym in constants.syms):
            query += """long_rush """
            query += request.args["lng"][:1]
            query += """ %s AND """
            vals.append(request.args["lng"][1:])

        else:
            query += "long_rush = %s AND "
            vals.append(request.args["lng"])

    if "ypa" in request.args:
        select += constants.RUSHING_COLUMNS.get("ypa") + ", "
        if any (sym in request.args["ypa"] for sym in constants.syms):
            query += """yards_per_attempt """
            query += request.args["ypa"][:1]
            query += """ %s AND """
            vals.append(request.args["ypa"][1:])
    
        else:
            query += "yards_per_attempt = %s AND "
            vals.append(request.args["ypa"])

    if "ypg" in request.args:
        select += constants.RUSHING_COLUMNS.get("ypg") + ", "
        if any (sym in request.args["ypg"] for sym in constants.syms):
            query += """yards_per_game """
            query += request.args["ypg"][:1]
            query += """ %s AND """
            vals.append(request.args["ypg"][1:])
        
        else:
            query += "yards_per_game = %s AND "
            vals.append(request.args["ypg"])

    if "fmbl" in request.args:
        select += constants.RUSHING_COLUMNS.get("fmbl") + ", "
        if any (sym in request.args["fmbl"] for sym in constants.syms):
            query += """fumbles """
            query += request.args["fmbl"][:1]
            query += """ %s AND """
            vals.append(request.args["fmbl"][1:])
        
        else:
            query += "fumbles = %s AND "
            vals.append(request.args["fmbl"])

    select = select[:-2]
    query = query[:-4]

    if "orderby" in request.args:
        query += "ORDER BY "
        col = constants.RUSHING_COLUMNS.get(request.args["orderby"])
        query += col + " DESC"

    if "order" in request.args and request.args["order"] == "asc":
        query = query[:-4]

    query += ";"
    print(select + query)
    print(vals)
    cursor.execute(select + query, vals)
    results = cursor.fetchall()
    
    return jsonify(results)