# imap_transfer

Transfers IMAP messages from one account to another.

## Description
These scripts retrieve emails from different accounts and transfer them to a single one.

Emails can be obtained from an IMAP mailbox or an `mbox` file.

All emails are stored in a SQLite database before being added to an IMAP mailbox, which allows for a sort by message date.

Sent emails are stored in the `Sent` directory, others in the `Inbox` directory.

## Files
 - `read_imap.py` : reads messages from an IMAP account and stores them in the database
 - `read_mbox.py` : reads messages from an mbox file and stores them in the database
 - `write_imap.py` : adds messages form the database to an IMAP account
 - `empty_imap.py` : empties all messages from an IMAP account
 - `imap_utils.py` : utilities & functions
 - `global.db` : SQLite database storing retrieved messages

## Configuration
 - `server` : IMAP server (`read_imap.py`, `write_imap.py`, `empty_imap.py`)
 - `user` : IMAP identifier (`read_imap.py`, `write_imap.py`, `empty_imap.py`)
 - `password` : IMAP password (`read_imap.py`, `write_imap.py`, `empty_imap.py`)
 - `folder` : IMAP mailbox containing messages (`read_imap.py`, `empty_imap.py`)
 - `path` : directory containing mbox files, theses files must begin with "`mbox_`" (`read_mbox.py`)
 - `origin` : originating email address (`read_imap.py`, `read_mbox.py`)
 - `database` : SQLite database (`read_imap.py`, `read_mbox.py`, `write_imap.py`)
 - `senders` : list of email addresses used for sending messages (`imap_utils.py`)

## Usage
If you send messages with multiple addresses, they all must be in the `senders` list in `imap_utils.py`.

Make sure the SQLite database is created and empty before adding messages into it.
If necessary, the database may be created from scratch with the `CREATE` query below.

Before using any script, make sure the configuration is correct. Each script has its own configuration (see below).
To add `mbox` messages, the directory containing mbox files must be created first (see the `path` configuration).

Typically, you first use `read_*.py` to add messages to the database, then `write_imap.py` to transfer those messages back into the final mailbox.
All messages in an IMAP mailbox can be deleted using `empty_imap.py`.

## Database
    CREATE TABLE messages (
      umid INTEGER PRIMARY KEY,
      date TIMESTAMP,
      orig VARCHAR,
      sent BOOL,
      text TEXT
    );

## Notes
With IMAP, received messages are in the `INBOX` directory, others might exist.
With Gmail, the `[Gmail]/Sent Mail` directory contains sent messages, and the `[Gmail]/All Mail` directory contains all messages.

<<<<<<< HEAD
https://github.com/majetzx/imap_transfer
=======
https://github.com/majetzx/imap_transfer
>>>>>>> e4abac2b1aa99113f144f055cb7c95f4fa015081
