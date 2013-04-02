# -*- coding: UTF-8 -*-
# Utilities and configuration

import mailbox, email, time
from datetime import datetime
from email.header import decode_header

# List of used senders
senders = ['me@example.net']

# Analyzes an mbox file and adds messages in the database
def open_mbox(mbox, c, origin):
    print '%s...' % mbox
    for msg in mailbox.mbox(mbox):
        add_msg(msg, c, origin)
    return True

# Adds a Message object in the database
def add_msg(msg, c, origin):
    date = email.utils.parsedate_tz(msg['Date'])
    # a message without a date is problematic as their sorted by date
    if date == None:
        print "\tWARNING! date is None (%s) for next message" % msg['Date']
        date_ts = 0
    else:
        date_ts = time.mktime(date[:9])
        if date[9] != None: date_ts = date_ts - date[9]
    From = email.utils.parseaddr(msg['From'])[1]
    sent = 1 if From in senders else 0
    print "\t%s: %s" % (datetime.fromtimestamp(date_ts), decode_header(msg['Subject'])[0][0][:40])
    c.execute('INSERT INTO messages (date, orig, sent, text) VALUES (?, ?, ?, ?)', (date_ts, origin, sent, msg.as_string(True)))
