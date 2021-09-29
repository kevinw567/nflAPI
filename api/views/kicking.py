from flask import Blueprint, jsonify, request
from views.passing import cursor
import const as constants

kicking = Blueprint("kicking", __name__, url_prefix = "/stats/nfl/")

@kicking.route("kicking", methods = ["GET"])
def get_kicking():
    select = constants.SELECT
    query = constants.SELECT_KICKING
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

    if "fga" in request.args:
        select += constants.KICKING_COLUMNS.get("fga") + ", "
        if any (sym in request.args["fga"] for sym in constants.syms):
            query += "FGA " 
            query += request.args["fga"][:1] 
            query += " %s AND "
            vals.append(request.args["fga"][1:])

        else:
            query += "FGA = %s"
            vals.append(request.args["fga"])

    if "fgm" in request.args:
        select += constants.KICKING_COLUMNS.get("fgm") + ", "
        if any (sym in request.args["fgm"] for sym in constants.syms):
            query += "FGM " 
            query += request.args["fgm"][:1] 
            query += " %s AND "
            vals.append(request.args["fgm"][1:])

        else:
            query += "FGM = %s"
            vals.append(request.args["fgm"])

    if "fga19" in request.args:
        select += constants.KICKING_COLUMNS.get("fga19") + ", "
        if any (sym in request.args["fga19"] for sym in constants.syms):
            query += "FGA19 " 
            query += request.args["fga19"][:1] 
            query += " %s AND "
            vals.append(request.args["fga19"][1:])

        else:
            query += "FGA19 = %s"
            vals.append(request.args["fga19"])

    if "fgm19" in request.args:
        select += constants.KICKING_COLUMNS.get("fgm19") + ", "
        if any (sym in request.args["fgm19"] for sym in constants.syms):
            query += "FGM19 " 
            query += request.args["fgm19"][:1] 
            query += " %s AND "
            vals.append(request.args["fgm19"][1:])

        else:
            query += "FGM19 = %s"
            vals.append(request.args["fgm19"])

    if "fga29" in request.args:
        select += constants.KICKING_COLUMNS.get("fga29") + ", "
        if any (sym in request.args["fga29"] for sym in constants.syms):
            query += "FGA29 " 
            query += request.args["fga29"][:1] 
            query += " %s AND "
            vals.append(request.args["fga29"][1:])

        else:
            query += "FGA29 = %s"
            vals.append(request.args["fga29"])

    if "fgm29" in request.args:
        select += constants.KICKING_COLUMNS.get("fgm29") + ", "
        if any (sym in request.args["fgm29"] for sym in constants.syms):
            query += "FGM29 " 
            query += request.args["fgm29"][:1] 
            query += " %s AND "
            vals.append(request.args["fgm29"][1:])

        else:
            query += "FGM29 = %s"
            vals.append(request.args["fgm29"])
    
    if "fga39" in request.args:
        select += constants.KICKING_COLUMNS.get("fga39") + ", "
        if any (sym in request.args["fga39"] for sym in constants.syms):
            query += "FGA39 " 
            query += request.args["fga39"][:1] 
            query += " %s AND "
            vals.append(request.args["fga39"][1:])

        else:
            query += "FGA39 = %s"
            vals.append(request.args["fga39"])

    if "fgm39" in request.args:
        select += constants.KICKING_COLUMNS.get("fgm39") + ", "
        if any (sym in request.args["fgm39"] for sym in constants.syms):
            query += "FGM39 " 
            query += request.args["fgm39"][:1] 
            query += " %s AND "
            vals.append(request.args["fgm39"][1:])

        else:
            query += "FGM39 = %s"
            vals.append(request.args["fgm39"])

    if "fga49" in request.args:
        select += constants.KICKING_COLUMNS.get("fga49") + ", "
        if any (sym in request.args["fga49"] for sym in constants.syms):
            query += "FGA49 " 
            query += request.args["fga49"][:1] 
            query += " %s AND "
            vals.append(request.args["fga49"][1:])

        else:
            query += "FGA49 = %s"
            vals.append(request.args["fga49"])

    if "fgm49" in request.args:
        select += constants.KICKING_COLUMNS.get("fgm49") + ", "
        if any (sym in request.args["fgm49"] for sym in constants.syms):
            query += "FGM49 " 
            query += request.args["fgm49"][:1] 
            query += " %s AND "
            vals.append(request.args["fgm49"][1:])

        else:
            query += "FGM49 = %s"
            vals.append(request.args["fgm49"])

    if "fga50" in request.args:
        select += constants.KICKING_COLUMNS.get("fga50") + ", "
        if any (sym in request.args["fga50"] for sym in constants.syms):
            query += "FGA50 " 
            query += request.args["fga50"][:1] 
            query += " %s AND "
            vals.append(request.args["fga50"][1:])

        else:
            query += "FGA50 = %s"
            vals.append(request.args["fga50"])

    if "fgm50" in request.args:
        select += constants.KICKING_COLUMNS.get("fgm50") + ", "
        if any (sym in request.args["fgm50"] for sym in constants.syms):
            query += "FGM50 " 
            query += request.args["fgm50"][:1] 
            query += " %s AND "
            vals.append(request.args["fgm50"][1:])

        else:
            query += "FGM50 = %s"
            vals.append(request.args["fgm50"])

    if "fglng" in request.args:
        select += constants.KICKING_COLUMNS.get("fglng") + ", "
        if any (sym in request.args["fglng"] for sym in constants.syms):
            query += "FGLong " 
            query += request.args["fglng"][:1] 
            query += " %s AND "
            vals.append(request.args["fglng"][1:])

        else:
            query += "FGALong = %s"
            vals.append(request.args["fglng"])

    if "fg%" in request.args:
        select += constants.KICKING_COLUMNS.get("fg%") + ", "
        if any (sym in request.args["fga%"] for sym in constants.syms):
            query += "FGPercent " 
            query += request.args["fg%"][:1] 
            query += " %s AND "
            vals.append(request.args["fg%"][1:])

        else:
            query += "FGAPercent = %s"
            vals.append(request.args["fg%"])

    if "xpa" in request.args:
        select += constants.KICKING_COLUMNS.get("xpa") + ", "
        if any (sym in request.args["xpa"] for sym in constants.syms):
            query += "XPA " 
            query += request.args["xpa"][:1] 
            query += " %s AND "
            vals.append(request.args["xpa"][1:])

        else:
            query += "XPA = %s"
            vals.append(request.args["xpa"])

    if "xpm" in request.args:
        select += constants.KICKING_COLUMNS.get("xpm") + ", "
        if any (sym in request.args["xpm"] for sym in constants.syms):
            query += "XPM " 
            query += request.args["xpm"][:1] 
            query += " %s AND "
            vals.append(request.args["xpm"][1:])

        else:
            query += "XPM = %s"
            vals.append(request.args["xpm"])

    if "xp%" in request.args:
        select += constants.KICKING_COLUMNS.get("xp%") + ", "
        if any (sym in request.args["xp%"] for sym in constants.syms):
            query += "XPPercent " 
            query += request.args["xp%"][:1] 
            query += " %s AND "
            vals.append(request.args["xp%"][1:])

        else:
            query += "XPPercent = %s"
            vals.append(request.args["xp%"])

    if "ko" in request.args:
        select += constants.KICKING_COLUMNS.get("ko") + ", "
        if any (sym in request.args["ko"] for sym in constants.syms):
            query += "KO " 
            query += request.args["ko"][:1] 
            query += " %s AND "
            vals.append(request.args["ko"][1:])

        else:
            query += "KO = %s"
            vals.append(request.args["ko"])

    if "koyds" in request.args:
        select += constants.KICKING_COLUMNS.get("koyds") + ", "
        if any (sym in request.args["koyds"] for sym in constants.syms):
            query += "KOYds " 
            query += request.args["koyds"][:1] 
            query += " %s AND "
            vals.append(request.args["koyds"][1:])

        else:
            query += "KOYds = %s"
            vals.append(request.args["koyds"])

    if "tb" in request.args:
        select += constants.KICKING_COLUMNS.get("tb") + ", "
        if any (sym in request.args["tb"] for sym in constants.syms):
            query += "TB " 
            query += request.args["tb"][:1] 
            query += " %s AND "
            vals.append(request.args["tb"][1:])

        else:
            query += "TB = %s"
            vals.append(request.args["tb"])

    if "tb%" in request.args:
        select += constants.KICKING_COLUMNS.get("tb%") + ", "
        if any (sym in request.args["tb%"] for sym in constants.syms):
            query += "TBPercent " 
            query += request.args["tb%"][:1] 
            query += " %s AND "
            vals.append(request.args["tb%"][1:])

        else:
            query += "TBPercent = %s"
            vals.append(request.args["tb%"])

    if "koavg" in request.args:
        select += constants.KICKING_COLUMNS.get("koavg") + ", "
        if any (sym in request.args["koavg"] for sym in constants.syms):
            query += "KOAvg " 
            query += request.args["koavg"][:1] 
            query += " %s AND "
            vals.append(request.args["koavg"][1:])

        else:
            query += "KOAvg = %s"
            vals.append(request.args["koavg"])
    
    if "pnts" in request.args:
        select += constants.KICKING_COLUMNS.get("pnts") + ", "
        if any (sym in request.args["pnts"] for sym in constants.syms):
            query += "Pnts " 
            query += request.args["pnts"][:1] 
            query += " %s AND "
            vals.append(request.args["pnts"][1:])

        else:
            query += "Pnts = %s"
            vals.append(request.args["pnts"])

    if "pntavg" in request.args:
        select += constants.KICKING_COLUMNS.get("pntavg") + ", "
        if any (sym in request.args["pntavg"] for sym in constants.syms):
            query += "PntAvg " 
            query += request.args["pntsavg"][:1] 
            query += " %s AND "
            vals.append(request.args["pntsavg"][1:])

        else:
            query += "PntAvg = %s"
            vals.append(request.args["pntsavg"])

    if "pntlng" in request.args:
        select += constants.KICKING_COLUMNS.get("pntlng") + ", "
        if any (sym in request.args["pntlng"] for sym in constants.syms):
            query += "PntLong " 
            query += request.args["pntlng"][:1] 
            query += " %s AND "
            vals.append(request.args["pntlng"][1:])

        else:
            query += "PntLong = %s"
            vals.append(request.args["pntlng"])

    if "blck" in request.args:
        select += constants.KICKING_COLUMNS.get("blck") + ", "
        if any (sym in request.args["blck"] for sym in constants.syms):
            query += "Blocked " 
            query += request.args["blck"][:1] 
            query += " %s AND "
            vals.append(request.args["blck"][1:])

        else:
            query += "Blocked = %s"
            vals.append(request.args["blck"])

    if "ypp" in request.args:
        select += constants.KICKING_COLUMNS.get("ypp") + ", "
        if any (sym in request.args["ypp"] for sym in constants.syms):
            query += "YdsPerPnt " 
            query += request.args["ypp"][:1] 
            query += " %s AND "
            vals.append(request.args["ypp"][1:])

        else:
            query += "YdsPerPnt = %s"
            vals.append(request.args["ypp"])

    select = select[:-2]
    query = query[:-4]

    if "orderby" in request.args:
        query += "ORDER BY "
        col = constants.KICKING_COLUMNS.get(request.args["orderby"])
        query += col + " DESC"

    if "order" in request.args and request.args["order"] == "asc":
        query = query[:-4]

    query += ";"
    print(select + query)
    print(vals)
    cursor.execute(select + query, vals)
    results = cursor.fetchall()

    return jsonify(results)