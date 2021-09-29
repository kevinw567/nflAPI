from flask import Blueprint, jsonify, request
from views.passing import cursor
import const as constants

defense = Blueprint("defense", __name__, url_prefix = "/stats/nfl/")

@defense.route("defense", methods = ["GET"])
def get_defense():
    select = constants.SELECT
    query = constants.SELECT_DEFENSE
    vals = []
    if "name" in request.args:
        query += "name LIKE %s AND "
        vals.append("%" + request.args["name"] + "%")
        if len(request.args) == 1 and request.args["name"] is not None:
            select = "SELECT *  "

    # if '!' is in the position argument, lookup all positions except the passed argument(s)
    if "pos" in request.args:
        if any (sym in request.args["pos"] for sym in ("!")):
            query += """position != %s AND """
            vals.append(request.args["pos"][1:].upper())

        else:
            query += """position = %s AND """
            vals.append(request.args["pos"])

    if "year" in request.args:
        query += "year = %s AND"
        vals.append(request.args["year"])

    if "team" in request.args:
        query += "team LIKE %s AND "
        vals.append("%" + request.args["team"] + "%")

    if "int" in request.args:
        select += constants.DEFENSE_COLUMNS.get("int") + ", "
        if any (sym in request.args["int"] for sym in constants.syms):
            query += """interceptions """
            query += request.args["int"][:1]
            query += """ %s AND """
            vals.append(request.args["int"][1:])

        else:
            query += """interceptions = %s AND """
            vals.append(request.args["int"])

    if "intyds" in request.args:
        select += constants.DEFENSE_COLUMNS.get("intyds") + ", "
        if any (sym in request.args["intyds"] for sym in constants.syms):
            query += """interception_yards """
            query += request.args["intyds"][:1]
            query += """ %s AND """
            vals.append(request.args["intyds"][1:])

        else:
            query += """interception_yards = %s AND """
            vals.append(request.args["intyds"])

    if "inttd" in request.args:
        select += constants.DEFENSE_COLUMNS.get("inttd") + ", "
        if any (sym in request.args["inttd"] for sym in constants.syms):
            query += """interception_tds """
            query += request.args["inttd"][:1]
            query += """ %s AND """
            vals.append(request.args["inttd"][1:])

        else:
            query += """interception_tds = %s AND """
            vals.append(request.args["inttd"])

    if "intlng" in request.args:
        select += constants.DEFENSE_COLUMNS.get("intlng") + ", "
        if any (sym in request.args["intlng"] for sym in constants.syms):
            query += """long_interception_return """
            query += request.args["intlng"][:1]
            query += """ %s AND """
            vals.append(request.args["intlng"][1:])

        else:
            query += """long_interception_return = %s AND """
            vals.append(request.args["intlng"])

    if "pdef" in request.args:
        select += constants.DEFENSE_COLUMNS.get("pdef") + ", "
        if any (sym in request.args["pdef"] for sym in constants.syms):
            query += """passes_defensed """
            query += request.args["pdef"][:1]
            query += """ %s AND """
            vals.append(request.args["pdef"][1:])

        else:
            query += """passes_defensed = %s AND """
            vals.append(request.args["pdef"])

    if "ffmbl" in request.args:
        select += constants.DEFENSE_COLUMNS.get("ffmbl") + ", "
        if any (sym in request.args["ffmbl"] for sym in constants.syms):
            query += """forced_fumbles """
            query += request.args["ffmbl"][:1]
            query += """ %s AND """
            vals.append(request.args["ffmbl"][1:])

        else:
            query += """forced_fumbles = %s AND """
            vals.append(request.args["ffmbl"])

    if "fmblrec" in request.args:
        select += constants.DEFENSE_COLUMNS.get("fmblrec") + ", "
        if any (sym in request.args["fmblrec"] for sym in constants.syms):
            query += """fumble_recoveries """
            query += request.args["fmblrec"][:1]
            query += """ %s AND """
            vals.append(request.args["fmblrec"][1:])

        else:
            query += """fumble_recoveries = %s AND """
            vals.append(request.args["fmblrec"])

    if "fmblyds" in request.args:
        select += constants.DEFENSE_COLUMNS.get("fmblyds") + ", "
        if any (sym in request.args["fmblyds"] for sym in constants.syms):
            query += """fumble_return_yards = %s """
            query += request.args["fmblyds"][:1]
            query += """ %s AND """
            vals.append(request.args["fmblyds"][1:])

        else:
            query += """fumble_return_yards = %s AND """
            vals.append(request.args["fmblyds"])

    if "fmbltd" in request.args:
        select += constants.DEFENSE_COLUMNS.get("fmbltd") + ", "
        if any (sym in request.args["fmbltd"] for sym in constants.syms):
            query += """fumble_return_tds """
            query += request.args["fmbltd"][:1]
            query += """ %s AND """
            vals.append(request.args["fmbltd"][1:])

        else:
            query += """fumble_return_tds = %s AND """
            vals.append(request.args["fmbltd"])

    if "sck" in request.args:
        select += constants.DEFENSE_COLUMNS.get("sck") + ", "
        if any (sym in request.args["sck"] for sym in constants.syms):
            query += """sacks """
            query += request.args["sck"][:1]
            query += """ %s AND """
            vals.append(request.args["sck"][1:])

        else:
            query += """sacks = %s AND """
            vals.append(request.args["sck"])

    if "tkls" in request.args:
        select += constants.DEFENSE_COLUMNS.get("tkls") + ", "
        if any (sym in request.args["tkls"] for sym in constants.syms):
            query += """comb_tackles """
            query += request.args["tkls"][:1]
            query += """ %s AND """
            vals.append(request.args["tkls"][1:])

        else:
            query += """comb_tackles = %s AND """
            vals.append(request.args["tkls"])

    if "solotkl" in request.args:
        select += constants.DEFENSE_COLUMNS.get("solotkl") + ", "
        if any (sym in request.args["solotkl"] for sym in constants.syms):
            query += """solo_tackles """
            query += request.args["solotkl"][:1]
            query += """ %s AND """
            vals.append(request.args["solotkl"][1:])

        else:
            query += """solo_tackles = %s AND """
            vals.append(request.args["solotkl"])

    if "assttkl" in request.args:
        select += constants.DEFENSE_COLUMNS.get("assttkl") + ", "
        if any (sym in request.args["assttkl"] for sym in constants.syms):
            query += """assisted_tackles """
            query += request.args["assttkl"][:1]
            query += """ %s AND """
            vals.append(request.args["assttkl"][1:])

        else:
            query += """assited_tackles = %s AND """
            vals.append(request.args["assttkl"])

    if "tfl" in request.args:
        select += constants.DEFENSE_COLUMNS.get("tfl") + ", "
        if any (sym in request.args["tfl"] for sym in constants.syms):
            query += """tackles_for_loss """
            query += request.args["tfl"][:1]
            query += """ %s AND """
            vals.append(request.args["tfl"][1:])

        else:
            query += """tackles_for_loss = %s AND """
            vals.append(request.args["tfl"])

    if "hits" in request.args:
        select += constants.DEFENSE_COLUMNS.get("hits") + ", "
        if any (sym in request.args["hits"] for sym in constants.syms):
            query += """qbhits """
            query += request.args["hits"][:1]
            query += """ %s AND """
            vals.append(request.args["hits"][1:])

        else:
            query += """qbhits = %s AND """
            vals.append(request.args["hits"])

    if "sfty" in request.args:
        select += constants.DEFENSE_COLUMNS.get("sfty") + ", "
        if any (sym in request.args["sfty"] for sym in constants.syms):
            query += """safetys """
            query += request.args["sfty"][:1]
            query += """ %s AND """
            vals.append(request.args["sfty"][1:])

        else:
            query += """safetys = %s AND """
            vals.append(request.args["sfty"])

    select = select[:-2]
    query = query[:-4]

    if "orderby" in request.args:
        query += "ORDER BY "
        col = constants.DEFENSE_COLUMNS.get(request.args["orderby"])
        query += col + " DESC"

    if "order" in request.args and request.args["order"] == "asc":
        query = query[:-4]

    query += ";"
    print(select + query)
    print(vals)
    cursor.execute(select + query, vals)
    results = cursor.fetchall()

    return jsonify(results)