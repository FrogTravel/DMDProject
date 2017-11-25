import DBStructure

CREATE_ORDER = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.ORDER_TABLE_NAME + ' (' \
               + DBStructure.ORDER_TABLE_FIELD_ID + ' integer PRIMARY KEY,' \
               + DBStructure.ORDER_TABLE_FIELD_STARTING_POSITION_LAT + ' real NOT NULL, ' \
               + DBStructure.ORDER_TABLE_FIELD_STARTING_POSITION_LNG + ' real NOT NULL, ' \
               + DBStructure.ORDER_TABLE_FIELD_DESTINATION_LAT + ' real NOT NULL, ' \
               + DBStructure.ORDER_TABLE_FIELD_DESTINATION_LNG + ' real NOT NULL, ' \
               + DBStructure.ORDER_TABLE_FIELD_START_TIME + ' datetime NOT NULL,' \
               + DBStructure.ORDER_TABLE_FIELD_END_TIME + ' datetime NOT NULL,' \
               + DBStructure.ORDER_TABLE_FIELD_PRICE + ' integer NOT NULL, ' \
               + DBStructure.ORDER_TABLE_FIELD_SATISFACTION + ' integer, ' \
               + DBStructure.ORDER_TABLE_FIELD_MANAGER_ID + ' integer NOT NULL REFERENCES ' \
               + DBStructure.MANAGER_TABLE_NAME + ', ' \
               + DBStructure.ORDER_TABLE_FIELD_CLIENT_ID + ' integer NOT NULL REFERENCES ' \
               + DBStructure.CLIENT_TABLE_NAME + ', ' \
               + DBStructure.ORDER_TABLE_FIELD_STATE + ' varchar(255) NOT NULL ' \
                                                       ');'

CREATE_LOCATION = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.LOCATION_TABLE_NAME + ' (' \
                  + DBStructure.LOCATION_TABLE_FIELD_ID + ' integer PRIMARY KEY,' \
                  + DBStructure.LOCATION_TABLE_FIELD_COUNTRY + ' varchar(255) NOT NULL, ' \
                  + DBStructure.LOCATION_TABLE_FIELD_ZIP + ' varchar(10) NOT NULL,' \
                  + DBStructure.LOCATION_TABLE_FIELD_CITY + ' varchar(255) NOT NULL' \
                                                            ');'

CREATE_CLIENT = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.CLIENT_TABLE_NAME + ' (' \
                + DBStructure.CLIENT_TABLE_FIELD_ID + ' integer PRIMARY KEY,' \
                + DBStructure.CLIENT_TABLE_FIELD_USERNAME + ' varchar(255) NOT NULL, ' \
                + DBStructure.CLIENT_TABLE_FIELD_DATE_OF_BIRTH + ' DATA NOT NULL' \
                                                                 ');'

CREATE_CAR_LOG = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.CAR_LOG_TABLE_NAME + ' (' \
                 + DBStructure.CAR_LOG_TABLE_FIELD_CHARGE_LEVEL + ' real NOT NULL,' \
                 + DBStructure.CAR_LOG_TABLE_FIELD_LAT + ' real NOT NULL,' \
                 + DBStructure.CAR_LOG_TABLE_FIELD_LNG + ' real NOT NULL,' \
                 + DBStructure.CAR_LOG_TABLE_FIELD_TIME + ' datetime NOT NULL, ' \
                 + DBStructure.CAR_LOG_TABLE_FIELD_ORDER_ID + ' integer NOT NULL REFERENCES ' \
                 + DBStructure.ORDER_TABLE_NAME + ',' \
                 + DBStructure.CAR_LOG_TABLE_FIELD_ALL_CARS + ' integer NOT NULL REFERENCES ' \
                 + DBStructure.ALL_CARS_TABLE_NAME + ', ' \
                                                     'PRIMARY KEY (' \
                 + DBStructure.CAR_LOG_TABLE_FIELD_ALL_CARS + ', ' \
                 + DBStructure.CAR_LOG_TABLE_FIELD_TIME + ')' \
                                                  ');'


CREATE_VIDEO = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.VIDEO_TABLE_NAME + ' (' \
               + DBStructure.VIDEO_TABLE_FIELD_DURATION + ' integer NOT NULL, ' \
               + DBStructure.VIDEO_TABLE_FIELD_START_TIME + ' varchar(255) NOT NULL,' \
               + DBStructure.VIDEO_TABLE_FIELD_ALL_CARS_ID + ' integer NOT NULL REFERENCES ' \
               + DBStructure.ALL_CARS_TABLE_NAME + ', ' \
               + DBStructure.VIDEO_TABLE_FIELD_CONTENT + ' varchar(255) NOT NULL,' \
                                                         ' PRIMARY KEY (' \
               + DBStructure.VIDEO_TABLE_FIELD_START_TIME + ', ' \
               + DBStructure.VIDEO_TABLE_FIELD_ALL_CARS_ID + ')' \
                                                             ');' \

