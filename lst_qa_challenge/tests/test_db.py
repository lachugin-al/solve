# Написать автотесты, сравнивающие данные из исходной базы с полученной рандомизированной:
#   a. Для каждого корабля должно быть 3 теста, проверяющие его орудие, корпус и двигатель.
#   b. Тест должен падать с assert:
#       i. Когда значение параметра компонента не соответствует тому, что было до запуска рандомизатора.

import sqlite3
from tkinter.messagebox import NO
from conftest import TMP_DB
from db.db_create import TEST_DB
import pytest


@pytest.mark.parametrize("ship_number", [i for i in range(1, 201)])
def test_1(randomize_ships_params_in_tmp_db, ship_number):
    connection1 = sqlite3.connect(TEST_DB)
    connection2 = sqlite3.connect(TMP_DB)
    cursor1 = connection1.cursor()
    cursor2 = connection2.cursor()

    ship1 = cursor1.execute("SELECT * FROM ships").fetchall()[ship_number - 1]
    ship2 = cursor2.execute("SELECT * FROM ships").fetchall()[ship_number - 1]
    weapons1_list = cursor1.execute("SELECT * FROM weapons").fetchall()
    weapons2_list = cursor2.execute("SELECT * FROM weapons").fetchall()
    weapons2_table_info_list = cursor2.execute(
        "PRAGMA table_info(weapons)").fetchall()

    # забираем названия колонок в таблице
    weapons2_collumns = []
    for element in weapons2_table_info_list:
        weapons2_collumns.append(element[1])

    weapon1_title, weapon2_title = ship1[1], ship2[1]

    # weapon
    weapon2, weapon2_index = None, None
    for i in range(len(weapons2_list)):
        if weapons2_list[i][0] == weapon2_title:
            weapon2_index = i
            weapon2 = weapons2_list[i]
    weapon1 = weapons1_list[weapon2_index]

    # Когда значение параметра компонента не соответствует тому, что было до запуска рандомизатора.
    for i in range(len(weapon2)):
        if (weapon1[i] != weapon2[i]):
            print(f"{ship2[0]}, {weapon2[0].lower()}")
            print(f"""
                {weapons2_collumns[i]}: 
                    expected {weapon1[i]}, was {weapon2[i]}   
                """)

    # Когда изменилось значение одного из компонентов в таблице Ship
    # print(f"""
    #     {ship2[0]}, {weapon2_title}
    #         expected {weapon1_title}, was {weapon2_title}""")

    connection1.close()
    connection2.close()


@pytest.mark.parametrize("ship_number", [i for i in range(1, 201)])
def test_2(randomize_ships_params_in_tmp_db, ship_number):
    connection1 = sqlite3.connect(TEST_DB)
    connection2 = sqlite3.connect(TMP_DB)
    cursor1 = connection1.cursor()
    cursor2 = connection2.cursor()

    ship1 = cursor1.execute("SELECT * FROM ships").fetchall()[ship_number - 1]
    ship2 = cursor2.execute("SELECT * FROM ships").fetchall()[ship_number - 1]
    hulls1_list = cursor1.execute("SELECT * FROM hulls").fetchall()
    hulls2_list = cursor2.execute("SELECT * FROM hulls").fetchall()
    hulls2_table_info_list = cursor2.execute(
        "PRAGMA table_info(hulls)").fetchall()

    # забираем названия колонок в таблице
    hulls2_collumns = []
    for element in hulls2_table_info_list:
        hulls2_collumns.append(element[1])

    hull1_title = cursor2.execute("SELECT * FROM hulls").fetchall()
    hull2_title = ship1[2]

    # hull
    hull2, hull2_index = None, None
    for i in range(len(hulls2_list)):
        for y in range(len(hulls2_list)):
            if hulls2_list[i][0] == hull1_title[y][0]:
                hull2_index = i
            hull2 = hulls2_list[i]
    hull1 = hulls1_list[hull2_index]

    # Когда значение параметра компонента не соответствует тому, что было до запуска рандомизатора.
    for i in range(len(hull2)):
        if (hull1[i] != hull2[i]):
            print(f"{ship2[0]}, {hull2[0].lower()}")
            print(f"""
                {hulls2_collumns[i]}: 
                    expected {hull1[i]}, was {hull2[i]}   
                """)

    connection1.close()
    connection2.close()


@pytest.mark.parametrize("ship_number", [i for i in range(1, 201)])
def test_3(randomize_ships_params_in_tmp_db, ship_number):
    connection1 = sqlite3.connect(TEST_DB)
    connection2 = sqlite3.connect(TMP_DB)
    cursor1 = connection1.cursor()
    cursor2 = connection2.cursor()

    ship1 = cursor1.execute("SELECT * FROM ships").fetchall()[ship_number - 1]
    ship2 = cursor2.execute("SELECT * FROM ships").fetchall()[ship_number - 1]
    engines1_list = cursor1.execute("SELECT * FROM engines").fetchall()
    engines2_list = cursor2.execute("SELECT * FROM engines").fetchall()
    engines2_table_info_list = cursor2.execute(
        "PRAGMA table_info(engines)").fetchall()

    # забираем названия колонок в таблице
    engines2_collumns = []
    for element in engines2_table_info_list:
        engines2_collumns.append(element[1])

    engine1_title = cursor2.execute("SELECT * FROM engines").fetchall()
    engine2_title = ship1[3]

    # engine
    engine2, engine2_index = None, None
    for i in range(len(engines2_list)):
        for y in range(len(engines2_list)):
            if engines2_list[i][0] == engine1_title[y][0]:
                engine2_index = i
            engine2 = engines2_list[i]
    engine1 = engines1_list[engine2_index]

    # Когда значение параметра компонента не соответствует тому, что было до запуска рандомизатора.
    for i in range(len(engine2)):
        if (engine1[i] != engine2[i]):
            print(f"{ship2[0]}, {engine2[0].lower()}")
            print(f"""
                {engines2_collumns[i]}: 
                    expected {engine1[i]}, was {engine2[i]}   
                """)

    connection1.close()
    connection2.close()


# @pytest.mark.parametrize("db_path", [TEST_DB, TMP_DB])
# def test_correct_data_in_db(db_path):
#     connection = sqlite3.connect(db_path)
#     cursor = connection.cursor()
#     item = cursor.execute("SELECT * from ships").fetchall()[0][0]
#     assert item == "Ship-1"
#     connection.close()


# def test_correct_items_in__both_db(randomize_ships_params_in_tmp_db):
#     connection1 = sqlite3.connect(TEST_DB)
#     connection2 = sqlite3.connect(TMP_DB)
#     cursor1 = connection1.cursor()
#     cursor2 = connection2.cursor()

#     item_from_test_db = cursor1.execute("SELECT * from ships").fetchall()
#     item_from_tmp_db = cursor2.execute("SELECT * from ships").fetchall()

#     for item1 in item_from_test_db:
#         for item2 in item_from_tmp_db:
#             assert item1 == item2

#     cursor1.close()
#     cursor2.close()
