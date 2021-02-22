import flask
import constants
import mysql.connector
from flask import jsonify, request
from mysql.connector import Error

app = flask.Flask(__name__)
app.config["DEBUG"] = True

db = mysql.connector.connect(
    host = "localhost",
    user = "kevin",
    password = "password",
    database = "nflStats"
)

cursor = db.cursor()

if db:
    print("Connected to database")
    

else:
    print("Unable to connect to database")

@app.route("/", methods = ["GET"])
def home():
    return "<h1> NFL Stats API <h1>"

@app.route("/stats/nfl/players/all", methods = ["GET"])
def get_all_players():
    cursor.execute("SELECT * FROM player_info")
    results = cursor.fetchall()
    
    return jsonify(results)

@app.route("/stats/nfl/players", methods = ["GET"])
def get_players():
    query = "SELECT * from player_info WHERE "
    vals = []
    # formulate query with endpoint arguments
    if "id" in request.args:
        query += "id = %s AND"
        vals.append(request.args["id"])

    if "name" in request.args:
        query += "name = %s AND"
        vals.append(request.args["name"])

    if "position" in request.args:
        query += "position = %s AND"
        vals.append(request.args["position"])

    if "team" in request.args:
        query += "team = %s AND"
        vals.append(request.args["team"])

    # remove the last 'AND' and add terminating semicolon
    query = query[:-4] + ";"
    cursor.execute(query, vals)
    results = cursor.fetchall()

    return jsonify(results)

@app.route("/stats/nfl/passing", methods = ["GET"])
def get_passing():
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
        if any (sym in request.args["cmp"] for sym in constants.syms):
            query += """completions """
            query += request.args["cmp"][:1]
            query += """ %s AND """
            vals.append(request.args["cmp"][1:])
        
        else:
            query += "completions = %s AND "
            vals.append(request.args["cmp"])

    if "att" in request.args:
        if any (sym in request.args["att"] for sym in constants.syms):
            query += """pass_attempts """
            query += request.args["att"][:1]
            query += """ %s AND """
            vals.append(request.args["att"][1:])
        
        else:
            query += "pass_attempts = %s AND "
            vals.append(request.args["att"])

    if "cmpp" in request.args:
        if any (sym in request.args["cmpp"] for sym in constants.syms):
            query += """completion_percent """
            query += request.args["cmpp"][:1]
            query += """ %s AND """
            vals.append(request.args["cmpp"][1:])
        
        else:
            query += "completion_percent = %s AND "
            vals.append(request.args["cmpp"])
    
    if "yds" in request.args:
        if any (sym in request.args["yds"] for sym in constants.syms):
            query += """yards """
            query += request.args["yds"][:1]
            query += """ %s AND """
            vals.append(request.args["yds"][1:])
        
        else:
            query += "yards = %s AND "
            vals.append(request.args["yds"])

    if "td" in request.args:
        if any (sym in request.args["td"] for sym in constants.syms):
            query += """TD """
            query += request.args["ts"][:1]
            query += """ %s AND """
            vals.append(request.args["ts"][1:])
        
        else:
            query += "TD = %s AND "
            vals.append(request.args["td"])

    if "int" in request.args:
        if any (sym in request.args["int"] for sym in constants.syms):
            query += """interceptions """
            query += request.args["int"][:1]
            query += """ %s AND """
            vals.append(request.args["int"][1:])
        
        else:
            query += "interceptions = %s AND "
            vals.append(request.args["int"])

    if "ypg" in request.args:
        if any (sym in request.args["ypg"] for sym in constants.syms):
            query += """yards_per_game """
            query += request.args["ypg"][:1]
            query += """ %s AND """
            vals.append(request.args["ypg"][1:])
        
        else:
            query += "yards_per_game = %s AND "
            vals.append(request.args["ypg"])

    if "ypc" in request.args:
        if any (sym in request.args["ypc"] for sym in constants.syms):
            query += """yards_per_completion """
            query += request.args["ypc"][:1]
            query += """ %s AND """
            vals.append(request.args["ypc"][1:])
        
        else:
            query += "yards_per_completion = %s AND "
            vals.append(request.args["ypc"])

    if "ypa" in request.args:
        if any (sym in request.args["ypa"] for sym in constants.syms):
            query += """yards_per_attempt """
            query += request.args["ypa"][:1]
            query += """ %s AND """
            vals.append(request.args["ypa"][1:])
        
        else:
            query += "yards_per_attempt = %s AND "
            vals.append(request.args["ypa"])

    if "lng" in request.args:
        if any (sym in request.args["lng"] for sym in constants.syms):
            query += """longest_pass """
            query += request.args["lng"][:1]
            query += """ %s AND """
            vals.append(request.args["lng"][1:])
        
        else:
            query += "longest_pass = %s AND "
            vals.append(request.args["lng"])

    if "rtng" in request.args:
        if any (sym in request.args["rtng"] for sym in constants.syms):
            query += """passer_rating """
            query += request.args["rtng"][:1]
            query += """ %s AND """
            vals.append(request.args["rtng"][1:])
        
        else:
            query += "passer_rating = %s AND "
            vals.append(request.args["rtng"])

    if "qbr" in request.args:
        if any (sym in request.args["qbr"] for sym in constants.syms):
            query += """qbr """
            query += request.args["qbr"][:1]
            query += """ %s AND """
            vals.append(request.args["qbr"][1:])
        
        else:
            query += "qbr = %s AND "
            vals.append(request.args["qbr"])

    query = query[:-4]

    if "orderby" in request.args:
        query += "ORDER BY "
        col = constants.PASSING_COLUMNS.get(request.args["orderby"])
        query += col

    if "order" in request.args and request.args["order"] == "desc":
        query += " DESC"

    query += ";"
    print(query)
    print(vals)
    cursor.execute(query, vals)
    results = cursor.fetchall()

    return jsonify(results)

