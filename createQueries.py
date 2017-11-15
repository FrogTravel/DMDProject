import DBStructure

# I have NOT NULL everywhere, not sure this is right

# what the fuck is state field?!
# what is start_time and end_time types
# satisfaction might be like byte, and it might be null actually, Yay
# TODO solve ID that is foreign key. Also order is the weak entity
# TODO accept is weak many-to-one relationship with car
# TODO supervice strong rel, many-to-one with manager
CREATE_ORDER = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.ORDER_TABLE_NAME + ' (' \
               + DBStructure.ORDER_TABLE_FIELD_ID + ' integer AUTOINCREMENT,' \
               + DBStructure.ORDER_TABLE_FIELD_STARTING_POSITION + ' varchar(255) NOT NULL,' \
               + DBStructure.ORDER_TABLE_FIELD_DESTINATION + ' varchar(255) NOT NULL' \
               + DBStructure.ORDER_TABLE_FIELD_STATE + ' varchar(255) NOT NULL' \
               + DBStructure.ORDER_TABLE_FIELD_START_TIME + ' varchar(255) NOT NULL,' \
               + DBStructure.ORDER_TABLE_FIELD_END_TIME + ' varchar(255) NOT NULL,' \
               + DBStructure.ORDER_TABLE_FIELD_PRICE + ' integer NOT NULL, ' \
               + DBStructure.ORDER_TABLE_FIELD_SATISFACTION + ' integer' \
                                                              ');'

# TODO 'lives at' is 0...N to 1..N relationship
# AM... No Primary key at this table, so let it be some ID
CREATE_LOCATION = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.LOCATION_TABLE_NAME + ' (' \
                  + DBStructure.LOCATION_TABLE_FIELD_ID + ' integer PRIMARY KEY AUTOINCREMENT,' \
                  + DBStructure.LOCATION_TABLE_FIELD_COUNTRY + ' varchar(255) NOT NULL, ' \
                  + DBStructure.LOCATION_TABLE_FIELD_ZIP + ' varchar(8) NOT NULL,' \
                  + DBStructure.LOCATION_TABLE_FIELD_CITY + ' varchar(255) NOT NULL' \
                                                            ');'

# TODO Order to Client relationship 'manage(create/cancel)' is weak 0..n to 1
# Are you sure we need username as primary key, I use ID
# Not sure DATA is the right one
CREATE_CLIENT = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.CLIENT_TABLE_NAME + ' (' \
                + DBStructure.CLIENT_TABLE_FIELD_ID + ' integer PRIMARY KEY AUTOINCREMENT,' \
                + DBStructure.CLIENT_TABLE_FIELD_USERNAME + ' varchar(255) NOT NULL, ' \
                + DBStructure.CLIENT_TABLE_FIELD_DATE_OF_BIRTH + ' DATA NOT NULL' \
                                                                 ');'

# what are sizes of number and model fields?
# maybe location must be splited to langitude latitude, because else what is type of this shit?
# TODO 'make order' weak relationship one-to-many with weak entity charge-order
# TODO 'record' weak relationship one-to-many with weak entity Video
CREATE_CAR = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.CAR_TABLE_NAME + ' (' \
             + DBStructure.CAR_TABLE_FIELD_UID + ' integer PRIMARY KEY AUTOINCREMENT,' \
             + DBStructure.CAR_TABLE_FIELD_NUMBER + ' varchar(10) NOT NULL, ' \
             + DBStructure.CAR_TABLE_FIELD_MODEL + ' varchar(10) NOT NULL,' \
             + DBStructure.CAR_TABLE_FIELD_CHARGE_LEVEL + ' varchar(10) NOT NULL,' \
             + DBStructure.CAR_TABLE_FIELD_LOCATION + ' varchar(10) NOT NULL' \
                                                      ');'

# same problem with start_time
# what is the type of content
# TODO ID is foreign key
# TODO Video is weak entity
CREATE_VIDEO = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.VIDEO_TABLE_NAME + ' (' \
               + DBStructure.VIDEO_TABLE_FIELD_ID + ' integer PRIMARY KEY AUTOINCREMENT,' \
               + DBStructure.VIDEO_TABLE_FIELD_DURATION + ' integer NOT NULL, ' \
               + DBStructure.VIDEO_TABLE_FIELD_START_TIME + ' varchar(255) NOT NULL,' \
               + DBStructure.VIDEO_TABLE_FIELD_CONTENT + ' varchar(255) NOT NULL' \
                                                         ');'

# TODO 'accept' is weak relationship many-to-one with Charger
# TODO weak entity
CREATE_CHARGE_ORDER = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.CHARGE_ORDER_TABLE_NAME + ' (' \
                      + DBStructure.CHARGE_ORDER_TABLE_FIELD_ID + ' integer PRIMARY KEY AUTOINCREMENT,' \
                      + DBStructure.CHARGE_ORDER_TABLE_FIELD_CHARGE_TIME + ' varchar(255) NOT NULL, ' \
                      + DBStructure.CHARGE_ORDER_TABLE_FIELD_ARRIVAL_TIME + ' DATA NOT NULL,' \
                      + DBStructure.CHARGE_ORDER_TABLE_FIELD_AMOUNT_OF_TAKEN_ENERGY + ' integer NOT NULL' \
                                                                                      ');'

# TODO weak entity
# Again, what is the type of location, may be we should change it to lat lang
CREATE_CHARGER = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.CHARGER_TABLE_NAME + ' (' \
                 + DBStructure.CHARGER_TABLE_FIELD_LOCATION + ' varchar(255) NOT NULL,' \
                 + DBStructure.CHARGER_TABLE_FIELD_ID + ' integer PRIMARY KEY AUTOINCREMENT,' \
                 + DBStructure.CHARGER_TABLE_FIELD_TOTAL_AMOUNT_OF_CHARGERS + ' integer NOT NULL,' \
                 + DBStructure.CHARGER_TABLE_FIELD_AMOUNT_OF_FREE_CHARGERS + ' integer NOT NULL' \
                                                                             ');'

# TODO Relationship 'manage(ban/restrict)' is 1..N to 0..N
CREATE_MANAGER = 'CREATE TABLE IF NOT EXISTS ' + DBStructure.MANAGER_TABLE_NAME + ' (' \
                 + DBStructure.MANAGER_TABLE_FIELD_ID + 'integer PRIMARY KEY AUTOINCREMENT,' \
                 + DBStructure.MANAGER_TABLE_FIELD_NAME + ' varchar(255) NOT NULL' \
                                                          ');'
