import random
import sqlite3
from db_create import TEST_DB

# Скрипт, который будет рандомно заполнять значения в созданной базе.
# Названия: Ship-1, Ship-2, Weapon-1 и т. д.

ships = 200
weapons = 20
hulls = 5
engines = 6
values = (1, 20)

connection = sqlite3.connect(TEST_DB)
cursor = connection.cursor()


def create_ship(ship: str, weapon: str, hull: str, engine: str):
    with connection:
        cursor.execute("INSERT INTO ships VALUES (?, ?, ?, ?)",
                       (ship, weapon, hull, engine))


def create_weapon(weapon: str, reload_speed: int, rotational_speed: int, diameter: int, power_volley: int, count: int):
    with connection:
        cursor.execute("INSERT INTO weapons VALUES (?, ?, ?, ?, ?, ?)",
                       (weapon, reload_speed, rotational_speed, diameter, power_volley, count))


def create_hull(hull: str, armor: int, type: int, capacity: int):
    with connection:
        cursor.execute("INSERT INTO hulls VALUES (?, ?, ?, ?)",
                       (hull, armor, type, capacity))


def create_engine(engine: str, power: int, type: int):
    with connection:
        cursor.execute("INSERT INTO engines VALUES (?, ?, ?)",
                       (engine, power, type))


def db_fill():
    """
    Скрипт, который будет рандомно заполнять значения в созданной базе.
    """
    for i in range(weapons):
        create_weapon(weapon=("Weapon-" + str(i + 1)),
                      reload_speed=random.randint(*values),
                      rotational_speed=random.randint(*values),
                      diameter=random.randint(*values),
                      power_volley=random.randint(*values),
                      count=random.randint(*values)
                      )

    for i in range(hulls):
        create_hull(hull=("Hull-" + str(i + 1)),
                    armor=random.randint(*values),
                    type=random.randint(*values),
                    capacity=random.randint(*values)
                    )

    for i in range(engines):
        create_engine(engine=("Engine-" + str(i + 1)),
                      power=random.randint(*values),
                      type=random.randint(*values)
                      )

    for i in range(ships):
        create_ship(ship=("Ship-" + str(i + 1)),
                    weapon=("Weapon-" + str(random.randint(*values))),
                    hull=("Hull-" + str(random.randint(*values))),
                    engine=("Engine-" + str(random.randint(*values)))
                    )
    cursor.close()


db_fill()
