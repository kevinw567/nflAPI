import mysql.connector
import views.const as constants
import csv
from views import app

"""

""" 
def add_passing():
    db = mysql.connector.connect(
    host = app.config["HOST"],
    user = app.config["USER"],
    password = app.config["PASSWORD"],
    database = app.config["DATABASE"],
    auth_plugin = "mysql_native_password"
    )

    cursor = db.cursor()
    with open("./csv/Passing*.csv") as csvFile:
            reader = csv.DictReader(csvFile)
            # read the csv file row-by-row and query for the current player, if the player is not already in the database add him,
            # if he is continue to add passing stats
            for row in reader:
                # cleanse the player name before searching
                name = str(row["Player"]).replace("*", "")
                name = name.replace("+", "").strip()
                cursor.execute(constants.SELECT_ID_BY_NAME, [name])
                results = cursor.fetchall()
                if len(results) == 0:
                    print("Adding to player_info")
                    team = str(row["Tm"]).upper()
                    pos = str(row["Pos"]).upper()
                    cursor.execute(constants.INSERT_PLAYER_INFO, [name, pos, team])
                    db.commit()
                    
                print(f'Adding {row["Player"]} to passing')
                pid = results[0][0]
                # get info to add to database
                completions = row["Cmp"]
                attempts = row["Att"]
                comp_percent = row["Cmp%"]
                yards = row["Yds"]
                tds = row["TD"]
                ints = row["Int"]
                long_pass = row["Lng"]
                yards_per_game = row["Y/G"]
                yards_per_comp = row["Y/C"]
                yards_per_attempt = row["Y/A"]
                passer_rating = row["Rate"]
                qbr = row["QBR"]
                
                vals = (pid, completions, attempts, comp_percent, yards, tds, ints, yards_per_game, yards_per_comp, \
                    yards_per_attempt, long_pass, passer_rating, qbr)
                cursor.execute(constants.INSERT_PASSING, vals)
                db.commit()

    db.close()

def add_defense():
    db = mysql.connector.connect(
    host = "localhost",
    user = "kevin",
    password = "password",
    database = "nflStats"
    )   

    cursor = db.cursor()
    with open("./csv/Defense2020.csv") as csvFile:
        reader = csv.DictReader(csvFile)
        # read the csv file row-by-row and query for the current player, if the player is not already in the database add him,
        # if he is continue to add passing stats
        for row in reader:
        # cleanse the player name before querying
            name = str(row["Player"]).replace("*", "")
            name = name.replace("+", "").strip()
            cursor.execute(constants.SELECT_ID_BY_NAME, [name])
            results = cursor.fetchall()
            if len(results) == 0:
                print("Adding to player_info")
                team = str(row["Tm"]).upper()
                pos = str(row["Pos"]).upper()
                cursor.execute(constants.INSERT_PLAYER_INFO, [name, pos, team])
                db.commit()
            print(f'Adding {name} to defense')
            cursor.execute(constants.SELECT_ID_BY_NAME, [name])
            results = cursor.fetchall()
            pid = results[0][0]                 # TODO get pid after inserting into player_info for first time
            # get info to add to database
            ints = row["Int"]
            int_return_yards = row["Yds"]
            p6 = row["TD"]
            long_return = row["Lng"]
            passes_defensed = row["PD"]
            forced_fmbl = row["FF"]
            fmbl_recoveries = row["FR"]
            fmbl_return_yards = row["Yds.1"]
            f6 = row["TD.1"]
            sacks = row["Sk"]
            combo_tkls = row["Comb"]
            solo_tkls = row["Solo"]
            assisted_tkls = row["Ast"]
            tfl = row["TFL"]
            qb_hits = row["QBHits"]
            sftys = row["Sfty"]

            vals = (pid, ints, int_return_yards, p6, long_return, passes_defensed, forced_fmbl, fmbl_recoveries, fmbl_return_yards, f6, sacks, combo_tkls, solo_tkls, assisted_tkls, tfl, qb_hits, sftys)
            cursor.execute(constants.INSERT_DEFENSE, vals)
            db.commit()

    db.close()