@app.route("/stats/nfl/rushing", methods = ["GET"])
def get_rushing():
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
        if any (sym in request.args["att"] for sym in constants.syms):
            query += """pass_attempts """
            query += request.args["att"][:1]
            query += """ %s AND """
            vals.append(request.args["att"][1:])
        
        else:
            query += "pass_attempts = %s AND "
            vals.append(request.args["att"])
    
    if "yds" in request.args:
        if any (sym in request.args["yds"] for sym in constants.syms):
            query += """yards """
            query += request.args["yds"][:1]
            query += """ %s AND """
            vals.append(request.args["yds"][1:])
        
        else:
            query += "yards = %s AND "
            vals.append(request.args["yds"])

    if "td" in request.args:
        if any (sym in request.args["td"] for sym in constants.syms):
            query += """TD """
            query += request.args["ts"][:1]
            query += """ %s AND """
            vals.append(request.args["ts"][1:])
        
        else:
            query += "TD = %s AND "
            vals.append(request.args["td"])

    if "fd" in request.args:
        if any (sym in request.args["fd"] for sym in constants.syms):
            query += """first_downs """
            query += request.args["int"][:1]
            query += """ %s AND """
            vals.append(request.args["fd"][1:])
        
        else:
            query += "first_downs = %s AND "
            vals.append(request.args["fd"])

    if "lng" in request.args:
        if any (sym in request.args["lng"] for sym in constants.syms):
            query += """long_rush """
            query += request.args["lng"][:1]
            query += """ %s AND """
            vals.append(request.args["lng"])

        else:
            query += "long_rush = %s AND "
            vals.append(request.args["lng"])

    if "ypa" in request.args:
        if any (sym in request.args["ypa"] for sym in constants.syms):
            query += """yards_per_attempt """
            query += request.args["ypa"][:1]
            query += """ %s AND """
            vals.append(request.args["ypa"][1:])
    
        else:
            query += "yards_per_attempt = %s AND "
            vals.append(request.args["ypa"])

    if "ypg" in request.args:
        if any (sym in request.args["ypg"] for sym in constants.syms):
            query += """yards_per_game """
            query += request.args["ypg"][:1]
            query += """ %s AND """
            vals.append(request.args["ypg"][1:])
        
        else:
            query += "yards_per_game = %s AND "
            vals.append(request.args["ypg"])

    if "fmbl" in request.args:
        if any (sym in request.args["fmbl"] for sym in constants.syms):
            query += """fumbles """
            query += request.args["fmbl"][:1]
            query += """ %s AND """
            vals.append(request.args["fmbl"][1:])
        
        else:
            query += "fumbles = %s AND "
            vals.append(request.args["fmbl"])


    query = query[:-4]

    if "orderby" in request.args:
        query += "ORDER BY "
        col = constants.RUSHING_COLUMNS.get(request.args["orderby"])
        query += col + " DESC "

    if "order" in request.args and request.args["order"] == "desc":
        query += " DESC"

    query += ";"
    print(query)
    print(vals)
    cursor.execute(query, vals)
    results = cursor.fetchall()

    return jsonify(results)

