# -*- coding: UTF-8 -*-
#

# IMAP server
server = 'mail.example.net'
# IMAP identifier
user = 'user@example.net'
# IMAP password
password = 'pwd'
# IMAP mailbox containing messages
folder = 'Trash'
# Originating email address
origin = user

import imap_utils
import imaplib, email
from email.header import decode_header, make_header

imap = imaplib.IMAP4_SSL(server)
imap.login(user, password)
print '%s...' % user

try:
    imap.select(folder, readonly=True)
    # searches for all messages and get the RFC822 version of the message
    typ, msg_ids = imap.search(None, 'ALL')
    nb = nb_sans = 0
    for msg_id in msg_ids[0].split():
        nb += 1
        typ, msg_data = imap.fetch(msg_id, '(RFC822)')
        # the text version is converted into a message object structure
        msg = email.message_from_string(msg_data[0][1].strip())
        if msg.has_key('X-Spam-Level') & (msg.get('X-Spam-Level') == ''):
            nb_sans += 1
            hdr = decode_header(msg.get('Subject'))
            default_charset = 'ASCII'
            print '> ' + msg.get('From')

finally:
    try:
        imap.close()
    except:
        pass
    imap.logout()

print '{0:d} en tout, {1:d} sans'.format(nb, nb_sans)