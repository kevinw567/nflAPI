CREATE DATABASE nflStats IF NOT EXISTS;
USE nflStats;

CREATE TABLE player_info (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    position VARCHAR(3),
    team VARCHAR(5)
);

CREATE TABLE passing (
    id INT PRIMARY KEY,
    year INT,
    completions INT,
    pass_attempts INT,
    completion_percent FLOAT,
    yards INT,
    TD INT,
    interceptions INT,
    yards_per_game FLOAT,
    yards_per_comp FLOAT,
    yards_per_attempt FLOAT,
    longest_pass INT,
    passer_rating FLOAT,
    qbr FLOAT,
) IF NOT EXISTS;

CREATE TABLE defense (
    id INT PRIMARY KEY,
    year INT,
    interceptions INT,
    interception_yards INT,
    interception_tds INT,
    long_interception_return INT,
    passes_defensed INT,
    forced_fumbles INT, 
    fumble_recoveries INT,
    fumble_return_yards INT,
    fumble_return_tds INT,
    sacks INT,
    comb_tackles INT,
    assisted_tackles INT,
    tackles_for_loss INT,
    qbhits INT, 
    safetys INT
) IF NOT EXISTS;

CREATE TABLE kicking (
    id INT PRIMARY KEY,
    year INT,
    FGA19 INT,
    FGM19 INT,
    FGA29 INT,
    FGM29 INT,
    FGA39 INT,
    FGM39 INT,
    FGA49 INT,
    FGM49 INT,
    FGA50 INT,
    FGM50 INT,
    FGA INT,
    FGM INT,
    FGLong INT,
    FGPercent FLOAT,
    XPA INT,
    XPM INT,
    XPPercent FLOAT,
    KO INT,
    KOYds INT,
    TB INT,
    TBPercent FLOAT,
    KOAvg FLOAT,
    Pnts INT,
    PntAvg FLOAT,
    PntLong INT,
    Blocked INT,
    YdsPerPnt FLOAT
) IF NOT EXISTS;

CREATE TABLE receiving (
    id INT PRIMARY KEY,
    year INT,
    targets INT,
    receptions INT,
    catch_percent FLOAT,
    yards INT,
    yards_per_reception FLOAT,
    td INT,
    first_downs INT,
    long_reception INT,
    yards_per_target FLOAT,
    receptions_per_game FLOAT,
    yards_per_game FLOAT,
    fumbles INT
);

CREATE TABLE returns (
    id INT PRIMARY KEY,
    year INT,
    punt_returns INT,
    punt_return_yards INT,
    punt_return_tds INT,
    long_punt_return INT,
    yards_per_punt_return FLOAT,
    kickoff_returns INT,
    kickoff_return_yards INT,
    kickoff_return_tds INT,
    long_kickoff_return INT,
    yards_per_kickoff_return FLOAT,
    all_purpose_yards INT
) IF NOT EXISTS;

CREATE TABLE rushing (
    id INT PRIMARY KEY,
    year INT,
    attempts INT,
    yards INT,
    touchdowns INT,
    first_downs INT,
    long_rush INT,
    yards_per_attempt FLOAT,
    yards_per_game FLOAT,
    fumbles INT
) IF NOT EXISTS;

CREATE TABLE scoring (
    id INT PRIMARY KEY,
    year INT,
    rushingTD INT,
    receivingTD INT,
    punt_returnTD INT,
    kick_returnTD INT,
    fumbleTD INT,
    interceptionTD INT,
    otherTD INT,
    allTD INT,
    twoPM INT,
    twoPA INT,
    XPA INT,
    XPM INT,
    FGM INT,
    FGA INT,
    Sfty INT,
    points INT,
    points_per_game FLOAT
) IF NOT EXISTS;

CREATE TABLE scrimmage (
    id INT PRIMARY KEY,
    year INT,
    touches INT,
    yards_per_touch FLOAT,
    scrimmage_yards INT
) IF NOT EXISTS;