@app.route("/stats/nfl/receiving", methods = ["GET"])
def get_receiving():
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
        if any (sym in request.args["tgt"] for sym in constants.syms):
            query += """targets """
            query += request.args["tgt"][:1]
            query += """ %s AND """
            vals.append(request.args["tgt"][1:])
        
        else:
            query += "targets = %s AND "
            vals.append(request.args["tgt"])

    if "rec" in request.args:
        if any (sym in request.args["rec"] for sym in constants.syms):
            query += """receptions """
            query += request.args["rec"][:1]
            query += """ %s AND """
            vals.append(request.args["rec"][1:])
        
        else:
            query += "receptions = %s AND "
            vals.append(request.args["rec"])
    
    if "ctch%" in request.args:
        if any (sym in request.args["ctch%"] for sym in constants.syms):
            query += """catch_percent """
            query += request.args["ctch%"][:1]
            query += """ %s AND """
            vals.append(request.args["ctch%"][1:])
        
        else:
            query += "catch_percent = %s AND "
            vals.append(request.args["ctch%"])

    if "yds" in request.args:
        if any (sym in request.args["yds"] for sym in constants.syms):
            query += """yards """
            query += request.args["yds"][:1]
            query += """ %s AND """
            vals.append(request.args["yds"][1:])
        
        else:
            query += "yards = %s AND "
            vals.append(request.args["yds"])

    if "ypc" in request.args:
        if any (sym in request.args["ypc"] for sym in constants.syms):
            query += """yards_per_reception """
            query += request.args["ypc"][:1]
            query += """ %s AND """
            vals.append(request.args["ypc"][1:])
        
        else:
            query += "yards_per_reception = %s AND "
            vals.append(request.args["ypc"])

    if "td" in request.args:
        if any (sym in request.args["td"] for sym in constants.syms):
            query += """td """
            query += request.args["td"][:1]
            query += """ %s AND """
            vals.append(request.args["td"][1:])
        
        else:
            query += "td = %s AND "
            vals.append(request.args["td"])

    if "fd" in request.args:
        if any (sym in request.args["fd"] for sym in constants.syms):
            query += """first_downs """
            query += request.args["fd"][:1]
            query += """ %s AND """
            vals.append(request.args["fd"][1:])
        
        else:
            query += "first_downs = %s AND "
            vals.append(request.args["fd"])
            
    if "lng" in request.args:
        if any (sym in request.args["lng"] for sym in constants.syms):
            query += """long_reception """
            query += request.args["lng"][:1]
            query += """ %s AND """
            vals.append(request.args["lng"][1:])
        
        else:
            query += "long_reception = %s AND "
            vals.append(request.args["lng"])

    if "ypt" in request.args:
        if any (sym in request.args["ypt"] for sym in constants.syms):
            query += """yards_per_target """
            query += request.args["ypt"][:1]
            query += """ %s AND """
            vals.append(request.args["ypt"][1:])
        
        else:
            query += "yards_per_target = %s AND "
            vals.append(request.args["ypt"])

    if "rpg" in request.args:
        if any (sym in request.args["rpg"] for sym in constants.syms):
            query += """receptions_per_game """
            query += request.args["rpg"][:1]
            query += """ %s AND """
            vals.append(request.args["rpg"][1:])
        
        else:
            query += "receptions_per_game = %s AND "
            vals.append(request.args["rpg"])

    if "ypg" in request.args:
        if any (sym in request.args["ypg"] for sym in constants.syms):
            query += """yards_per_game """
            query += request.args["ypg"][:1]
            query += """ %s AND """
            vals.append(request.args["ypg"][1:])
        
        else:
            query += "yards_per_game = %s AND "
            vals.append(request.args["ypg"])

    if "fmbl" in request.args:
        if any (sym in request.args["fmbl"] for sym in constants.syms):
            query += """fumbles """
            query += request.args["fmbl"][:1]
            query += """ %s AND """
            vals.append(request.args["fmbl"][1:])
        
        else:
            query += "fumbles = %s AND "
            vals.append(request.args["fmbl"])

    query = query[:-4]

    if "orderby" in request.args:
        query += "ORDER BY "
        col = constants.RECEIVING_COLUMNS.get(request.args["orderby"])
        query += col + " DESC "
        vals.append(col)

    if "order" in request.args and request.args["order"] == "desc":
        query += " DESC"

    query += ";"
    print(query)
    print(vals)
    cursor.execute(query, vals)
    results = cursor.fetchall()

    return jsonify(results)

