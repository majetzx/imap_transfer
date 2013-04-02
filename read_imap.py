# -*- coding: UTF-8 -*-
# Opens an IMAP mailbox, retrieves messages and adds them in the database

# IMAP server
server = 'mail.example.net'
# IMAP identifier
user = 'user@example.net'
# IMAP password
password = 'pwd'
# IMAP mailbox containing messages
folder = 'INBOX'
# Originating email address
origin = user
# SQLite database
database = 'global.db'

import imap_utils
import imaplib, email, sqlite3

db = sqlite3.connect(database)
c = db.cursor()

imap = imaplib.IMAP4_SSL(server)
imap.login(user, password)
print '%s...' % user

try:
    imap.select(folder, readonly=True)
    # searches for all messages and get the RFC822 version of the message
    typ, msg_ids = imap.search(None, 'ALL')
    for msg_id in msg_ids[0].split():
        typ, msg_data = imap.fetch(msg_id, '(RFC822)')
        # the text version is converted into a message object structure
        msg = email.message_from_string(msg_data[0][1].strip())
        imap_utils.add_msg(msg, c, origin)
        db.commit()

finally:
    try:
        imap.close()
    except:
        pass
    imap.logout()

c.close()
db.close()
