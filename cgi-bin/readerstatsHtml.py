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
sdt = datetime.datetime.now() - datetime.timedelta(minutes=60)
res = c.execute('select *, records/elapsed as rate from stats where endtime > ?', (sdt,)).fetchall()

print yate.start_response()
print yate.include_header("Project IRIS - Reader Stats")

head = ['endtime','copy','records','bytes','elapsed','nfiles', 'rate']

print yate.html_table((res, head))

conn.close()

