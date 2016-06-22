#!/usr/bin/env python
import dbc
import time
import random

dbc.db.query("""SELECT COUNT(*) FROM `Data`;""")
count = (dbc.db.store_result().fetch_row()[0])[0]

t = time.time()

for i in range(0, 5000-count):
    #Sys. time in UNIX epoch
    ts = str(t+i*.01)
    #random ACC values
    ACC_X = str(random.randint(-25500,25500)*0.01)
    ACC_Y = str(random.randint(-25500,25500)*0.01)
    ACC_Z = str(random.randint(-25500,25500)*0.01)
    #random MAG values
    MAG_X = str(random.randint(-25500,25500)*0.01)
    MAG_Y = str(random.randint(-25500,25500)*0.01)
    MAG_Z = str(random.randint(-25500,25500)*0.01)
    #random GYRO values
    G_YAW = str(random.randint(-25500,25500)*0.01)
    G_PITCH = str(random.randint(-25500,25500)*0.01)
    G_ROLL= str(random.randint(-25500,25500)*0.01)
    #random TEMP and PRESS values
    TEMP = str(random.randint(-25500,25500)*0.01)
    PRESS = str(random.randint(-25500,25500)*0.01)
    #ramdom MOTOR values
    M1 = str(random.randint(-25500,25500)*0.01)
    M2 = str(random.randint(-25500,25500)*0.01)
    M3 = str(random.randint(-25500,25500)*0.01)
    M4 = str(random.randint(-25500,25500)*0.01)
    #inserting data into DB
    dbc.db.query("""
    INSERT INTO `SenseData`.`DATA`
    (`PITIME`,
    `ACC_X`,`ACC_Y`,`ACC_Z`,
    `MAG_X`,`MAG_Y`,`MAG_Z`,
    `G_ROLL`,`G_PITCH`,`G_YAW`,
    `TEMP`,`PRESS`,
    `M1`,`M2`,`M3`,`M4`)
    VALUES
    (FROM_UNIXTIME("""+ts+"""),
    """+ACC_X+""","""+ACC_Y+""","""+ACC_Z+""",
    """+MAG_X+""","""+MAG_Y+""","""+MAG_Z+""",
    """+G_ROLL+""","""+G_PITCH+""","""+G_YAW+""",
    """+TEMP+""","""+PRESS+""",
    """+M1+""","""+M2+""","""+M3+""","""+M4+""");
    """)

dbc.db.commit()
dbc.db.close()