@app.route("/stats/nfl/defense", methods = ["GET"])
def get_defense():
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
        if any (sym in request.args["int"] for sym in constants.syms):
            query += """interceptions """
            query += request.args["int"][:1]
            query += """ %s AND """
            vals.append(request.args["int"][1:])

        else:
            query += """interceptions = %s AND """
            vals.append(request.args["int"])

    if "intyds" in request.args:
        if any (sym in request.args["intyds"] for sym in constants.syms):
            query += """interception_yards """
            query += request.args["intyds"][:1]
            query += """ %s AND """
            vals.append(request.args["intyds"][1:])

        else:
            query += """interception_yards = %s AND """
            vals.append(request.args["intyds"])

    if "inttd" in request.args:
        if any (sym in request.args["inttd"] for sym in constants.syms):
            query += """interception_tds """
            query += request.args["inttd"][:1]
            query += """ %s AND """
            vals.append(request.args["inttd"][1:])

        else:
            query += """interception_tds = %s AND """
            vals.append(request.args["inttd"])

    if "intlng" in request.args:
        if any (sym in request.args["intlng"] for sym in constants.syms):
            query += """long_interception_return """
            query += request.args["intlng"][:1]
            query += """ %s AND """
            vals.append(request.args["intlng"][1:])

        else:
            query += """long_interception_return = %s AND """
            vals.append(request.args["intlng"])

    if "pdef" in request.args:
        if any (sym in request.args["pdef"] for sym in constants.syms):
            query += """passes_defensed """
            query += request.args["pdef"][:1]
            query += """ %s AND """
            vals.append(request.args["pdef"][1:])

        else:
            query += """passes_defensed = %s AND """
            vals.append(request.args["pdef"])

    if "ffmbl" in request.args:
        if any (sym in request.args["ffmbl"] for sym in constants.syms):
            query += """forced_fumbles """
            query += request.args["ffmbl"][:1]
            query += """ %s AND """
            vals.append(request.args["ffmbl"][1:])

        else:
            query += """forced_fumbles = %s AND """
            vals.append(request.args["ffmbl"])

    if "fmblrec" in request.args:
        if any (sym in request.args["fmblrec"] for sym in constants.syms):
            query += """fumble_recoveries """
            query += request.args["fmblrec"][:1]
            query += """ %s AND """
            vals.append(request.args["fmblrec"][1:])

        else:
            query += """fumble_recoveries = %s AND """
            vals.append(request.args["fmblrec"])

    if "fmblyds" in request.args:
        if any (sym in request.args["fmblyds"] for sym in constants.syms):
            query += """fumble_return_yards = %s """
            query += request.args["fmblyds"][:1]
            query += """ %s AND """
            vals.append(request.args["fmblyds"][1:])

        else:
            query += """fumble_return_yards = %s AND """
            vals.append(request.args["fmblyds"])

    if "fmbltd" in request.args:
        if any (sym in request.args["fmbltd"] for sym in constants.syms):
            query += """fumble_return_tds """
            query += request.args["fmbltd"][:1]
            query += """ %s AND """
            vals.append(request.args["fmbltd"][1:])

        else:
            query += """fumble_return_tds = %s AND """
            vals.append(request.args["fmbltd"])

    if "sck" in request.args:
        if any (sym in request.args["sck"] for sym in constants.syms):
            query += """sacks """
            query += request.args["sck"][:1]
            query += """ %s AND """
            vals.append(request.args["sck"][1:])

        else:
            query += """sacks = %s AND """
            vals.append(request.args["sck"])

    if "tkls" in request.args:
        if any (sym in request.args["tkls"] for sym in constants.syms):
            query += """comb_tackles """
            query += request.args["tkls"][:1]
            query += """ %s AND """
            vals.append(request.args["tkls"][1:])

        else:
            query += """comb_tackles = %s AND """
            vals.append(request.args["tkls"])

    if "solotkl" in request.args:
        if any (sym in request.args["solotkl"] for sym in constants.syms):
            query += """solo_tackles """
            query += request.args["solotkl"][:1]
            query += """ %s AND """
            vals.append(request.args["solotkl"][1:])

        else:
            query += """solo_tackles = %s AND """
            vals.append(request.args["solotkl"])

    if "assttkl" in request.args:
        if any (sym in request.args["assttkl"] for sym in constants.syms):
            query += """assisted_tackles """
            query += request.args["assttkl"][:1]
            query += """ %s AND """
            vals.append(request.args["assttkl"][1:])

        else:
            query += """assited_tackles = %s AND """
            vals.append(request.args["assttkl"])

    if "tfl" in request.args:
        if any (sym in request.args["tfl"] for sym in constants.syms):
            query += """tackles_for_loss """
            query += request.args["tfl"][:1]
            query += """ %s AND """
            vals.append(request.args["tfl"][1:])

        else:
            query += """tackles_for_loss = %s AND """
            vals.append(request.args["tfl"])

    if "hits" in request.args:
        if any (sym in request.args["hits"] for sym in constants.syms):
            query += """qbhits """
            query += request.args["hits"][:1]
            query += """ %s AND """
            vals.append(request.args["hits"][1:])

        else:
            query += """qbhits = %s AND """
            vals.append(request.args["hits"])

    if "sfty" in request.args:
        if any (sym in request.args["sfty"] for sym in constants.syms):
            query += """safetys """
            query += request.args["sfty"][:1]
            query += """ %s AND """
            vals.append(request.args["sfty"][1:])

        else:
            query += """safetys = %s AND """
            vals.append(request.args["sfty"])

    query = query[:-4]

    if "orderby" in request.args:
        query += "ORDER BY "
        col = constants.DEFENSE_COLUMNS.get(request.args["orderby"])
        query += col + " DESC "
        vals.append(col)

    if "order" in request.args and request.args["order"] == "desc":
        query += " DESC"

    query += ";"
    print(query)
    print(vals)
    cursor.execute(query, vals)
    results = cursor.fetchall()

    return jsonify(results)



