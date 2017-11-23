import DBStructure

# I have NOT NULL everywhere, not sure this is right

# what the fuck is state field?!
# what is start_time and end_time types
# satisfaction might be like byte, and it might be null actually, Yay
# TODO solve ID that is foreign key. Also order is the weak entity
# TODO accept is weak many-to-one relationship with car
# TODO supervice strong rel, many-to-one with manager
# TODO Not sure that manager id is not null...
CREATE_ORDER = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.ORDER_TABLE_NAME + ' (' \
               + DBStructure.ORDER_TABLE_FIELD_ID + ' integer PRIMARY KEY,' \
               + DBStructure.ORDER_TABLE_FIELD_STARTING_POSITION + ' varchar(255) NOT NULL,' \
               + DBStructure.ORDER_TABLE_FIELD_DESTINATION + ' varchar(255) NOT NULL, ' \
               + DBStructure.ORDER_TABLE_FIELD_START_TIME + ' datetime NOT NULL,' \
               + DBStructure.ORDER_TABLE_FIELD_END_TIME + ' datetime NOT NULL,' \
               + DBStructure.ORDER_TABLE_FIELD_PRICE + ' integer NOT NULL, ' \
               + DBStructure.ORDER_TABLE_FIELD_SATISFACTION + ' integer, ' \
               + DBStructure.ORDER_TABLE_FIELD_MANAGER_ID + ' integer NOT NULL REFERENCES ' \
               + DBStructure.MANAGER_TABLE_NAME + ', ' \
               + DBStructure.ORDER_TABLE_FIELD_CLIENT_ID + ' integer NOT NULL REFERENCES ' \
               + DBStructure.CLIENT_TABLE_NAME + ', ' \
               + DBStructure.ORDER_TABLE_FIELD_CAR_ID + ' integer NOT NULL REFERENCES ' \
               + DBStructure.CAR_TABLE_NAME + ', ' \
               + DBStructure.ORDER_TABLE_FIELD_STATE_ID + ' integer NOT NULL REFERENCES ' \
               + DBStructure.STATE_TABLE_NAME + '' \
                                                ');'

# TODO 'lives at' is 0...N to 1..N relationship
# AM... No Primary key at this table, so let it be some ID
CREATE_LOCATION = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.LOCATION_TABLE_NAME + ' (' \
                  + DBStructure.LOCATION_TABLE_FIELD_ID + ' integer PRIMARY KEY,' \
                  + DBStructure.LOCATION_TABLE_FIELD_COUNTRY + ' varchar(255) NOT NULL, ' \
                  + DBStructure.LOCATION_TABLE_FIELD_ZIP + ' varchar(8) NOT NULL,' \
                  + DBStructure.LOCATION_TABLE_FIELD_CITY + ' varchar(255) NOT NULL' \
                                                            ');'

# TODO Order to Client relationship 'manage(create/cancel)' is weak 0..n to 1
# Are you sure we need username as primary key, I use ID
# Not sure DATA is the right one
CREATE_CLIENT = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.CLIENT_TABLE_NAME + ' (' \
                + DBStructure.CLIENT_TABLE_FIELD_ID + ' integer PRIMARY KEY,' \
                + DBStructure.CLIENT_TABLE_FIELD_USERNAME + ' varchar(255) NOT NULL, ' \
                + DBStructure.CLIENT_TABLE_FIELD_DATE_OF_BIRTH + ' DATA NOT NULL' \
                                                                 ');'

# what are sizes of number and model fields?
# maybe location must be splited to langitude latitude, because else what is type of this shit?
# TODO 'make order' weak relationship one-to-many with weak entity charge-order
# TODO 'record' weak relationship one-to-many with weak entity Video
CREATE_CAR = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.CAR_TABLE_NAME + ' (' \
             + DBStructure.CAR_TABLE_FIELD_UID + ' integer PRIMARY KEY,' \
             + DBStructure.CAR_TABLE_FIELD_CHARGE_LEVEL + ' varchar(10) NOT NULL,' \
             + DBStructure.CAR_TABLE_FIELD_LOCATION + ' varchar(10) NOT NULL,' \
             + DBStructure.CAR_TABLE_LAT + ' real NOT NULL,' \
             + DBStructure.CAR_TABLE_LNG + ' real NOT NULL,' \
             + DBStructure.CAR_TABLE_ALL_CARS + ' integer NOT NULL REFERENCES ' \
             + DBStructure.ALL_CARS_TABLE_NAME + '' \
                                                 ');'

# same problem with start_time
# what is the type of content
# TODO ID is foreign key
# TODO Video is weak entity
CREATE_VIDEO = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.VIDEO_TABLE_NAME + ' (' \
               + DBStructure.VIDEO_TABLE_FIELD_ID + ' integer PRIMARY KEY,' \
               + DBStructure.VIDEO_TABLE_FIELD_DURATION + ' integer NOT NULL, ' \
               + DBStructure.VIDEO_TABLE_FIELD_START_TIME + ' varchar(255) NOT NULL,' \
               + DBStructure.VIDEO_TABLE_FIELD_ALL_CARD_ID + ' integer NOT NULL REFERENCES ' \
               + DBStructure.ALL_CARS_TABLE_NAME + ', ' \
               + DBStructure.VIDEO_TABLE_FIELD_CONTENT + ' varchar(255) NOT NULL' \
                                                         ');'

