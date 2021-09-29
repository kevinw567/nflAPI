import mysql.connector
import os
from os import path
import dbSetUp
import csv
from views import app

db = mysql.connector.connect(
    host = app.config["HOST"],
    user = app.config["USER"],
    password = app.config["PASSWORD"],
    database = app.config["DATABASE"],
    auth_plugin = "mysql_native_password"
)

cursor = db.cursor()
dirname = path.join(os.getcwd(), '/csv')
files = os.listdir(path.join(os.getcwd(), "./csv"))
for file in files:
    if file == "Passing2020.csv":
        dbSetUp.add_passing()
    elif file == "Defense2020.csv":
       dbSetUp.add_defense()
    elif file == "Kicking2020.csv":
        dbSetUp.add_kicking()
    elif file == "Receiving2020.csv":
        dbSetUp.add_receiving()
    elif file == "Returns2020.csv":
        dbSetUp.add_returns()
    elif file == "Rushing2020.csv":
        dbSetUp.add_rushing()
    elif file == "Scoring2020.csv":
        dbSetUp.add_scoring()
    elif file == "Scrimmage2020.csv":
        dbSetUp.add_scrimmage()      