import flask
import constants
import mysql.connector
from flask import jsonify, request
from mysql.connector import Error

app = flask.Flask(__name__)
app.config["DEBUG"] = True

db = mysql.connector.connect(
    host = app.config["HOST"],
    user = app.config["USER"],
    password = app.config["PASSWORD"],
    database = app.config["DATABASE"]
)

cursor = db.cursor(dictionary = True)

if db:
    print("Connected to database")
    

else:
    print("Unable to connect to database")

@app.route("/", methods = ["GET"])
def home():
    return "<h1> NFL Stats API <h1>"

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

# API endpoints for single category stats
@app.route("/stats/nfl/passing", methods = ["GET"])
def get_passing():
    select = constants.SELECT
    query = constants.SELECT_PASSING
    vals = []
    for param in request.args:
        print(param + request.args[param])

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

@app.route("/stats/nfl/rushing", methods = ["GET"])
def get_rushing():
    select = constants.SELECT
    query = constants.SELECT_RUSHING
    vals = []
    if "name" in request.args:
        query += "name LIKE %s AND "
        vals.append("%" + request.args["name"] + "%")

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

@app.route("/stats/nfl/receiving", methods = ["GET"])
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

@app.route("/stats/nfl/defense", methods = ["GET"])
def get_defense():
    select = constants.SELECT
    query = constants.SELECT_DEFENSE
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



@app.route("/stats/nfl/scrimmage", methods = ["GET"])
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

@app.route("/stats/nfl/kicking", methods = ["GET"])
def get_kicking():
    select = constants.SELECT
    query = constants.SELECT_KICKING
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

@app.route("/stats/nfl/returns", methods = ["GET"])
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

@app.route("/stats/nfl/scoring", methods = ["GET"])
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

app.run()