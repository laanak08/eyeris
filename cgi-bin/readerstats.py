#!/usr/local/bin/python2.7

import cgitb
cgitb.enable()

import cgi
import yate
import logging
import ConfigParser
import re
import sqlite3
from utilities import *

config = ConfigParser.ConfigParser()
config.read('../basic.cfg')
logfile = config.get('MySection','weblog')
#colName = config.get('MySection','colName')
metadatapath = config.get('MySection','metadatapath')




#logging.basicConfig(filename=logfile,level=logging.INFO,
#                    format='%(asctime)s %(message)s')


#bad should use the object
conn = sqlite3.connect(metadatapath + 'metadata', detect_types=sqlite3.PARSE_DECLTYPES)
c = conn.cursor()
#hardcoding for the time the bookmark system went in
sdt = datetime.datetime(2013,11,6,14,10)
res = c.execute('select * from stats where endtime > ?', (sdt,)).fetchall()


print "Content-Type: text/csv"
print "Content-Disposition: attachment;filename=readerstats.csv\n"
print "endtime,copy,records,bytes,elapsed,nfiles,starttime"
for r in res:
	for c in r:
		print "%s," % c,
	print " " 

conn.close()