def add_kicking():
    db = mysql.connector.connect(
    host = "localhost",
    user = "kevin",
    password = "password",
    database = "nflStats"
    )   

    cursor = db.cursor()
    with open("./csv/Kicking2020.csv") as csvFile:
        reader = csv.DictReader(csvFile)
        # read the csv file row-by-row and query for the current player, if the player is not already in the database add him,
        # if he is continue to add passing stats
        for row in reader:
        # cleanse the player name before querying
            name = str(row["Player"]).replace("*", "")
            name = name.replace("+", "").strip()
            cursor.execute(constants.SELECT_ID_BY_NAME, [name])
            results = cursor.fetchall()
            if len(results) == 0:
                print("Adding to player_info")
                team = str(row["Tm"]).upper()
                pos = str(row["Pos"]).upper()
                cursor.execute(constants.INSERT_PLAYER_INFO, [name, pos, team])
                db.commit()
            print(f'Adding {name} to kicking')
            cursor.execute(constants.SELECT_ID_BY_NAME, [name])
            results = cursor.fetchall()
            pid = results[0][0]
            # get info to add to database
            FGA19U = row["FGA"]
            FGM19U = row["FGM"]
            FGA29U = row["FGA.1"]
            FGM29U = row["FGM.1"]
            FGA39U = row["FGA.2"]
            FGM39U = row["FGM.2"]
            FGA49U = row["FGA.3"]
            FGM49U = row["FGM.3"]
            FGA50 = row["FGA.4"]
            FGM50 = row["FGM.4"]
            FGA = row["FGA.5"]
            FGM = row["FGM.5"]
            long_kick = row["Lng"]
            fg_percent = row["FG%"]
            XPA = row["XPA"]
            XPM = row["XPM"]
            xp_percent = row["XP%"]
            kickoffs = row["KO"]
            kickoff_yards = row["KOYds"]
            touchbacks = row["TB"]
            tb_percent = row["TB%"]
            ko_avg = row["KOAvg"]
            punts = row["Pnt"]
            punt_yards = row["Yds"]
            long_punt = row["Lng.1"]
            blocked = row["Blck"]
            yards_per_punt = row["Y/P"]
            # remove percent symbol from percent data
            fg_percent = fg_percent.replace("%", "")
            xp_percent = xp_percent.replace("%", "")
            tb_percent = tb_percent.replace("%", "")

            vals = (pid, FGA19U, FGM19U, FGA29U, FGM29U, FGA39U, FGM39U, FGA49U, FGM49U, FGA50, FGM50, FGA, FGM, long_kick, \
                fg_percent, XPA, XPM, xp_percent, kickoffs, kickoff_yards, touchbacks, tb_percent, ko_avg, punts, punt_yards, \
                    long_punt, blocked, yards_per_punt)
            cursor.execute(constants.INSERT_KICKING, vals)
            db.commit()

    db.close()


