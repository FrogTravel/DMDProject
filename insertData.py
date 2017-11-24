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
    query = 'INSERT INTO ' + table_name + '('
    for i in range(len(fields) - 1):
        query += fields[i] + ','
    query += fields[len(fields) - 1]
    query += ') VALUES (' + '?,' * (len(values) - 1) + '?)'
    cursor.execute(query, values)


def gen_random_location(cursor):
    table_name = DBStructure.LOCATION_TABLE_NAME
    fields = (DBStructure.LOCATION_TABLE_FIELD_COUNTRY, DBStructure.LOCATION_TABLE_FIELD_ZIP,
              DBStructure.LOCATION_TABLE_FIELD_CITY)
    values = ('RUSSIA', 'INNOPOLIS', '420500')
    exec_insert_query(cursor, table_name, fields, values)


def gen_random_refill_station(cursor):
    table_name = DBStructure.REFILL_STATION_TABLE_NAME
    fields = (DBStructure.REFILL_STATION_TABLE_FIELD_LAT, DBStructure.REFILL_STATION_TABLE_FIELD_LNG,
              DBStructure.REFILL_STATION_TABLE_FIELD_TOTAL_AMOUNT_OF_CHARGERS)
    values = (get_lat_lng()[0], get_lat_lng()[1], 20)
    exec_insert_query(cursor, table_name, fields, values)