CREATE_REFILL_STATION = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.REFILL_STATION_TABLE_NAME + ' (' \
                        + DBStructure.REFILL_STATION_TABLE_FIELD_ID + ' integer PRIMARY KEY,' \
                        + DBStructure.REFILL_STATION_TABLE_FIELD_LAT + ' real NOT NULL, ' \
                        + DBStructure.REFILL_STATION_TABLE_FIELD_LNG + ' real NOT NULL, ' \
                        + DBStructure.REFILL_STATION_TABLE_FIELD_TOTAL_AMOUNT_OF_CHARGERS + ' integer NOT NULL ' \
                                                                                            ');'

CREATE_REFILL_STATION_HISTORY = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.REFILL_STATION_HISTORY_TABLE_NAME + ' (' \
                                + DBStructure.REFILL_STATION_HISTORY_TABLE_FIELD_REFILL_STATION_ID + ' integer NOT NULL REFERENCES ' \
                                + DBStructure.REFILL_STATION_TABLE_NAME + ', ' \
                                + DBStructure.REFILL_STATION_HISTORY_TABLE_FIELD_TIME + ' datetime NOT NULL,' \
                                + DBStructure.REFILL_STATION_HISTORY_TABLE_FIELD_AMOUNT_OF_OCCUPIED_CHARGER + ' integer NOT NULL,' \
                                                                                                          ' PRIMARY KEY ( ' \
                                + DBStructure.REFILL_STATION_HISTORY_TABLE_FIELD_REFILL_STATION_ID + ',' \
                                + DBStructure.REFILL_STATION_HISTORY_TABLE_FIELD_TIME + ')' \
                                                                                        ');'
#
CREATE_MANAGER = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.MANAGER_TABLE_NAME + ' (' \
                 + DBStructure.MANAGER_TABLE_FIELD_ID + ' integer PRIMARY KEY,' \
                 + DBStructure.MANAGER_TABLE_FIELD_NAME + ' varchar(255) NOT NULL, ' \
                 + DBStructure.MANAGER_TABLE_PHONE + ' varchar(255) NOT NULL ' \
                                                     ');'

CREATE_LIVES_AT_RELATION_TABLE = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.RELATION_TABLE_LIVES_AT_NAME + ' (' \
                                 + DBStructure.RELATION_TABLE_FIELD_LIVES_AT_LOCATION_ID + ' integer NOT NULL, ' \
                                 + DBStructure.RELATION_TABLE_FIELD_LIVES_AT_CLIENT_ID + ' integer NOT NULL,' \
                                                                                         'PRIMARY KEY (' \
                                 + DBStructure.RELATION_TABLE_FIELD_LIVES_AT_CLIENT_ID + ', ' \
                                 + DBStructure.RELATION_TABLE_FIELD_LIVES_AT_LOCATION_ID + '),' \
                                                                                           'FOREIGN KEY (' \
                                 + DBStructure.RELATION_TABLE_FIELD_LIVES_AT_CLIENT_ID + ') REFERENCES ' \
                                 + DBStructure.CLIENT_TABLE_NAME + ', ' \
                                                                   'FOREIGN KEY (' \
                                 + DBStructure.RELATION_TABLE_FIELD_LIVES_AT_LOCATION_ID + ') REFERENCES ' \
                                 + DBStructure.LOCATION_TABLE_NAME + '' \
                                                                     '); '

CREATE_ALL_CARS = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.ALL_CARS_TABLE_NAME + ' (' \
                  + DBStructure.ALL_CARS_FIELD_ID + ' integer PRIMARY KEY, ' \
                  + DBStructure.ALL_CARS_FIELD_COLOR + ' varchar(255) NOT NULL, ' \
                  + DBStructure.ALL_CARS_FIELD_MODEL + ' varchar(255) NOT NULL,' \
                  + DBStructure.ALL_CARS_FIELD_NUMBER + ' varchar(255) NOT NULL ' \
                                                        ');'

CREATE_PAYMENT = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.PAYMENT_TABLE_NAME + ' (' \
                 + DBStructure.PAYMENT_TABLE_FIELD_ORDER_ID + ' integer NOT NULL REFERENCES ' \
                 + DBStructure.ORDER_TABLE_NAME + ',' \
                 + DBStructure.PAYMENT_TABLE_FIELD_HASH_CREDIT_CARD + ' varchar(255) NOT NULL,' \
                                                                      'PRIMARY KEY (' \
                 + DBStructure.PAYMENT_TABLE_FIELD_ORDER_ID + ')' \
                                                              ');'