def add_receiving():
    db = mysql.connector.connect(
    host = "localhost",
    user = "kevin",
    password = "password",
    database = "nflStats"
    )   

    cursor = db.cursor()
    with open("./csv/Receiving2020.csv") as csvFile:
        reader = csv.DictReader(csvFile)
        # read the csv file row-by-row and query for the current player, if the player is not already in the database add him,
        # if he is continue to add passing stats
        for row in reader:
        # cleanse the player name before querying
            name = str(row["Player"]).replace("*", "")
            name = name.replace("+", "").strip()
            cursor.execute(constants.SELECT_ID_BY_NAME, [name])
            results = cursor.fetchall()
            if len(results) == 0:
                print("Adding to player_info")
                team = str(row["Tm"]).upper()
                pos = str(row["Pos"]).upper()
                cursor.execute(constants.INSERT_PLAYER_INFO, [name, pos, team])
                db.commit()
            print(f'Adding {name} to receiving')
            cursor.execute(constants.SELECT_ID_BY_NAME, [name])
            results = cursor.fetchall()
            pid = results[0][0]
            # get info to add to database
            targets = row["Tgt"]
            rec = row["Rec"]
            catch_per = row["Ctch%"]
            yards = row["Yds"]
            yards_per_rec = row["Y/R"]
            tds = row["TD"]
            first_downs = row["1D"]
            long = row["Lng"]
            yards_per_tar = row["Y/Tgt"]
            rec_per_game = row["R/G"]
            yards_per_game = row["Y/G"]
            fmbls = row["Fmb"]
            # remove percent symbol from percent data
            catch_per = catch_per.replace("%", "")

            vals = (pid, targets, rec, catch_per, yards, yards_per_rec, tds, first_downs, long, yards_per_tar, rec_per_game, \
                yards_per_game, fmbls)
            cursor.execute(constants.INSERT_RECEIVING, vals)
            db.commit()
    
    db.close()

def add_returns():
    db = mysql.connector.connect(
        host = "localhost",
        user = "kevin",
        password = "password",
        database = "nflStats"
    )   

    cursor = db.cursor()
    with open("./csv/Returns2020.csv") as csvFile:
        reader = csv.DictReader(csvFile)
        # read the csv file row-by-row and query for the current player, if the player is not already in the database add him,
        # if he is continue to add passing stats
        for row in reader:
        # cleanse the player name before querying
            name = str(row["Player"]).replace("*", "")
            name = name.replace("+", "").strip()
            cursor.execute(constants.SELECT_ID_BY_NAME, [name])
            results = cursor.fetchall()
            if len(results) == 0:
                print("Adding to player_info")
                team = str(row["Tm"]).upper()
                pos = str(row["Pos"]).upper()
                cursor.execute(constants.INSERT_PLAYER_INFO, [name, pos, team])
                db.commit()
            print(f'Adding {name} to returns')
            cursor.execute(constants.SELECT_ID_BY_NAME, [name])
            results = cursor.fetchall()
            pid = results[0][0]
            # get info to add to database
            punt_rets = row["Ret"]
            punt_ret_yards = row["Yds"]
            punt_ret_td = row["TD"]
            long_punt_ret = row["Lng"]
            yards_per_punt_ret = row["Y/R"]
            ko_returns = row["Rt"]
            ko_yards = row["Yds.1"]
            ko_td = row["TD.1"]
            long_ko_ret = row["Lng.1"]
            yards_per_ko_ret = row["Y/Rt"]
            all_purpose_yards = row["APYd"]

            vals = (pid, punt_rets, punt_ret_yards, punt_ret_td, long_punt_ret, yards_per_punt_ret, ko_returns, ko_yards, ko_td, \
                long_ko_ret, yards_per_ko_ret, all_purpose_yards)
            cursor.execute(constants.INSERT_RETURNS, vals)
            db.commit()
    
    db.close()

def add_rushing():
    db = mysql.connector.connect(
    host = "localhost",
    user = "kevin",
    password = "password",
    database = "nflStats"
    )   

    cursor = db.cursor()
    with open("./csv/Rushing2020.csv") as csvFile:
        reader = csv.DictReader(csvFile)
        # read the csv file row-by-row and query for the current player, if the player is not already in the database add him,
        # if he is continue to add passing stats
        for row in reader:
        # cleanse the player name before querying
            name = str(row["Player"]).replace("*", "")
            name = name.replace("+", "").strip()
            cursor.execute(constants.SELECT_ID_BY_NAME, [name])
            results = cursor.fetchall()
            if len(results) == 0:
                print("Adding to player_info")
                team = str(row["Tm"]).upper()
                pos = str(row["Pos"]).upper()
                cursor.execute(constants.INSERT_PLAYER_INFO, [name, pos, team])
                db.commit()
            print(f'Adding {name} to rushing')
            cursor.execute(constants.SELECT_ID_BY_NAME, [name])
            results = cursor.fetchall()
            pid = results[0][0]
            # get info to add to database
            attempts = row["Att"]
            yards = row["Yds"]
            tds = row["TD"]
            fds = row["1D"]
            long = row["Lng"]
            yards_per_attempt = row["Y/A"]
            yards_per_game = row["Y/G"]
            fmbls = row["Fmb"]

            vals = (pid, attempts, yards, tds, fds, long, yards_per_attempt, yards_per_game, fmbls)
            cursor.execute(constants.INSERT_RUSHING, vals)
            db.commit()

    db.close()