@app.route("/stats/nfl/scrimmage", methods = ["GET"])
def get_scrimmage():
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
        if any (sym in request.args["tch"] for sym in constants.syms):
            query += """touches """
            query += request.args["tch"][:1]
            query += """ %s AND """
            vals.append(request.args["tch"][1:])

        else:
            query += """touches = %s AND """
            vals.append(request.args["tch"])

    if "ypt" in request.args:
        if any (sym in request.args["ypt"] for sym in constants.syms):
            query += """yards_per_touch """
            query += request.args["ypt"][:1]
            query += """ %s AND """
            vals.append(request.args["ypt"][1:])

        else:
            query += """yards_per_touch = %s AND """
            vals.append(request.args["ypt"])

    if "yds" in request.args:
        if any (sym in request.args["yds"] for sym in constants.syms):
            query += """scrimmage_yards """
            query += request.args["yds"][:1]
            query += """ %s AND """
            vals.append(request.args["yds"][1:])

        else:
            query += """scrimmage_yards = %s AND """
            vals.append(request.args["yds"])

    query = query[:-4]

    if "orderby" in request.args:
        query += "ORDER BY "
        col = constants.SCRIMMAGE_COLUMNS.get(request.args["orderby"])
        query += col

    if "order" in request.args and request.args["order"] == "desc":
        query += " DESC"

    query += ";"
    print(query)
    print(vals)
    cursor.execute(query, vals)
    results = cursor.fetchall()

    return jsonify(results)

