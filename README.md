imap_transfert
==============

Transfer IMAP messages from one account to another.

### Description
These scripts retrieve emails from different accounts and transfer them into a single one.
You can get emails from an IMAP mailbox or an mbox file.
All emails are stored in a SQLite database before being added to an IMAP mailbox.
Thanks to the database, messages are sorted by date before the addition to the final mailbox.
Sent emails are stored in the "Sent" directory, other in the "Inbox" directory.

### Files
 - read_imap.py : reads messages from an IMAP account and stores them in the database
 - read_mbox.py : reads messages from an mbox file and stores them in the database
 - write_imap.py : adds messages form the database to an IMAP account
 - empty_imap.py : empties all messages from an IMAP account
 - imap_utils.py : utilities & functions
 - global : SQLite database storing retrieved messages

### Configuration (selon les scripts) :
 - server : IMAP server (read_imap.py, write_imap.py, empty_imap.py)
 - user : IMAP identifier (read_imap.py, write_imap.py, empty_imap.py)
 - password : IMAP password (read_imap.py, write_imap.py, empty_imap.py)
 - folder : IMAP mailbox containing messages (read_imap.py, empty_imap.py)
 - path : répertoire contenant les fichiers mbox commençant par "mbox_" (read_mbox.py)
 - origin : originating email address (read_imap.py, read_mbox.py)
 - database : SQLite database (read_imap.py, read_mbox.py, write_imap.py)
 - senders : list of email addresses used for sending messages (imap_utils.py)

### Database

CREATE TABLE messages (
  umid INTEGER PRIMARY KEY,
  date TIMESTAMP,
  orig VARCHAR,
  sent BOOL,
  text TEXT
);

### Notes
With IMAP, received messages are in the "INBOX" directory, others might exist.
With Gmail, the "[Gmail]/Sent Mail" directory contains sent messages, and the "[Gmail]/All Mail" directory contains all messages.
