#!/usr/bin/env python
import dbc

dbc.db.query('''
TRUNCATE `SenseData`.`DATA`
''')

dbc.db.commit()
dbc.db.close()