def add_scoring():
    db = mysql.connector.connect(
    host = "localhost",
    user = "kevin",
    password = "password",
    database = "nflStats"
    )   

    cursor = db.cursor()
    with open("./csv/Scoring2020.csv") as csvFile:
        reader = csv.DictReader(csvFile)
        # read the csv file row-by-row and query for the current player, if the player is not already in the database add him,
        # if he is continue to add passing stats
        for row in reader:
        # cleanse the player name before querying
            name = str(row["Player"]).replace("*", "")
            name = name.replace("+", "").strip()
            cursor.execute(constants.SELECT_ID_BY_NAME, [name])
            results = cursor.fetchall()
            if len(results) == 0:
                print("Adding to player_info")
                team = str(row["Tm"]).upper()
                pos = str(row["Pos"]).upper()
                cursor.execute(constants.INSERT_PLAYER_INFO, [name, pos, team])
                db.commit()
            print(f'Adding {name} to scoring')
            cursor.execute(constants.SELECT_ID_BY_NAME, [name])
            results = cursor.fetchall()
            pid = results[0][0]
            # get info to add to database
            rushTD = row["RshTD"]
            recTD = row["RecTD"]
            prTD = row["PR TD"]
            krTD = row["KR TD"]
            fblTD = row["FblTD"]
            intTD = row["IntTD"]
            otherTD = row["OthTD"]
            allTD = row["AllTD"]
            twoPM = row["2PM"]
            twoPA = row["2PA"]
            pts = row["Pts"]
            pts_per_game = row["Pts/G"]

            vals = (pid, rushTD, recTD, prTD, krTD, fblTD, intTD, otherTD, allTD, twoPM, twoPA, pts, pts_per_game)
            cursor.execute(constants.INSERT_SCORING, vals)
            db.commit()
    
    db.close()

def add_scrimmage():
    db = mysql.connector.connect(
    host = "localhost",
    user = "kevin",
    password = "password",
    database = "nflStats"
    )   

    cursor = db.cursor()
    with open("./csv/Scrimmage2020.csv") as csvFile:
        reader = csv.DictReader(csvFile)
        # read the csv file row-by-row and query for the current player, if the player is not already in the database add him,
        # if he is continue to add passing stats
        for row in reader:
        # cleanse the player name before querying
            name = str(row["Player"]).replace("*", "")
            name = name.replace("+", "").strip()
            cursor.execute(constants.SELECT_ID_BY_NAME, [name])
            results = cursor.fetchall()
            if len(results) == 0:
                print("Adding to player_info")
                team = str(row["Tm"]).upper()
                pos = str(row["Pos"]).upper()
                cursor.execute(constants.INSERT_PLAYER_INFO, [name, pos, team])
                db.commit()
            print(f'Adding {name} to scrimmage')
            cursor.execute(constants.SELECT_ID_BY_NAME, [name])
            results = cursor.fetchall()
            pid = results[0][0]
            # get info to add to database
            touches = row["Touch"]
            yards_per_touch = row["Y/Tch"]
            scrimmage_yards = row["YScm"]

            vals = (pid, touches, yards_per_touch, scrimmage_yards)
            cursor.execute(constants.INSERT_SCRIMMAGE, vals)
            db.commit()
            
    db.close()