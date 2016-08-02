#!/usr/bin/env python
import MySQLdb
mysql_server    = 'localhost' # SERVERNAME
mysql_user      = 'PiSense'   # USERNAME
mysql_pw        = 'somePW'    # PASSWORD
mysql_db        = 'SenseData' # NAME OF THE DATABASE

global db
try:
    db = MySQLdb.connect(mysql_server,mysql_user,mysql_pw,mysql_db)
except Exception as e:
    print("Connection to the DB failed!")
