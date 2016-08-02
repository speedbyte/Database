#!/usr/bin/env python
import dbc
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data = data.split("\n")
    ts= data[0][4:]
    ACC_X = data[1][4:]
    ACC_Y = data[2][4:]
    ACC_Z = data[3][4:]
    MAG_X = data[4][4:]
    MAG_Y = data[5][4:]
    MAG_Z = data[6][4:]
    G_ROLL = data[9][4:]
    G_PITCH = data[8][4:]
    G_YAW = data[7][4:]
    TEMP = data[10][4:]
    PRESS = data[11][4:]
    M1 = data[12][4:]
    M2 = data[13][4:]
    M3 = data[14][4:]
    M4 = data[15][4:]
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
