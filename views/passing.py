from flask import Blueprint, jsonify, request
import const as constants
import mysql.connector
from views import db, cursor

passing = Blueprint("passing", __name__, url_prefix = "/stats/nfl/")

@passing.route("passing", methods = ["GET"])
def get_passing():
    print("IN PASSING FUNC")
    select = constants.SELECT
    query = constants.SELECT_PASSING
    vals = []
    if "name" in request.args:
        query += "name LIKE %s AND "
        vals.append("%" + request.args["name"] + "%")

    if "pos" in request.args:
        if any (sym in request.args["pos"] for sym in ("!")):
            query += """position != %s AND """
            vals.append(request.args["pos"][1:])

        else:
            query += """position = %s AND """
            vals.append(request.args["pos"])

    if "cmp" in request.args:
        select += constants.PASSING_COLUMNS.get("cmp") + ", "
        if any (sym in request.args["cmp"] for sym in constants.syms):
            
            query += """completions """
            query += request.args["cmp"][:1]
            query += """ %s AND """
            vals.append(request.args["cmp"][1:])
        
        else:
            query += "completions = %s AND "
            vals.append(request.args["cmp"])

    if "att" in request.args:
        select += constants.PASSING_COLUMNS.get("att") + ", "
        if any (sym in request.args["att"] for sym in constants.syms):
            query += """pass_attempts """
            query += request.args["att"][:1]
            query += """ %s AND """
            vals.append(request.args["att"][1:])
        
        else:
            query += "pass_attempts = %s AND "
            vals.append(request.args["att"])

    if "cmp%" in request.args:
        select += constants.PASSING_COLUMNS.get("cmp%") + ", "
        if any (sym in request.args["cmp%"] for sym in constants.syms):
            query += """completion_percent """
            query += request.args["cmp%"][:1]
            query += """ %s AND """
            vals.append(request.args["cmp%"][1:])
        
        else:
            query += "completion_percent = %s AND "
            vals.append(request.args["cmp%"])
    
    if "yds" in request.args:
        select += constants.PASSING_COLUMNS.get("yds") + ", "
        if any (sym in request.args["yds"] for sym in constants.syms):
            query += """yards """
            query += request.args["yds"][:1]
            query += """ %s AND """
            vals.append(request.args["yds"][1:])
        
        else:
            query += "yards = %s AND "
            vals.append(request.args["yds"])

    if "td" in request.args:
        select += constants.PASSING_COLUMNS.get("td") + ", "
        if any (sym in request.args["td"] for sym in constants.syms):
            query += """TD """
            query += request.args["td"][:1]
            query += """ %s AND """
            vals.append(request.args["td"][1:])
        
        else:
            query += "TD = %s AND "
            vals.append(request.args["td"])

    if "int" in request.args:
        select += constants.PASSING_COLUMNS.get("int") + ", "
        if any (sym in request.args["int"] for sym in constants.syms):
            query += """interceptions """
            query += request.args["int"][:1]
            query += """ %s AND """
            vals.append(request.args["int"][1:])
        
        else:
            query += "interceptions = %s AND "
            vals.append(request.args["int"])

    if "ypg" in request.args:
        select += constants.PASSING_COLUMNS.get("ypg") + ", "
        if any (sym in request.args["ypg"] for sym in constants.syms):
            query += """yards_per_game """
            query += request.args["ypg"][:1]
            query += """ %s AND """
            vals.append(request.args["ypg"][1:])
        
        else:
            query += "yards_per_game = %s AND "
            vals.append(request.args["ypg"])

    if "ypc" in request.args:
        select += constants.PASSING_COLUMNS.get("ypc") + ", "
        if any (sym in request.args["ypc"] for sym in constants.syms):
            query += """yards_per_comp """
            query += request.args["ypc"][:1]
            query += """ %s AND """
            vals.append(request.args["ypc"][1:])
        
        else:
            query += "yards_per_comp = %s AND "
            vals.append(request.args["ypc"])

    if "ypa" in request.args:
        select += constants.PASSING_COLUMNS.get("ypa") + ", "
        if any (sym in request.args["ypa"] for sym in constants.syms):
            query += """yards_per_attempt """
            query += request.args["ypa"][:1]
            query += """ %s AND """
            vals.append(request.args["ypa"][1:])
        
        else:
            query += "yards_per_attempt = %s AND "
            vals.append(request.args["ypa"])

    if "lng" in request.args:
        select += constants.PASSING_COLUMNS.get("lng") + ", "
        if any (sym in request.args["lng"] for sym in constants.syms):
            query += """longest_pass """
            query += request.args["lng"][:1]
            query += """ %s AND """
            vals.append(request.args["lng"][1:])
        
        else:
            query += "longest_pass = %s AND "
            vals.append(request.args["lng"])

    if "rtng" in request.args:
        select += constants.PASSING_COLUMNS.get("rtng") + ", "
        if any (sym in request.args["rtng"] for sym in constants.syms):
            query += """passer_rating """
            query += request.args["rtng"][:1]
            query += """ %s AND """
            vals.append(request.args["rtng"][1:])
        
        else:
            query += "passer_rating = %s AND "
            vals.append(request.args["rtng"])

    if "qbr" in request.args:
        select += constants.PASSING_COLUMNS.get("qbr") + ", "
        if any (sym in request.args["qbr"] for sym in constants.syms):
            query += """qbr """
            query += request.args["qbr"][:1]
            query += """ %s AND """
            vals.append(request.args["qbr"][1:])
        
        else:
            query += "qbr = %s AND "
            vals.append(request.args["qbr"])

    
    select = select[:-2]
    query = query[:-4]

    if "orderby" in request.args:
        query += "ORDER BY "
        col = constants.PASSING_COLUMNS.get(request.args["orderby"])
        query += col + " DESC"

    if "order" in request.args and request.args["order"] == "asc":
        query = query[:-4]

    query += ";"
    print(select + query)
    print(vals)
    cursor.execute(select + query, vals)
    results = cursor.fetchall()
    
    return jsonify(results)