@app.route("/stats/nfl/kicking", methods = ["GET"])
def get_kicking():
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
        if any (sym in request.args["fga"] for sym in constants.syms):
            query += "FGA " 
            query += request.args["fga"][:1] 
            query += " %s AND "
            vals.append(request.args["fga"][1:])

        else:
            query += "FGA = %s"
            vals.append(request.args["fga"])

    if "fgm" in request.args:
        if any (sym in request.args["fgm"] for sym in constants.syms):
            query += "FGM " 
            query += request.args["fgm"][:1] 
            query += " %s AND "
            vals.append(request.args["fgm"][1:])

        else:
            query += "FGM = %s"
            vals.append(request.args["fgm"])

    if "fga19" in request.args:
        if any (sym in request.args["fga19"] for sym in constants.syms):
            query += "FGA19 " 
            query += request.args["fga19"][:1] 
            query += " %s AND "
            vals.append(request.args["fga19"][1:])

        else:
            query += "FGA19 = %s"
            vals.append(request.args["fga19"])

    if "fgm19" in request.args:
        if any (sym in request.args["fgm19"] for sym in constants.syms):
            query += "FGM19 " 
            query += request.args["fgm19"][:1] 
            query += " %s AND "
            vals.append(request.args["fgm19"][1:])

        else:
            query += "FGM19 = %s"
            vals.append(request.args["fgm19"])

    if "fga29" in request.args:
        if any (sym in request.args["fga29"] for sym in constants.syms):
            query += "FGA29 " 
            query += request.args["fga29"][:1] 
            query += " %s AND "
            vals.append(request.args["fga29"][1:])

        else:
            query += "FGA29 = %s"
            vals.append(request.args["fga29"])

    if "fgm29" in request.args:
        if any (sym in request.args["fgm29"] for sym in constants.syms):
            query += "FGM29 " 
            query += request.args["fgm29"][:1] 
            query += " %s AND "
            vals.append(request.args["fgm29"][1:])

        else:
            query += "FGM29 = %s"
            vals.append(request.args["fgm29"])
    
    if "fga39" in request.args:
        if any (sym in request.args["fga39"] for sym in constants.syms):
            query += "FGA39 " 
            query += request.args["fga39"][:1] 
            query += " %s AND "
            vals.append(request.args["fga39"][1:])

        else:
            query += "FGA39 = %s"
            vals.append(request.args["fga39"])

    if "fgm39" in request.args:
        if any (sym in request.args["fgm39"] for sym in constants.syms):
            query += "FGM39 " 
            query += request.args["fgm39"][:1] 
            query += " %s AND "
            vals.append(request.args["fgm39"][1:])

        else:
            query += "FGM39 = %s"
            vals.append(request.args["fgm39"])

    if "fga49" in request.args:
        if any (sym in request.args["fga49"] for sym in constants.syms):
            query += "FGA49 " 
            query += request.args["fga49"][:1] 
            query += " %s AND "
            vals.append(request.args["fga49"][1:])

        else:
            query += "FGA49 = %s"
            vals.append(request.args["fga49"])

    if "fgm49" in request.args:
        if any (sym in request.args["fgm49"] for sym in constants.syms):
            query += "FGM49 " 
            query += request.args["fgm49"][:1] 
            query += " %s AND "
            vals.append(request.args["fgm49"][1:])

        else:
            query += "FGM49 = %s"
            vals.append(request.args["fgm49"])

    if "fga50" in request.args:
        if any (sym in request.args["fga50"] for sym in constants.syms):
            query += "FGA50 " 
            query += request.args["fga50"][:1] 
            query += " %s AND "
            vals.append(request.args["fga50"][1:])

        else:
            query += "FGA50 = %s"
            vals.append(request.args["fga50"])

    if "fgm50" in request.args:
        if any (sym in request.args["fgm50"] for sym in constants.syms):
            query += "FGM50 " 
            query += request.args["fgm50"][:1] 
            query += " %s AND "
            vals.append(request.args["fgm50"][1:])

        else:
            query += "FGM50 = %s"
            vals.append(request.args["fgm50"])

    if "fglng" in request.args:
        if any (sym in request.args["fglng"] for sym in constants.syms):
            query += "FGLong " 
            query += request.args["fglng"][:1] 
            query += " %s AND "
            vals.append(request.args["fglng"][1:])

        else:
            query += "FGALong = %s"
            vals.append(request.args["fglng"])

    if "fg%" in request.args:
        if any (sym in request.args["fga%"] for sym in constants.syms):
            query += "FGPercent " 
            query += request.args["fg%"][:1] 
            query += " %s AND "
            vals.append(request.args["fg%"][1:])

        else:
            query += "FGAPercent = %s"
            vals.append(request.args["fg%"])

    if "xpa" in request.args:
        if any (sym in request.args["xpa"] for sym in constants.syms):
            query += "XPA " 
            query += request.args["xpa"][:1] 
            query += " %s AND "
            vals.append(request.args["xpa"][1:])

        else:
            query += "XPA = %s"
            vals.append(request.args["xpa"])

    if "xpm" in request.args:
        if any (sym in request.args["xpm"] for sym in constants.syms):
            query += "XPM " 
            query += request.args["xpm"][:1] 
            query += " %s AND "
            vals.append(request.args["xpm"][1:])

        else:
            query += "XPM = %s"
            vals.append(request.args["xpm"])

    if "xp%" in request.args:
        if any (sym in request.args["xp%"] for sym in constants.syms):
            query += "XPPercent " 
            query += request.args["xp%"][:1] 
            query += " %s AND "
            vals.append(request.args["xp%"][1:])

        else:
            query += "XPPercent = %s"
            vals.append(request.args["xp%"])

    if "ko" in request.args:
        if any (sym in request.args["ko"] for sym in constants.syms):
            query += "KO " 
            query += request.args["ko"][:1] 
            query += " %s AND "
            vals.append(request.args["ko"][1:])

        else:
            query += "KO = %s"
            vals.append(request.args["ko"])

    if "koyds" in request.args:
        if any (sym in request.args["koyds"] for sym in constants.syms):
            query += "KOYds " 
            query += request.args["koyds"][:1] 
            query += " %s AND "
            vals.append(request.args["koyds"][1:])

        else:
            query += "KOYds = %s"
            vals.append(request.args["koyds"])

    if "tb" in request.args:
        if any (sym in request.args["tb"] for sym in constants.syms):
            query += "TB " 
            query += request.args["tb"][:1] 
            query += " %s AND "
            vals.append(request.args["tb"][1:])

        else:
            query += "TB = %s"
            vals.append(request.args["tb"])

    if "tb%" in request.args:
        if any (sym in request.args["tb%"] for sym in constants.syms):
            query += "TBPercent " 
            query += request.args["tb%"][:1] 
            query += " %s AND "
            vals.append(request.args["tb%"][1:])

        else:
            query += "TBPercent = %s"
            vals.append(request.args["tb%"])

    if "koavg" in request.args:
        if any (sym in request.args["koavg"] for sym in constants.syms):
            query += "KOAvg " 
            query += request.args["koavg"][:1] 
            query += " %s AND "
            vals.append(request.args["koavg"][1:])

        else:
            query += "KOAvg = %s"
            vals.append(request.args["koavg"])
    
    if "pnts" in request.args:
        if any (sym in request.args["pnts"] for sym in constants.syms):
            query += "Pnts " 
            query += request.args["pnts"][:1] 
            query += " %s AND "
            vals.append(request.args["pnts"][1:])

        else:
            query += "Pnts = %s"
            vals.append(request.args["pnts"])

    if "pntavg" in request.args:
        if any (sym in request.args["pntavg"] for sym in constants.syms):
            query += "PntAvg " 
            query += request.args["pntsavg"][:1] 
            query += " %s AND "
            vals.append(request.args["pntsavg"][1:])

        else:
            query += "PntAvg = %s"
            vals.append(request.args["pntsavg"])

    if "pntlng" in request.args:
        if any (sym in request.args["pntlng"] for sym in constants.syms):
            query += "PntLong " 
            query += request.args["pntlng"][:1] 
            query += " %s AND "
            vals.append(request.args["pntlng"][1:])

        else:
            query += "PntLong = %s"
            vals.append(request.args["pntlng"])

    if "blck" in request.args:
        if any (sym in request.args["blck"] for sym in constants.syms):
            query += "Blocked " 
            query += request.args["blck"][:1] 
            query += " %s AND "
            vals.append(request.args["blck"][1:])

        else:
            query += "Blocked = %s"
            vals.append(request.args["blck"])

    if "ypp" in request.args:
        if any (sym in request.args["ypp"] for sym in constants.syms):
            query += "YdsPerPnt " 
            query += request.args["ypp"][:1] 
            query += " %s AND "
            vals.append(request.args["ypp"][1:])

        else:
            query += "YdsPerPnt = %s"
            vals.append(request.args["ypp"])

    query = query[:-4]

    if "orderby" in request.args:
        query += "ORDER BY "
        col = constants.KICKING_COLUMNS.get(request.args["orderby"])
        query += col

    if "order" in request.args and request.args["order"] == "desc":
        query += " DESC"

    query += ";"
    print(query)
    print(vals)
    cursor.execute(query, vals)
    results = cursor.fetchall()

    return jsonify(results)

