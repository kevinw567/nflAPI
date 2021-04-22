from flask import Blueprint, jsonify, request
from views.passing import cursor
import const as constants

receiving = Blueprint("receiving", __name__, url_prefix = "/stats/nfl/")

@receiving.route("receiving", methods = ["GET"])
def get_receiving():
    select = constants.SELECT
    query = constants.SELECT_RECEIVING
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
        query += "team = %s AND "
        vals.append(request.args["team"])

    if "tgt" in request.args:
        select += constants.RECEIVING_COLUMNS.get("tgt") + ", "
        if any (sym in request.args["tgt"] for sym in constants.syms):
            query += """targets """
            query += request.args["tgt"][:1]
            query += """ %s AND """
            vals.append(request.args["tgt"][1:])
        
        else:
            query += "targets = %s AND "
            vals.append(request.args["tgt"])

    if "rec" in request.args:
        select += constants.RECEIVING_COLUMNS.get("rec") + ", "
        if any (sym in request.args["rec"] for sym in constants.syms):
            query += """receptions """
            query += request.args["rec"][:1]
            query += """ %s AND """
            vals.append(request.args["rec"][1:])
        
        else:
            query += "receptions = %s AND "
            vals.append(request.args["rec"])
    
    if "ctch%" in request.args:
        select += constants.RECEIVING_COLUMNS.get("ctch%") + ", "
        if any (sym in request.args["ctch%"] for sym in constants.syms):
            query += """catch_percent """
            query += request.args["ctch%"][:1]
            query += """ %s AND """
            vals.append(request.args["ctch%"][1:])
        
        else:
            query += "catch_percent = %s AND "
            vals.append(request.args["ctch%"])

    if "yds" in request.args:
        select += constants.RECEIVING_COLUMNS.get("yds") + ", "
        if any (sym in request.args["yds"] for sym in constants.syms):
            query += """yards """
            query += request.args["yds"][:1]
            query += """ %s AND """
            vals.append(request.args["yds"][1:])
        
        else:
            query += "yards = %s AND "
            vals.append(request.args["yds"])

    if "ypc" in request.args:
        select += constants.RECEIVING_COLUMNS.get("ypc") + ", "
        if any (sym in request.args["ypc"] for sym in constants.syms):
            query += """yards_per_reception """
            query += request.args["ypc"][:1]
            query += """ %s AND """
            vals.append(request.args["ypc"][1:])
        
        else:
            query += "yards_per_reception = %s AND "
            vals.append(request.args["ypc"])

    if "td" in request.args:
        select += constants.RECEIVING_COLUMNS.get("td") + ", "
        if any (sym in request.args["td"] for sym in constants.syms):
            query += """td """
            query += request.args["td"][:1]
            query += """ %s AND """
            vals.append(request.args["td"][1:])
        
        else:
            query += "td = %s AND "
            vals.append(request.args["td"])

    if "fd" in request.args:
        select += constants.RECEIVING_COLUMNS.get("fd") + ", "
        if any (sym in request.args["fd"] for sym in constants.syms):
            query += """first_downs """
            query += request.args["fd"][:1]
            query += """ %s AND """
            vals.append(request.args["fd"][1:])
        
        else:
            query += "first_downs = %s AND "
            vals.append(request.args["fd"])
            
    if "lng" in request.args:
        select += constants.RECEIVING_COLUMNS.get("lng") + ", "
        if any (sym in request.args["lng"] for sym in constants.syms):
            query += """long_reception """
            query += request.args["lng"][:1]
            query += """ %s AND """
            vals.append(request.args["lng"][1:])
        
        else:
            query += "long_reception = %s AND "
            vals.append(request.args["lng"])

    if "ypt" in request.args:
        select += constants.RECEIVING_COLUMNS.get("ypt") + ", "
        if any (sym in request.args["ypt"] for sym in constants.syms):
            query += """yards_per_target """
            query += request.args["ypt"][:1]
            query += """ %s AND """
            vals.append(request.args["ypt"][1:])
        
        else:
            query += "yards_per_target = %s AND "
            vals.append(request.args["ypt"])

    if "rpg" in request.args:
        select += constants.RECEIVING_COLUMNS.get("rpg") + ", "
        if any (sym in request.args["rpg"] for sym in constants.syms):
            query += """receptions_per_game """
            query += request.args["rpg"][:1]
            query += """ %s AND """
            vals.append(request.args["rpg"][1:])
        
        else:
            query += "receptions_per_game = %s AND "
            vals.append(request.args["rpg"])

    if "ypg" in request.args:
        select += constants.RECEIVING_COLUMNS.get("ypg") + ", "
        if any (sym in request.args["ypg"] for sym in constants.syms):
            query += """yards_per_game """
            query += request.args["ypg"][:1]
            query += """ %s AND """
            vals.append(request.args["ypg"][1:])
        
        else:
            query += "yards_per_game = %s AND "
            vals.append(request.args["ypg"])

    if "fmbl" in request.args:
        select += constants.RECEIVING_COLUMNS.get("fmbl") + ", "
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
        col = constants.RECEIVING_COLUMNS.get(request.args["orderby"])
        query += col + " DESC"

    if "order" in request.args and request.args["order"] == "asc":
        query = query[:-4]

    query += ";"
    print(select + query)
    print(vals)
    cursor.execute(select + query, vals)
    results = cursor.fetchall()

    return jsonify(results)