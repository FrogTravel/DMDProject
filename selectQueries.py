import DBStructure

RED_CAR = 'SELECT ' + DBStructure.ALL_CARS_FIELD_MANUFACTURE + ', All_Cars.' + DBStructure.ALL_CARS_FIELD_NUMBER + """
                FROM """ + DBStructure.ALL_CARS_TABLE_NAME + ', ' + DBStructure.CAR_TABLE_NAME + ', ' + DBStructure.ORDER_TABLE_NAME\
                + ' WHERE color="red" AND All_Cars.number LIKE "AN%"' \
                + 'AND ac_id = All_cars.id AND UID = car_id AND ' \
                + 'start_time >= date("2017-05-13") AND start_time < date("2017-05-13", "+1 day")'

ALL_CARS = 'SELECT COUNT(' + DBStructure.ALL_CARS_FIELD_ID + \
            ') FROM ' + DBStructure.ALL_CARS_TABLE_NAME