@app.route("/stats/nfl/returns", methods = ["GET"])
def get_returns():
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
        if any (sym in request.args["prets"] for sym in constants.syms):
            query += "punt_returns " 
            query += request.args["prets"][:1] 
            query += " %s AND "
            vals.append(request.args["prets"][1:])

        else:
            query += "punt_returns= %s"
            vals.append(request.args["pntrets"])

    if "pretyds" in request.args:
        if any (sym in request.args["pretyds"] for sym in constants.syms):
            query += "punt_return_yards " 
            query += request.args["pretyds"][:1] 
            query += " %s AND "
            vals.append(request.args["pretyds"][1:])

        else:
            query += "punt_return_yards= %s"
            vals.append(request.args["pretyds"])

    if "prettds" in request.args:
        if any (sym in request.args["prettds"] for sym in constants.syms):
            query += "punt_return_tds " 
            query += request.args["prettds"][:1] 
            query += " %s AND "
            vals.append(request.args["prettds"][1:])

        else:
            query += "punt_return_tds = %s"
            vals.append(request.args["prettds"])

    if "pretlng" in request.args:
        if any (sym in request.args["pretlng"] for sym in constants.syms):
            query += "long_punt_return " 
            query += request.args["pretyds"][:1] 
            query += " %s AND "
            vals.append(request.args["pretyds"][1:])

        else:
            query += "punt_returns= %s"
            vals.append(request.args["pretyds"])

    if "yppr" in request.args:
        if any (sym in request.args["yppr"] for sym in constants.syms):
            query += "yards_per_punt_return " 
            query += request.args["yppr"][:1] 
            query += " %s AND "
            vals.append(request.args["yppr"][1:])

        else:
            query += "yards_per_punt_return = %s"
            vals.append(request.args["yppr"])

    if "koret" in request.args:
        if any (sym in request.args["koret"] for sym in constants.syms):
            query += "kickoff_returns " 
            query += request.args["koret"][:1] 
            query += " %s AND "
            vals.append(request.args["koret"][1:])

        else:
            query += "kickoff_returns = %s"
            vals.append(request.args["koret"])

    if "koretyds" in request.args:
        if any (sym in request.args["koretyds"] for sym in constants.syms):
            query += "kickoff_return_yards " 
            query += request.args["koretyds"][:1] 
            query += " %s AND "
            vals.append(request.args["koretyds"][1:])

        else:
            query += "kickoff_return_yards = %s"
            vals.append(request.args["koretyds"])

    if "korettds" in request.args:
        if any (sym in request.args["kotd"] for sym in constants.syms):
            query += "kickoff_return_tds " 
            query += request.args["kotd"][:1] 
            query += " %s AND "
            vals.append(request.args["kotd"][1:])

        else:
            query += "kickoff_return_tds = %s"
            vals.append(request.args["kotd"])

    if "koretlng" in request.args:
        if any (sym in request.args["koretlng"] for sym in constants.syms):
            query += "long_kickoff_return " 
            query += request.args["koretlng"][:1] 
            query += " %s AND "
            vals.append(request.args["koretlng"][1:])

        else:
            query += "long_kickoff_return = %s"
            vals.append(request.args["koretlng"])

    if "ypkoret" in request.args:
        if any (sym in request.args["ypkoret"] for sym in constants.syms):
            query += "yards_per_kickoff_return " 
            query += request.args["ypkoret"][:1] 
            query += " %s AND "
            vals.append(request.args["ypkoret"][1:])

        else:
            query += "yards_per_kickoff_return = %s"
            vals.append(request.args["ypkoret"])

    if "apyds" in request.args:
        if any (sym in request.args["apyds"] for sym in constants.syms):
            query += "all_purpose_yards " 
            query += request.args["apyds"][:1] 
            query += " %s AND "
            vals.append(request.args["apyds"][1:])

        else:
            query += "all_purpose_yards = %s"
            vals.append(request.args["apyds"])

    query = query[:-4]

    if "orderby" in request.args:
        query += "ORDER BY "
        col = constants.RETURNS_COLUMNS.get(request.args["orderby"])
        query += col + " DESC"

    if "order" in request.args and request.args["order"] == "asc":
        query = query[:-4]

    query += ";"
    print(query)
    print(vals)
    cursor.execute(query, vals)
    results = cursor.fetchall()

    return jsonify(results)

@app.route("/stats/nfl/scoring", methods = ["GET"])
def get_scoring():
    return














app.run()