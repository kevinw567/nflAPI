syms = [">", "<"]

# dictionaries mapping url categories to the corresponding table columns
PASSING_COLUMNS = { "cmp": "completions", "att": "pass_attempts", "cmpp": "completion_percent", "yds": "yards", "td": "TD", "int": "interceptions", "ypg": "yards_per_game", "ypc": "yards_per_comp", "ypa": "yards_per_attempt", "lng": "longest_pass", "rtng": "passer_rating", "qbr": "qbr" }
RUSHING_COLUMNS = { "att": "attempts", "yds": "yards", "td": "touchdowns", "fd": "first_downs", "lng": "long_rush", "ypa": "yards_per_attempt", "ypg": "yards_per_game", "fmb": "fumbles" }
DEFENSE_COLUMNS = { "int": "interceptions", "intyds": "interception_yards", "hits": "qbhits" }
SCRIMMAGE_COLUMNS = { "tch": "touches", "ypt": "yards_per_touch", "yds": "scrimmage_yards" }
RECEIVING_COLUMNS = { "tgt": "targets", "rec": "receptions", "ctch%": "catch_percent", "yds": "yards", "ypc": "yards_per_reception", "td": "td", "fd": "first_downs", "lng": "long_reception", "ypt": "yards_per_target", "rpg": "receptions_per_game", "ypg": "yards_per_game", "fmbl": "fumbles" }
KICKING_COLUMNS = { "fga19": "FGA19", "fgm19": "FGM19", "fga29": "FGM29", "fga39": "FGM39", "fga49": "FGM49", "fga50": "FGA50", "fgm50": "FGM50", "fga" : "FGA", "fgm": "FGM", "fglng": "FGLong", "fg%": "FGPercent", "xpa": "XPA", "xpm": "XPM", "xp%": "XPPercent", "ko" : "KO", "koyds": "KOYds", "tb": "TB", "tb%": "TBPercent", "koavg": "KOAvg", "pnts": "Pnts", "pntavg": "PntAvg", "pntlng": "PntLong", "blck": "Blocked", "ypp": "YdsPerPnt" }
RETURNS_COLUMNS = { "prets": "punt_returns", "pretyds": "punt_return_yards", "prettds": "punt_return_tds", "pretlng": "long_punt_return", "yppr": "yards_per_punt_return", "koret": "kickoff_returns", "koretyds": "kickoff_return_yards", "korettds": "kickoff_return_tds", "koretlng": "long_kickoff_return", "ypkoret": "yards_per_kickoff_return", "apyds": "all_purpose_yards" }
SCORING_COLUMNS = { "rushtd": "rushingTD", "rectd": "receivingTD", "prettd": "punt_returnTD", "koretd": "kick_returnTD", "fmbltd": "fumbleTD", "inttd": "interceptionTD", "othertd": "otherTD", "alltd": "allTD", "2pm": "twoPM", "2pa": "twoPA", "xpa": "XPA", "xpm": "XPM", "fga": "FGA", "fgm": "FGM", "sfty": "Sfty", "pts": "points", "ppg": "points_per_game" }
# SELECT QUERIES
SELECT_ID_BY_NAME = "SELECT id FROM player_info WHERE name LIKE %s"
SELECT_PASSING = "SELECT * from player_info as p JOIN passing2020 as pa on p.id = pa.id WHERE "
SELECT_RUSHING = "SELECT * FROM player_info as p JOIN rushing2020 as r on p.id = r.id WHERE "
SELECT_RECEIVING = "SELECT * FROM player_info as p JOIN receiving2020 as r on p.id = r.id WHERE "
SELECT_DEFENSE = "SELECT * FROM player_info as p JOIN defense2020 as d on p.id = d.id WHERE "
SELECT_SCRIMMAGE = "SELECT * FROM player_info as p JOIN scrimmage2020 as s on p.id = s.id WHERE "
SELECT_KICKING = "SELECT * FROM player_info as p JOIN kicking2020 as k on p.id = k.id WHERE "
SELECT_RETURNS = "SELECT * FROM player_info as p JOIN returns2020 as r on p.id = r.id WHERE "
SELECT_SCORING = "SELECT * FROM player_info as p JOIN scoring2020 as s on p.id = s.id WHERE "

# INSERT QUERIES
INSERT_PLAYER_INFO = "INSERT INTO player_info (name, position, team) VALUES (%s, %s, %s)"
INSERT_PASSING = "INSERT INTO passing2020 (id, completions, pass_attempts, completion_percent, yards, TD, interceptions, \
                    yards_per_game, yards_per_comp, yards_per_attempt, longest_pass, passer_rating, qbr) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
INSERT_DEFENSE = "INSERT INTO defense2020 (id, interceptions, interception_yards, interception_tds, long_interception_return, passes_defensed, forced_fumbles, \
                fumble_recoveries, fumble_return_yards, fumble_return_tds, sacks, comb_tackles, solo_tackles, assisted_tackles, tackles_for_loss, qbhits, safetys) VALUES \
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
INSERT_KICKING = "INSERT INTO kicking2020 (id, FGA19, FGM19, FGA29, FGM29, FGA39, FGM39, FGA49, FGM49, FGA50, FGM50, FGA, FGM, FGLong, FGPercent, XPA, XPM, XPPercent, KO, KOYds, TB, TBPercent, \
    KOAvg, Pnts, PntAvg, PntLong, Blocked, YdsPerPnt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
INSERT_RECEIVING = "INSERT INTO receiving2020 (id, targets, receptions, catch_percent, yards, yards_per_reception, td, first_downs, long_reception, yards_per_target, \
    receptions_per_game, yards_per_game, fumbles) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
INSERT_RETURNS = "INSERT INTO returns2020 (id, punt_returns, punt_return_yards, punt_return_tds, long_punt_return, yards_per_punt_return, kickoff_returns, kickoff_return_yards, \
    kickoff_return_tds, long_kickoff_return, yards_per_kickoff_return, all_purpose_yards) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
INSERT_RUSHING = "INSERT INTO rushing2020 (id, attempts, yards, touchdowns, first_downs, long_rush, yards_per_attempt, yards_per_game, fumbles) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
INSERT_SCORING = "INSERT INTO scoring2020 (id, rushingTD, receivingTD, punt_returnTD, kick_returnTD, fumbleTD, interceptionTD, otherTD, allTD, twoPM, twoPA, points, points_per_game) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
INSERT_SCRIMMAGE = "INSERT INTO scrimmage2020 (id, touches, yards_per_touch, scrimmage_yards) VALUES (%s, %s, %s, %s)"