def gen_refill_station_history(cursor, rs_id, n):
    table_name = DBStructure.REFILL_STATION_HISTORY_TABLE_NAME
    fields = (DBStructure.REFILL_STATION_HISTORY_TABLE_FIELD_REFILL_STATION_ID,
              DBStructure.REFILL_STATION_HISTORY_TABLE_FIELD_DATE,
              DBStructure.REFILL_STATION_HISTORY_TABLE_FIELD_AMOUNT_OF_FREE_CHARGER)
    d1 = datetime.strptime('8/1/2017 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('11/1/2017 4:50 AM', '%m/%d/%Y %I:%M %p')
    d = random_date(d1, d2)
    for i in range(n):
        values = (rs_id, d, randint(0, 20))
        exec_insert_query(cursor, table_name, fields, values)
        d += timedelta(hours=1)


def gen_random_client(cursor):
    d1 = datetime.strptime('1/1/1938 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/1/1998 4:50 AM', '%m/%d/%Y %I:%M %p')
    table_name = DBStructure.CLIENT_TABLE_NAME
    fields = (DBStructure.CLIENT_TABLE_FIELD_USERNAME, DBStructure.CLIENT_TABLE_FIELD_DATE_OF_BIRTH)
    values = ("sample_user_" + str(randint(1, 1000)), random_date(d1, d2))
    exec_insert_query(cursor, table_name, fields, values)


def gen_random_car(cursor):
    color = ["red", "blue", "green", "yellow", "purple", "orange", "white", "black"]
    manufacturers = ["Chevrolet", "Ford", "Toyota", "Honda", "BMW", "Nissan", "Jeep", "Hyundai"]
    number = choice(string.ascii_uppercase) + choice(string.ascii_uppercase) + str(randint(1000, 9999)) + choice(
        string.ascii_uppercase)
    table_name = DBStructure.ALL_CARS_TABLE_NAME
    fields = (DBStructure.ALL_CARS_FIELD_COLOR, DBStructure.ALL_CARS_FIELD_MODEL,
              DBStructure.ALL_CARS_FIELD_NUMBER)
    values = (choice(color), choice(manufacturers), number)
    exec_insert_query(cursor, table_name, fields, values)


def get_lat_lng():
    return uniform(55.2, 56.2), uniform(48, 50)


def gen_car_log(cursor, car_id, order_ids):
    table_name = DBStructure.CAR_LOG_TABLE_NAME
    fields = (DBStructure.CAR_LOG_TABLE_FIELD_ALL_CARS, DBStructure.CAR_LOG_TABLE_FIELD_CHARGE_LEVEL,
              DBStructure.CAR_LOG_TABLE_FIELD_LAT, DBStructure.CAR_LOG_TABLE_FIELD_LNG,
              DBStructure.CAR_LOG_TABLE_FIELD_TIME, DBStructure.CAR_LOG_TABLE_FIELD_ORDER_ID)
    d1 = datetime.strptime('8/1/2017 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('11/1/2017 4:50 AM', '%m/%d/%Y %I:%M %p')
    d = random_date(d1, d2)
    for i in range(3 * 30 * 24):
        id = "NULL"
        if uniform(0, 1) > 0.8 and len(order_ids) > 0:
            id = choice(order_ids)
            order_ids.remove(id)
        values = (car_id, 1.0, get_lat_lng()[0], get_lat_lng()[1], d, id)
        exec_insert_query(cursor, table_name, fields, values)
        d += timedelta(hours=1)


# TODO: decide what to do with charge event and refill station


def gen_random_video(cursor, car_id):
    table_name = DBStructure.VIDEO_TABLE_NAME
    d1 = datetime.strptime('8/1/2017 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('11/1/2017 4:50 AM', '%m/%d/%Y %I:%M %p')
    fields = (DBStructure.VIDEO_TABLE_FIELD_DURATION, DBStructure.VIDEO_TABLE_FIELD_START_TIME,
              DBStructure.VIDEO_TABLE_FIELD_CONTENT, DBStructure.VIDEO_TABLE_FIELD_ALL_CARS_ID)
    # duration is in ms
    values = (randint(1000, 1000000000), random_date(d1, d2), "sample_video_" + str(randint(1, 1000)) + ".avi", car_id)
    exec_insert_query(cursor, table_name, fields, values)


def gen_random_manager(cursor):
    phone = '+'.join(choice(string.digits) for i in range(11))
    table_name = DBStructure.MANAGER_TABLE_NAME
    fields = (DBStructure.MANAGER_TABLE_FIELD_NAME, DBStructure.MANAGER_TABLE_PHONE)
    values = ("sample_manager_" + str(randint(1, 1000)), phone)
    exec_insert_query(cursor, table_name, fields, values)


def bind_usr_loc(cursor, user_id, loc_id):
    table_name = DBStructure.RELATION_TABLE_LIVES_AT_NAME
    fields = (DBStructure.RELATION_TABLE_FIELD_LIVES_AT_CLIENT_ID,
              DBStructure.RELATION_TABLE_FIELD_LIVES_AT_LOCATION_ID)
    values = (user_id, loc_id)
    exec_insert_query(cursor, table_name, fields, values)


def gen_order(cursor, manager_id, client_id):
    table_name = DBStructure.ORDER_TABLE_NAME
    fields = (DBStructure.ORDER_TABLE_FIELD_STARTING_POSITION_LAT, DBStructure.ORDER_TABLE_FIELD_STARTING_POSITION_LNG,
              DBStructure.ORDER_TABLE_FIELD_DESTINATION_LAT, DBStructure.ORDER_TABLE_FIELD_DESTINATION_LNG,
              DBStructure.ORDER_TABLE_FIELD_START_TIME, DBStructure.ORDER_TABLE_FIELD_END_TIME,
              DBStructure.ORDER_TABLE_FIELD_PRICE, DBStructure.ORDER_TABLE_FIELD_SATISFACTION,
              DBStructure.ORDER_TABLE_FIELD_MANAGER_ID, DBStructure.ORDER_TABLE_FIELD_CLIENT_ID,
              DBStructure.ORDER_TABLE_FIELD_STATE)
    d1 = datetime.strptime('8/1/2017 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('11/1/2017 4:50 AM', '%m/%d/%Y %I:%M %p')
    states = ("created", "accepted", "in_process", "completed", "canceled")
    start_time = random_date(d1, d2)
    end_time = random_date(start_time, start_time + timedelta(hours=4))
    # price is in dollars
    values = (get_lat_lng()[0], get_lat_lng()[1], get_lat_lng()[0], get_lat_lng()[1],
              start_time, end_time, randint(10, 500), randint(1, 5), manager_id, client_id, states[3])
    exec_insert_query(cursor, table_name, fields, values)


def gen_payment(cursor, order_id):
    table_name = DBStructure.PAYMENT_TABLE_NAME
    fields = (DBStructure.PAYMENT_TABLE_FIELD_ORDER_ID, DBStructure.PAYMENT_TABLE_FIELD_HASH_CREDIT_CARD)
    values = (order_id, ''.join(choice(string.digits + string.ascii_letters) for i in range(254)))
    exec_insert_query(cursor, table_name, fields, values)


def gen_1st_query_data(cursor):
    return


def gen_random_data(cursor):
    order_ids = list()
    gen_random_location(cursor)
    loc_id = cursor.lastrowid
    for i in range(3000):
        gen_random_client(cursor)
        client_id = cursor.lastrowid
        bind_usr_loc(cursor, client_id, loc_id)
        gen_random_manager(cursor)
        manager_id = cursor.lastrowid
        for j in range(randint(1, 10)):
            gen_order(cursor, manager_id, client_id)
            order_id = cursor.lastrowid
            order_ids.append(order_id)
            gen_payment(cursor, order_id)
    for i in range(20):
        gen_random_car(cursor)
        car_id = cursor.lastrowid
        gen_car_log(cursor, car_id, order_ids)
        gen_random_video(cursor, car_id)
        gen_random_refill_station(cursor)
        rs_id = cursor.lastrowid
        gen_refill_station_history(cursor, rs_id, 100)