# -*- coding: UTF-8 -*-
# Empties an IMAP mailbox of all its messages

# IMAP server
server = 'mail.example.net'
# IMAP identifier
user = 'user@example.net'
# IMAP password
password = 'pwd'
# IMAP mailbox containing messages
folder = 'INBOX'

import imaplib

imap = imaplib.IMAP4_SSL(server)
imap.login(user, password)
print '%s...' % user

try:
    imap.select(folder)
    # searches for all messages and marks them as Deleted
    typ, [msg_ids] = imap.search(None, 'ALL')
    msg_ids = ','.join(msg_ids.split(' '))
    imap.store(msg_ids, '+FLAGS', r'(\Deleted)')
    imap.expunge()

finally:
    try:
        imap.close()
    except:
        pass
    imap.logout()
