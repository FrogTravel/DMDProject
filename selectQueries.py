import DBStructure

RED_CAR = 'SELECT ' + DBStructure.ALL_CARS_FIELD_MODEL + ', All_Cars.' + DBStructure.ALL_CARS_FIELD_NUMBER + """
                FROM """ + DBStructure.ALL_CARS_TABLE_NAME + ', ' + DBStructure.CAR_LOG_TABLE_NAME\
                + ' WHERE color="red" AND All_Cars.number LIKE "AN%"' \
                + 'AND ac_id = All_cars.id AND ' \
                + 'time >= date("2017-05-13") AND time < date("2017-05-13", "+1 day")'

ALL_CARS = 'SELECT COUNT(' + DBStructure.ALL_CARS_FIELD_ID + \
            ') FROM ' + DBStructure.ALL_CARS_TABLE_NAME

CHARGERS = 'SELECT ' + DBStructure.REFILL_STATION_HISTORY_TABLE_FIELD_AMOUNT_OF_OCCUPIED_CHARGER + \
            ' FROM ' + DBStructure.REFILL_STATION_HISTORY_TABLE_NAME + \
            ' WHERE ' + DBStructure.REFILL_STATION_HISTORY_TABLE_FIELD_TIME + ' >= date(?) AND ' +\
            DBStructure.REFILL_STATION_HISTORY_TABLE_FIELD_TIME + ' < date(?, "+1 day") AND time(' +\
            DBStructure.REFILL_STATION_HISTORY_TABLE_FIELD_TIME + ") BETWEEN time(?) AND time(?)"

BUSY_TAXI = 'SELECT COUNT(DISTINCT ' + DBStructure.CAR_LOG_TABLE_FIELD_ALL_CARS +\
            ') FROM ' + DBStructure.CAR_LOG_TABLE_NAME + ', ' + DBStructure.ORDER_TABLE_NAME +\
            ' WHERE ' + DBStructure.CAR_LOG_TABLE_FIELD_ORDER_ID + " = " + DBStructure.ORDER_TABLE_FIELD_ID +\
            " AND time(" + DBStructure.ORDER_TABLE_FIELD_START_TIME + ") BETWEEN TIME(?) AND TIME(?) AND " +\
            DBStructure.CAR_LOG_TABLE_FIELD_TIME + ' >= DATE("2017-12-05") AND ' +\
            DBStructure.CAR_LOG_TABLE_FIELD_TIME + ' < DATE("2017-12-12")'

PAYMENTS = 'SELECT COUNT(' + DBStructure.ORDER_TABLE_FIELD_PRICE + \
            '), count(start_time), count(end_time) FROM ' + DBStructure.ORDER_TABLE_NAME + " A, " + DBStructure.CLIENT_TABLE_NAME +\
            " WHERE " + DBStructure.ORDER_TABLE_FIELD_START_TIME + " AND " +\
            "Client." + DBStructure.CLIENT_TABLE_FIELD_ID + " = A." + DBStructure.ORDER_TABLE_FIELD_CLIENT_ID +\
            """ AND start_time >= date('2017-09-20') AND start_time < DATE('2017-10-20') AND state = "completed" 
            GROUP BY price, start_time, end_time HAVING (COUNT(price) > 1) AND (COUNT(start_time) > 1) AND (COUNT(end_time) > 1)"""

LAZY_TAXIS = 'select sum(case when ' + DBStructure.CAR_LOG_TABLE_FIELD_ORDER_ID + ' LIKE "NULL" then 1 else 0 end) as c, '\
               + DBStructure.CAR_LOG_TABLE_FIELD_ALL_CARS + ", " + DBStructure.ALL_CARS_FIELD_NUMBER +\
               ' from Car, All_Cars group by ' + DBStructure.CAR_LOG_TABLE_FIELD_ALL_CARS + ", " + DBStructure.ALL_CARS_FIELD_NUMBER \
               + ' having c > 0 and ac_id = All_Cars.id order by c and time >= date("2017-08-01") and time < date("2017-11-01")'

def first_query(cursor):
    print("Possible car(s) for date 13/05/2017:")
    cursor.execute(RED_CAR)
    row = cursor.fetchone()
    while row is not None:
        print("Model: {0}, number {1}\n".format(row[0], row[1]))
        row = cursor.fetchone()

def second_query(cursor):
    day = input("Write the date to get the statistics (in format yyyy-mm-dd): ")
    hour = 0
    while hour != 24:
        if hour < 9:
            print("0" + repr(hour) + "h-0" + repr(hour + 1) + "h: ", end='')
            cursor.execute(CHARGERS,
                           (day, day, str("0" + str(hour) + ":00:00"), str("0" + str(hour + 1) + ":00:00")))
        elif hour == 9:
            print("0" + repr(hour) + "h-" + repr(hour + 1) + "h: ", end='')
            cursor.execute(CHARGERS,
                           (day, day, str("0" + str(hour)) + ":00:00", str(hour + 1) + ":00:00"))
        else:
            print(repr(hour) + "h-" + repr(hour + 1) + "h: ", end='')
            cursor.execute(CHARGERS, (day, day, str(hour) + ":00:00", str(hour + 1) + ":00:00"))
        count = cursor.fetchall()
        sum = 0
        i = 0
        while i < len(count):
            sum += count[i][0]
            i += 1
        print(sum)
        hour += 1
    print()

def third_query(cursor):
    cursor.execute(ALL_CARS)
    row = cursor.fetchone()
    countAllCars = row[0]

    print("% of busy taxis during week 05/12/2017-12/12/2017:\nMorning:\t Afternoon:\t\t Evening:\t")

    cursor.execute(BUSY_TAXI, ("07:00:00", "10:00:00"))
    row = cursor.fetchone()
    print(round((row[0] * 100 / countAllCars), 0), end='\t\t ')

    cursor.execute(BUSY_TAXI, ("12:00:00", "14:00:00"))
    row = cursor.fetchone()
    print(round((row[0] * 100 / countAllCars), 0), end='\t\t\t ')

    cursor.execute(BUSY_TAXI, ("15:00:00", "19:00:00"))
    row = cursor.fetchone()
    print(round((row[0] * 100 / countAllCars), 0))
    print()

def fourth_query(cursor):
    cursor.execute(PAYMENTS)
    if cursor.fetchone() is not None:
        print("Customer is right, he payed twice")
    else:
        print("No, in period 20/09/2017-20/10/2017 nothing was doubled")
    print()

def fifth_query(cursor):
    cursor.execute(ALL_CARS)
    row = cursor.fetchone()
    countCars = int(round(row[0] * 0.1))
    cursor.execute(LAZY_TAXIS)
    print("Numbers of taxis that take less orders:")
    while countCars != 0:
        row = cursor.fetchone()
        print(row[2])
        countCars -= 1
    print()

def start(cursor):
    userInput = input("Write which query you want to see the result of(number from 1 to 5):\n")
    while not userInput.__eq__("0"):
        if userInput.__eq__("1"):
            first_query(cursor)
        elif userInput.__eq__("2"):
            second_query(cursor)
        elif userInput.__eq__("3"):
            third_query(cursor)
        elif userInput.__eq__("4"):
            fourth_query(cursor)
        elif userInput.__eq__("5"):
            fifth_query(cursor)
        else:
            print("Wrong input")
        userInput = input("What is the next one? (0 for exit):\n")