import sqlite3
import string
from datetime import *
from random import *

import DBStructure


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def exec_insert_query(cursor, table_name, fields, values):
    query = 'INSERT INTO ?(' + '?,' * (len(fields) - 1) + '?' + ') VALUES (' + '?,' * (len(values) - 1) + '?)'
    cursor.execute(query, (table_name,) + fields + values)


def gen_random_location(cursor):
    table_name = DBStructure.LOCATION_TABLE_NAME
    fields = (DBStructure.LOCATION_TABLE_FIELD_COUNTRY, DBStructure.LOCATION_TABLE_FIELD_ZIP,
              DBStructure.LOCATION_TABLE_FIELD_CITY)
    values = ('RUSSIA', 'INNOPOLIS', '420500')
    exec_insert_query(cursor, table_name, fields, values)


def gen_random_client(cursor):
    d1 = datetime.strptime('1/1/1938 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/1/1998 4:50 AM', '%m/%d/%Y %I:%M %p')
    table_name = DBStructure.CLIENT_TABLE_NAME
    fields = (DBStructure.CLIENT_TABLE_FIELD_USERNAME, DBStructure.CLIENT_TABLE_FIELD_DATE_OF_BIRTH)
    values = ("sample_user_" + randint(1, 1000), random_date(d1, d2))
    exec_insert_query(cursor, table_name, fields, values)


def gen_random_car_model(cursor):
    color = ["red", "blue", "green", "yellow", "purple", "orange", "white", "black"]
    manufacturers = ["Chevrolet", "Ford", "Toyota", "Honda", "BMW", "Nissan", "Jeep", "Hyundai"]
    number = choice(string.ascii_uppercase) + choice(string.ascii_uppercase) + randint(1000, 9999) + choice(
        string.ascii_uppercase)
    table_name = DBStructure.ALL_CARS_TABLE_NAME
    fields = (DBStructure.ALL_CARS_FIELD_COLOR, DBStructure.ALL_CARS_FIELD_MANUFACTURE,
              DBStructure.ALL_CARS_FIELD_NUMBER)
    values = (choice(color), choice(manufacturers), number)
    exec_insert_query(cursor, table_name, fields, values)


def gen_random_car(cursor, model_id):
    table_name = DBStructure.CAR_TABLE_NAME
    fields = (DBStructure.CAR_TABLE_FIELD_CHARGE_LEVEL, DBStructure.CAR_TABLE_LAT,
              DBStructure.CAR_TABLE_LNG, DBStructure.CAR_TABLE_ALL_CARS)
    lat = uniform(-90, 90)
    lng = uniform(-180, 180)
    values = (1.0, lat, lng, model_id)
    exec_insert_query(cursor, table_name, fields, values)


# TODO: decide what to do with charge event and refill station


def gen_random_video(cursor, model_id):
    table_name = DBStructure.VIDEO_TABLE_NAME
    d1 = datetime.strptime('1/1/2017 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/11/2018 4:50 AM', '%m/%d/%Y %I:%M %p')
    fields = (DBStructure.VIDEO_TABLE_FIELD_DURATION, DBStructure.VIDEO_TABLE_FIELD_START_TIME,
              DBStructure.VIDEO_TABLE_FIELD_CONTENT, DBStructure.VIDEO_TABLE_FIELD_ALL_CARD_ID)
    # duration is in ms
    values = (randint(1000, 1000000000), random_date(d1, d2), "sample_video_" + randint(1, 1000) + ".avi", model_id)
    exec_insert_query(cursor, table_name, fields, values)


def gen_random_manager(cursor):
    phone = '+'.join(random.choice(string.digits) for i in range(11))
    table_name = DBStructure.MANAGER_TABLE_NAME
    fields = (DBStructure.MANAGER_TABLE_FIELD_NAME, DBStructure.MANAGER_TABLE_PHONE)
    values = ("sample_manager_" + randint(1, 1000), phone)
    exec_insert_query(cursor, table_name, fields, values)


def bind_usr_loc(cursor, user_id, loc_id):
    table_name = DBStructure.RELATION_TABLE_LIVES_AT_NAME
    fields = (DBStructure.RELATION_TABLE_LIVES_AT_CLIENT_ID, DBStructure.RELATION_TABLE_LIVES_AT_LOCATION_ID)
    values = (user_id, loc_id)
    exec_insert_query(cursor, table_name, fields, values)


def gen_order(cursor, manager_id, client_id, car_id):
    table_name = DBStructure.ORDER_TABLE_NAME
    fields = (DBStructure.ORDER_TABLE_FIELD_STARTING_POSITION_LAT, DBStructure.ORDER_TABLE_FIELD_STARTING_POSITION_LNG,
              DBStructure.ORDER_TABLE_FIELD_DESTINATION_LAT, DBStructure.ORDER_TABLE_FIELD_DESTINATION_LNG,
              DBStructure.ORDER_TABLE_FIELD_START_TIME, DBStructure.ORDER_TABLE_FIELD_END_TIME,
              DBStructure.ORDER_TABLE_FIELD_PRICE, DBStructure.ORDER_TABLE_FIELD_SATISFACTION,
              DBStructure.ORDER_TABLE_FIELD_MANAGER_ID, DBStructure.ORDER_TABLE_FIELD_CLIENT_ID,
              DBStructure.ORDER_TABLE_FIELD_CAR_ID)
    d1 = datetime.strptime('1/1/2017 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/11/2018 4:50 AM', '%m/%d/%Y %I:%M %p')
    start_time = random_date(d1, d2)
    end_time = random_date(start_time, start_time + timedelta(hours=4))
    # price is in dollars
    values = (uniform(-90, 90), uniform(-180, 180), uniform(-90, 90), uniform(-180, 180),
              start_time, end_time, randint(10, 500), randint(1, 5), manager_id, client_id, car_id)
    exec_insert_query(cursor, table_name, fields, values)


def gen_payment(cursor, order_id):
    table_name = DBStructure.PAYMENT_TABLE_NAME
    fields = (DBStructure.PAYMENT_TABLE_FIELD_ORDER_ID, DBStructure.PAYMENT_TABLE_FIELD_HASH_CREDIT_CARD)
    values = (order_id, ''.join(random.choice(string.digits + string.ascii_letters) for i in range(254)))
    exec_insert_query(cursor, table_name, fields, values)


def gen_1st_query_data(cursor):
    return


def gen_random_data(cursor, n):
    for i in range(n):
        gen_random_client(cursor)
        client_id = cursor.lastrowid
        gen_random_car_model(cursor)
        model_id = cursor.lastrowid
        gen_random_car(cursor, model_id)
        car_id = cursor.lastrowid
        gen_random_video(cursor, model_id)
        gen_random_location(cursor)
        loc_id = cursor.lastrowid
        bind_usr_loc(cursor, client_id, loc_id)
        gen_random_manager(cursor)
        manager_id = cursor.lastrowid
        gen_order(cursor, manager_id, client_id, car_id)
        order_id = cursor.lastrowid
        gen_payment(cursor, order_id)


def gen_data():
    conn = sqlite3.connect(DBStructure.DB_FILENAME)
    cursor = conn.cursor()
    gen_1st_query_data(cursor)
