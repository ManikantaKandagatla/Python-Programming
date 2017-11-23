__author__ = 'ManiKanta Kandagatla'

import sqlite3
mails = {}
conn = sqlite3.connect('D:\Languages\python\SQLite\emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1].split('@')[1]
    if email not in mails.keys():
        mails[email] = 1
    else:
        mails[email] = mails[email] + 1
for mail in mails.keys():
    cur.execute('''INSERT INTO Counts (org, count)
                VALUES ( ?, ? )''', ( mail,mails[mail] ) )
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count desc'

print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]
cur.close()
