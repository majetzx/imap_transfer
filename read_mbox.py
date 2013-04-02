# -*- coding: UTF-8 -*-
# Opens mbox files in a directory, retrieves messages and adds them in the database

# mbox files directory
path = 'mboxes'
# Originating email address
origin = 'user@example.net'
# SQLite database
database = 'global.db'

import imap_utils
import os, re, sqlite3

db = sqlite3.connect(database)
c = db.cursor()

mbox_list = os.listdir(path)
for f in mbox_list:
    # an mbox file must begin with "mbox_"
    if re.match('mbox_', f):
        imap_utils.open_mbox(path + '/' + f, c, origin)

db.commit()
c.close()
db.close()
