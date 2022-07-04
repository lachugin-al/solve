from enum import auto
import os
import random
import sqlite3
import pytest
from db.db_create import TEST_DB

# Session-scope фикстуру, которая получает текущее состояние базы данных и
# создает временную новую базу, в которой рандомизируются значения:
#   a. Для каждого корабля меняется на случайный один из компонентов: корпус, орудие или двигатель
#   b. В каждом компоненте меняется один из случайно выбранных параметров на случайное значение из допустимого диапазона (см. выше)

TMP_DB = f'{os.popen("pwd").read().rstrip()}/db/tmp.db'


@pytest.fixture(scope='session', autouse=True)
def db_tmp_create():
    """
    Session-scope фикстура, которая получает текущее состояние базы данных и создает временную новую базу.
    """
    if os.path.isfile(TMP_DB):
        os.remove(TMP_DB)

    test_db = open(TEST_DB, mode='rb+')
    tmp_db = open(TMP_DB, mode='xb+')
    tmp_db.write(test_db.read())
    test_db.close()
    tmp_db.close()

@pytest.fixture(scope="session")
def randomize_ships_params_in_tmp_db():
    """
    Для каждого корабля меняется на случайный один из компонентов: корпус, орудие или двигатель.
    """
    connection = sqlite3.connect(TMP_DB)
    cursor = connection.cursor()

    collect_ships = cursor.execute("SELECT * FROM ships").fetchall()
    collect_weapons = cursor.execute("SELECT * FROM weapons").fetchall()
    collect_hulls = cursor.execute("SELECT * FROM hulls").fetchall()
    collect_engines = cursor.execute("SELECT * FROM engines").fetchall()
    weapons_components = ["reload_speed", "rotational_speed",
                          "diameter", "power_volley", "count"]
    hulls_components = ["armor", "type", "capacity"]
    engines_components = ["power", "type"]

    for row in collect_ships:
        ship_component = random.randint(1, len(row) - 1)
        current_ship = list(row)
        if ship_component == 1:
            current_ship[ship_component] = f"Weapon-" + \
                str(random.randint(1, 20))
            current_ship_table = current_ship[ship_component].split(
                "-")[0].lower()
        elif ship_component == 2:
            current_ship[ship_component] = f"Hull-" + \
                str(random.randint(1, 20))
            current_ship_table = current_ship[ship_component].split(
                "-")[0].lower()
        elif ship_component == 3:
            current_ship[ship_component] = f"Engine-" + \
                str(random.randint(1, 20))
            current_ship_table = current_ship[ship_component].split(
                "-")[0].lower()
        with connection:
            cursor.execute(f"UPDATE ships SET {current_ship_table} = ? WHERE ship = ?",
                           (current_ship[ship_component], current_ship[0]))

    def randomize_ship_component_params_in_tmp_db():
        """
        В каждом компоненте меняется один из случайно выбранных параметров на случайное значение из допустимого диапазона.
        """
        for row in collect_weapons:
            current_weapon = list(row)
            random_component = random.choice(weapons_components)
            random_value = random.randint(1, 20)
            with connection:
                cursor.execute(
                    f"UPDATE weapons SET {random_component}={random_value} WHERE weapon='{current_weapon[0]}'")
        for row in collect_hulls:
            current_hull = list(row)
            random_component = random.choice(hulls_components)
            random_value = random.randint(1, 20)
            with connection:
                cursor.execute(
                    f"UPDATE hulls SET {random_component}={random_value} WHERE hull='{current_hull[0]}'")
        for row in collect_engines:
            current_engine = list(row)
            random_component = random.choice(engines_components)
            random_value = random.randint(1, 20)
            with connection:
                cursor.execute(
                    f"UPDATE engines SET {random_component}={random_value} WHERE engine='{current_engine[0]}'")

    randomize_ship_component_params_in_tmp_db()
    connection.commit()
    cursor.close()


# db_tmp_create()
# randomize_ships_params_in_tmp_db()
