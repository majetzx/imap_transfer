# -*- coding: UTF-8 -*-
# Adds all messages stored in the SQLite to an IMAP mailbox

# IMAP server
server = 'mail.example.net'
# IMAP identifier
user = 'user@example.net'
# IMAP password
password = 'pwd'
# SQLite database
database = 'global.db'

import sqlite3, imaplib

db = sqlite3.connect(database)
db.text_factory = str # TEXT datatypes in the DB are returned as string
c = db.cursor()

imap = imaplib.IMAP4_SSL(server)
imap.login(user, password)
print '%s...' % user

try:
    c.execute('SELECT umid, date, orig, sent, text FROM messages ORDER BY date')
    for row in c:
        date = imaplib.Time2Internaldate(row[1])
        box = 'Sent' if row[3] == 1 else 'INBOX'
        print " %4d: %s - %s" % (row[0], date, row[2])
        # the message is added to the mailbox as already Seen
        imap.append(box, r'(\Seen)', date, row[4])

finally:
    try:
        imap.close()
    except:
        pass
    imap.logout()

c.close()
db.close()