# TODO 'accept' is weak relationship many-to-one with Charger
# TODO weak entity
CREATE_REFILL_STATION = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.REFILL_STATION_TABLE_NAME + ' (' \
                        + DBStructure.REFILL_STATION_TABLE_FIELD_ID + ' integer PRIMARY KEY,' \
                        + DBStructure.REFILL_STATION_TABLE_FIELD_AMOUNT_OF_TAKEN_ENERGY + ' integer NOT NULL, ' \
                        + DBStructure.REFILL_STATION_TABLE_FIELD_LAT + ' real NOT NULL, ' \
                        + DBStructure.REFILL_STATION_TABLE_FIELD_LNG + ' real NOT NULL, ' \
                        + DBStructure.REFILL_STATION_TABLE_FIELD_TOTAL_AMOUNT_OF_CHARGERS + ' integer NOT NULL, ' \
                        + DBStructure.REFILL_STATION_TABLE_FIELD_AMOUNT_OF_FREE_CHARGERS + ' integer NOT NULL ' \
                                                                                           ');'

CREATE_CHARGE_EVENT = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.CHARGE_EVENT_TABLE_NAME + ' (' \
                      + DBStructure.CHARGE_EVENT_TABLE_FIELD_ID + ' integer PRIMARY KEY,' \
                      + DBStructure.CHARGE_EVENT_TABLE_FIELD_CAR_ID + ' integer NOT NULL REFERENCES ' \
                      + DBStructure.ALL_CARS_TABLE_NAME + ',' \
                      + DBStructure.CHARGE_EVENT_TABLE_FIELD_REFILL_STATION_ID + ' integer NOT NULL REFERENCES ' \
                      + DBStructure.REFILL_STATION_TABLE_NAME + ', ' \
                      + DBStructure.CHARGE_EVENT_TABLE_FIELD_COST + ' integer NOT NULL,' \
                      + DBStructure.CHARGE_EVENT_TABLE_FIELD_DATE + ' datetime NOT NULL,' \
                      + DBStructure.CHARGE_EVENT_TABLE_FIELD_CHARGE_TIME + ' integer NOT NULL, ' \
                      + DBStructure.CHARGE_EVENT_TABLE_FIELD_ARRIVAL_TIME + ' datetime NOT NULL ' \
                                                                            ');'

CREATE_MANAGER = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.MANAGER_TABLE_NAME + ' (' \
                 + DBStructure.MANAGER_TABLE_FIELD_ID + ' integer PRIMARY KEY,' \
                 + DBStructure.MANAGER_TABLE_FIELD_NAME + ' varchar(255) NOT NULL, ' \
                 + DBStructure.MANAGER_TABLE_PHONE + ' varchar(255) NOT NULL ' \
                                                     ');'

CREATE_LIVES_AT_RELATION_TABLE = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.RELATION_TABLE_LIVES_AT_NAME + ' (' \
                                 + DBStructure.RELATION_TABLE_LIVES_AT_LOCATION_ID + ' integer NOT NULL, ' \
                                 + DBStructure.RELATION_TABLE_LIVES_AT_CLIENT_ID + ' integer NOT NULL,' \
                                                                                   'PRIMARY KEY (' \
                                 + DBStructure.RELATION_TABLE_LIVES_AT_CLIENT_ID + ', ' \
                                 + DBStructure.RELATION_TABLE_LIVES_AT_LOCATION_ID + '),' \
                                                                                     'FOREIGN KEY (' \
                                 + DBStructure.RELATION_TABLE_LIVES_AT_CLIENT_ID + ') REFERENCES ' \
                                 + DBStructure.CLIENT_TABLE_NAME + ', ' \
                                                                   'FOREIGN KEY (' \
                                 + DBStructure.RELATION_TABLE_LIVES_AT_LOCATION_ID + ') REFERENCES ' \
                                 + DBStructure.LOCATION_TABLE_NAME + '' \
                                                                     '); '

CREATE_STATE = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.STATE_TABLE_NAME + ' (' \
               + DBStructure.STATE_TABLE_FIELD_ID + ' integer PRIMARY KEY, ' \
               + DBStructure.STATE_TABLE_FIELD_STATE_NAME + ' varchar(255) NOT NULL' \
                                                            ');'

CREATE_ALL_CARS = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.ALL_CARS_TABLE_NAME + ' (' \
                  + DBStructure.ALL_CARS_FIELD_ID + ' integer PRIMARY KEY, ' \
                  + DBStructure.ALL_CARS_FIELD_COLOR + ' varchar(255) NOT NULL, ' \
                  + DBStructure.ALL_CARS_FIELD_MANUFACTURE + ' varchar(255) NOT NULL, ' \
                                                             '' \
                  + DBStructure.ALL_CARS_FIELD_NUMBER + ' varchar(255) NOT NULL ' \
                                                        ');'

CREATE_PAYMENT = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.PAYMENT_TABLE_NAME + ' (' \
                 + DBStructure.PAYMENT_TABLE_FIELD_ID + ' integer PRIMARY KEY,' \
                 + DBStructure.PAYMENT_TABLE_FIELD_ORDER_ID + ' integer NOT NULL REFERENCES ' \
                 + DBStructure.ORDER_TABLE_NAME + ',' \
                 + DBStructure.PAYMENT_TABLE_FIELD_HASH_CREDIT_CARD + ' varchar(255) NOT NULL' \
                                                                                     ');'
