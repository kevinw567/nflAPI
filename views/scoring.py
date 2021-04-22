from flask import Blueprint, jsonify, request
from views.passing import cursor
import const as constants

scoring = Blueprint("scoring", __name__, url_prefix = "/stats/nfl/")

@scoring.route("scoring", methods = ["GET"])
def get_scoring():
    select = constants.SELECT
    query = constants.SELECT_SCORING
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

    if "rushtd" in request.args:
        select += constants.SCORING_COLUMNS.get("rushtd") + ", "
        if any (sym in request.args["rushtd"] for sym in constants.syms):
            query += "rushingTD " 
            query += request.args["rushtd"][:1] 
            query += " %s AND "
            vals.append(request.args["rushtd"][1:])

        else:
            query += "rushingTD = %s AND"
            vals.append(request.args["rushtd"])

    if "rectd" in request.args:
        select += constants.SCORING_COLUMNS.get("rectd") + ", "
        if any (sym in request.args["rectd"] for sym in constants.syms):
            query += "receivingTD "
            query += request.args["rectd"][:1] + " %s AND "
            vals.append(request.args["rectd"][1:])

        else:
            query += "receivingTD = %s AND"
            vals.append(request.args["rectd"])

    if "prettd" in request.args:
        select += constants.SCORING_COLUMNS.get("prettd") + ", "
        if any (sym in request.args["prettd"] for sym in constants.syms):
            query += "punt_returnTD " 
            query += request.args["prettd"][:1] 
            query += " %s AND "
            vals.append(request.args["prettd"][1:])

        else:
            query += "punt_returnTD = %s AND"
            vals.append(request.args["prettd"])

    if "korettd" in request.args:
        select += constants.SCORING_COLUMNS.get("korettd") + ", "
        if any (sym in request.args["korettd"] for sym in constants.syms):
            query += "kick_returnTD " 
            query += request.args["korettd"][:1] 
            query += " %s AND "
            vals.append(request.args["korettd"][1:])

        else:
            query += "kick_returnTD = %s AND"
            vals.append(request.args["korettd"])

    if "fmbltd" in request.args:
        select += constants.SCORING_COLUMNS.get("fmbltd") + ", "
        if any (sym in request.args["fmbltd"] for sym in constants.syms):
            query += "fumbleTD " 
            query += request.args["fmbltd"][:1] 
            query += " %s AND "
            vals.append(request.args["fmbltd"][1:])

        else:
            query += "fumbleTD = %s AND"
            vals.append(request.args["fmbltd"])

    if "inttd" in request.args:
        select += constants.SCORING_COLUMNS.get("inttd") + ", "
        if any (sym in request.args["inttd"] for sym in constants.syms):
            query += "interceptionTD " 
            query += request.args["inttd"][:1] 
            query += " %s AND "
            vals.append(request.args["inttd"][1:])

        else:
            query += "interceptionTD = %s AND"
            vals.append(request.args["inttd"])

    if "othertd" in request.args:
        select += constants.SCORING_COLUMNS.get("othertd") + ", "
        if any (sym in request.args["othertd"] for sym in constants.syms):
            query += "otherTD " 
            query += request.args["othertd"][:1] 
            query += " %s AND "
            vals.append(request.args["othertd"][1:])

        else:
            query += "otherTD = %s AND"
            vals.append(request.args["othertd"])

    if "alltd" in request.args:
        select += constants.SCORING_COLUMNS.get("alltd") + ", "
        if any (sym in request.args["alltd"] for sym in constants.syms):
            query += "allTD " 
            query += request.args["alltd"][:1] 
            query += " %s AND "
            vals.append(request.args["alltd"][1:])

        else:
            query += "allTD = %s AND"
            vals.append(request.args["alltd"])

    if "2pa" in request.args:
        select += constants.SCORING_COLUMNS.get("2pa") + ", "
        if any (sym in request.args["2pa"] for sym in constants.syms):
            query += "twoPA " 
            query += request.args["2pa"][:1] 
            query += " %s AND "
            vals.append(request.args["2pa"][1:])

        else:
            query += "twoPA = %s AND"
            vals.append(request.args["2pa"])

    if "2pm" in request.args:
        select += constants.SCORING_COLUMNS.get("2pm") + ", "
        if any (sym in request.args["2pm"] for sym in constants.syms):
            query += "twoPM " 
            query += request.args["2pm"][:1] 
            query += " %s AND "
            vals.append(request.args["2pm"][1:])

        else:
            query += "twoPM = %s AND"
            vals.append(request.args["2pm"])

    if "xpa" in request.args:
        select += constants.SCORING_COLUMNS.get("xpa") + ", "
        if any (sym in request.args["xpa"] for sym in constants.syms):
            query += "XPA " 
            query += request.args["xpa"][:1] 
            query += " %s AND "
            vals.append(request.args["xpa"][1:])

        else:
            query += "XPA = %s AND"
            vals.append(request.args["xpa"])

    if "xpm" in request.args:
        select += constants.SCORING_COLUMNS.get("xpm") + ", "
        if any (sym in request.args["xpm"] for sym in constants.syms):
            query += "XPM " 
            query += request.args["xpm"][:1] 
            query += " %s AND "
            vals.append(request.args["xpm"][1:])

        else:
            query += "XPM = %s AND"
            vals.append(request.args["xpm"])

    if "fga" in request.args:
        select += constants.SCORING_COLUMNS.get("fga") + ", "
        if any (sym in request.args["fga"] for sym in constants.syms):
            query += "FGA " 
            query += request.args["fga"][:1] 
            query += " %s AND "
            vals.append(request.args["fga"][1:])

        else:
            query += "FGA = %s AND"
            vals.append(request.args["fga"])

    if "fgm" in request.args:
        select += constants.SCORING_COLUMNS.get("fgm") + ", "
        if any (sym in request.args["fgm"] for sym in constants.syms):
            query += "FGzzm " 
            query += request.args["fgm"][:1] 
            query += " %s AND "
            vals.append(request.args["fgm"][1:])

        else:
            query += "FGM = %s AND"
            vals.append(request.args["fgm"])

    if "sfty" in request.args:
        select += constants.SCORING_COLUMNS.get("sfty") + ", "
        if any (sym in request.args["sfty"] for sym in constants.syms):
            query += "Sfty " 
            query += request.args["sfty"][:1] 
            query += " %s AND "
            vals.append(request.args["sfty"][1:])

        else:
            query += "Sfty = %s AND"
            vals.append(request.args["sfty"])

    if "pts" in request.args:
        select += constants.SCORING_COLUMNS.get("pts") + ", "
        if any (sym in request.args["pts"] for sym in constants.syms):
            query += "points " 
            query += request.args["pts"][:1] 
            query += " %s AND "
            vals.append(request.args["pts"][1:])

        else:
            query += "points = %s AND"
            vals.append(request.args["pts"])

    if "ppg" in request.args:
        select += constants.SCORING_COLUMNS.get("ppg") + ", "
        if any (sym in request.args["ppg"] for sym in constants.syms):
            query += "points_per_game " 
            query += request.args["ppg"][:1] 
            query += " %s AND "
            vals.append(request.args["ppg"][1:])

        else:
            query += "points_per_game = %s AND"
            vals.append(request.args["ppg"])

    select = select[:-2]
    query = query[:-4]

    if "orderby" in request.args:
        query += "ORDER BY "
        col = constants.SCORING_COLUMNS.get(request.args["orderby"])
        query += col + " DESC"

    if "order" in request.args and request.args["order"] == "asc":
        query = query[:-4]

    query += ";"
    print(select + query)
    print(vals)
    cursor.execute(select + query, vals)
    results = cursor.fetchall()

    return jsonify(results)