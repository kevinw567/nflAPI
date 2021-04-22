from flask import Blueprint, jsonify, request
import const as constants
import mysql.connector

players = Blueprint("players", __name__, url_prefix= "/stats/nfl")

