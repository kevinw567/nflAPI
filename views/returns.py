from flask import Blueprint, jsonify, request
from views.passing import cursor
import const as constants

returns = Blueprint("returns", __name__, url_prefix = "/stats/nfl/")

@returns.route("returns", methods = ["GET"])
def get_returns():
    select = constants.SELECT
    query = constants.SELECT_RETURNS
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

    if "prets" in request.args:
        select += constants.RETURNS_COLUMNS.get("prets") + ", "
        if any (sym in request.args["prets"] for sym in constants.syms):
            query += "punt_returns " 
            query += request.args["prets"][:1] 
            query += " %s AND "
            vals.append(request.args["prets"][1:])

        else:
            query += "punt_returns= %s "
            vals.append(request.args["pntrets"])

    if "pretyds" in request.args:
        select += constants.RETURNS_COLUMNS.get("pretyds") + ", "
        if any (sym in request.args["pretyds"] for sym in constants.syms):
            query += "punt_return_yards " 
            query += request.args["pretyds"][:1] 
            query += " %s AND "
            vals.append(request.args["pretyds"][1:])

        else:
            query += "punt_return_yards= %s "
            vals.append(request.args["pretyds"])

    if "prettds" in request.args:
        select += constants.RETURNS_COLUMNS.get("prettds") + ", "
        if any (sym in request.args["prettds"] for sym in constants.syms):
            query += "punt_return_tds " 
            query += request.args["prettds"][:1] 
            query += " %s AND "
            vals.append(request.args["prettds"][1:])

        else:
            query += "punt_return_tds = %s "
            vals.append(request.args["prettds"])

    if "pretlng" in request.args:
        select += constants.RETURNS_COLUMNS.get("pretlng") + ", "
        if any (sym in request.args["pretlng"] for sym in constants.syms):
            query += "long_punt_return " 
            query += request.args["pretyds"][:1] 
            query += " %s AND "
            vals.append(request.args["pretyds"][1:])

        else:
            query += "punt_returns= %s AND"
            vals.append(request.args["pretyds "])

    if "yppr" in request.args:
        select += constants.RETURNS_COLUMNS.get("yppr") + ", "
        if any (sym in request.args["yppr"] for sym in constants.syms):
            query += "yards_per_punt_return " 
            query += request.args["yppr"][:1] 
            query += " %s AND "
            vals.append(request.args["yppr"][1:])

        else:
            query += "yards_per_punt_return = %s AND"
            vals.append(request.args["yppr"])

    if "koret" in request.args:
        select += constants.RETURNS_COLUMNS.get("koret") + ", "
        if any (sym in request.args["koret"] for sym in constants.syms):
            query += "kickoff_returns " 
            query += request.args["koret"][:1] 
            query += " %s AND "
            vals.append(request.args["koret"][1:])

        else:
            query += "kickoff_returns = %s AND"
            vals.append(request.args["koret"])

    if "koretyds" in request.args:
        select += constants.RETURNS_COLUMNS.get("koretyds") + ", "
        if any (sym in request.args["koretyds"] for sym in constants.syms):
            query += "kickoff_return_yards " 
            query += request.args["koretyds"][:1] 
            query += " %s AND "
            vals.append(request.args["koretyds"][1:])

        else:
            query += "kickoff_return_yards = %s AND"
            vals.append(request.args["koretyds"])

    if "korettds" in request.args:
        select += constants.RETURNS_COLUMNS.get("korettds") + ", "
        if any (sym in request.args["korettds"] for sym in constants.syms):
            query += "kickoff_return_tds " 
            query += request.args["korettds"][:1] 
            query += " %s AND "
            vals.append(request.args["korettds"][1:])

        else:
            query += "kickoff_return_tds = %s AND"
            vals.append(request.args["korettds"])

    if "koretlng" in request.args:
        select += constants.RETURNS_COLUMNS.get("koretlng") + ", "
        if any (sym in request.args["koretlng"] for sym in constants.syms):
            query += "long_kickoff_return " 
            query += request.args["koretlng"][:1] 
            query += " %s AND "
            vals.append(request.args["koretlng"][1:])

        else:
            query += "long_kickoff_return = %s AND"
            vals.append(request.args["koretlng"])

    if "ypkoret" in request.args:
        select += constants.RETURNS_COLUMNS.get("ypkoret") + ", "
        if any (sym in request.args["ypkoret"] for sym in constants.syms):
            query += "yards_per_kickoff_return " 
            query += request.args["ypkoret"][:1] 
            query += " %s AND "
            vals.append(request.args["ypkoret"][1:])

        else:
            query += "yards_per_kickoff_return = %s AND"
            vals.append(request.args["ypkoret"])

    if "apyds" in request.args:
        select += constants.RETURNS_COLUMNS.get("apyds") + ", "
        if any (sym in request.args["apyds"] for sym in constants.syms):
            query += "all_purpose_yards " 
            query += request.args["apyds"][:1] 
            query += " %s AND "
            vals.append(request.args["apyds"][1:])

        else:
            query += "all_purpose_yards = %s AND"
            vals.append(request.args["apyds"])

    select = select[:-2]
    query = query[:-4]

    if "orderby" in request.args:
        query += "ORDER BY "
        col = constants.RETURNS_COLUMNS.get(request.args["orderby"])
        query += col + " DESC"

    if "order" in request.args and request.args["order"] == "asc":
        query = query[:-4]

    query += ";"
    print(select + query)
    print(vals)
    cursor.execute(select + query, vals)
    results = cursor.fetchall()

    return jsonify(results)