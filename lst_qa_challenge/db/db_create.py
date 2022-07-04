import os
import sqlite3


# Python-скрипт, создающий SQLite базу по указанной схеме.
# Primary key – текстовое поле weapon / ship / hull / engine соответственно.

TEST_DB = f'{os.popen("pwd").read().rstrip()}/db/test.db'

db_ships = """
CREATE TABLE IF NOT EXISTS
ships (
    ship TEXT PRIMARY KEY, weapon TEXT, hull TEXT, engine TEXT,
    FOREIGN KEY (weapon) REFERENCES weapons (weapon),
    FOREIGN KEY (hull) REFERENCES hulls (hull),
    FOREIGN KEY (engine) REFERENCES engines (engine)
)
"""
db_weapons = """
CREATE TABLE IF NOT EXISTS
weapons (
    weapon TEXT PRIMARY KEY, reload_speed INT, rotational_speed INT, diameter INT, power_volley INT, count INT
)
"""
db_hulls = """
CREATE TABLE IF NOT EXISTS
hulls (
    hull TEXT PRIMARY KEY, armor INT, type INT, capacity INT
)
"""
db_engines = """
CREATE TABLE IF NOT EXISTS
engines (
    engine TEXT PRIMARY KEY, power INT, type INT
)
"""

db_list = [db_ships, db_weapons, db_hulls, db_engines]


def db_create(db_list: list[str]):
    """
    Python-скрипт, создающий SQLite базу по указанной схеме.
    """
    connection = sqlite3.connect(TEST_DB)
    cursor = connection.cursor()
    for table in db_list:
        cursor.execute(table)
    cursor.close()


def db_drop():
    """
    Python-скрипт, очищающий SQLite базу данных.
    """
    connection = sqlite3.connect(TEST_DB)
    cursor = connection.cursor()
    cursor.execute("DROP TABLE ships")
    cursor.execute("DROP TABLE weapons")
    cursor.execute("DROP TABLE hulls")
    cursor.execute("DROP TABLE engines")
    cursor.close()


db_create(db_list)
