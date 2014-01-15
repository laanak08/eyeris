#!/usr/local/bin/python2.7

import re
import pymongo
import datetime
import logging
import os
import time
import ConfigParser
import sys

from metadatamanager import * 

mycopy = sys.argv[1]
#logging.basicConfig(filename='readtest.log',level=logging.DEBUG)
#logging.basicConfig(filename='read.log',level=logging.INFO)
#logging.basicConfig(level=logging.INFO)
config = ConfigParser.ConfigParser()
config.read('/cpm/projects/smapi/basic.cfg')

path = config.get('MySection','basePath')
metadataPath = config.get('MySection','metadataPath')
mongoDB = config.get('MySection','mongoDB_'+mycopy)
sleepCycle = 300
#readlog = config.get('MySection','readlog_'+mycopy)
readlog = "%s/logs/read_%s.log" % (path, mycopy)
stateFile = "%s/state/state_%s.txt" % (path, mycopy)

logging.basicConfig(filename=readlog,level=logging.INFO)
rawPaths = config.get('MySection','rawDataPath_'+mycopy)
targetFiles = config.get('MySection','targetFiles_'+mycopy)
colName = config.get('MySection','colName_'+mycopy)

targetFilesRE = re.compile(targetFiles)

def checkIn():
	with open(stateFile) as stf:
		sv = stf.read().strip()
		logging.info("State read value is %s",sv)
		return sv

def parseField(value, sline):
	p = value + "=(.*?);" 
	mo = re.search(p,sline)
	if mo:
		return mo.group(1)
	else:
		return ''


from pymongo import MongoClient
mclient = MongoClient('lab7983',27017)
db = mclient[mongoDB]
kers = db[colName]
batch = 15 

def readInsert(source, start):
	nrec = 0
	records = []
	with open(source) as sf:
		sf.seek(start)
		_nl = 0
		for line in sf:
			ts = re.search(r'^timestamp=([\d\/\s:\.]*);dimeName=(\w+);',line)
			if not ts:
				#thi sis not a good line
				continue
			tso = datetime.datetime.strptime(ts.group(1),'%Y/%m/%d %H:%M:%S.%f')

			rtype = ts.group(2)
                        try:
                                event = dict(p.split('=',1) for p in line.rstrip()[:-1].split(';'))
                        except ValueError as e:
                                logging.debug("ValueError dic")
                                logging.debug("%s", e)
				try:
					event = dict(p.split('=',1) for p in line.rstrip().split(';'))
				except ValueError as e2:
					logging.warning("ValueError2 dic retry on %s", line)
                                	logging.warning("%s", e2)
                                	for p in line.rstrip()[:-1].split(';'):
                                        	logging.warning("%s",p)
                                	logging.warning("last characters %s.",line.rstrip()[-5:])
                                	event = {'timestamp' : ts.group(1),
                                          	 'dimeName': rtype,
                                          	 'line':  line}
			for key in event.keys():
				if '.' in key:
					nkey = key.replace('.','_')
					event[nkey] = event[key]
					del event[key]

                        event.update({'ts': tso})
                        del event['timestamp']

                        #Placing something for now
                        if 'appName' not in event:
                                event['appName']= 'UNKNOWN' 



			if rtype == 'KeyEvent': 
				bdt = event.get('beginTime')
				edt = event.get('endTime')
				if bdt and edt:
					bdto=datetime.datetime.strptime(bdt,'%Y/%m/%d %H:%M:%S.%f')
					edto=datetime.datetime.strptime(edt,'%Y/%m/%d %H:%M:%S.%f')
					response = edto - bdto
					event.update({ 
						 'bdt': bdto, 
				 		 'edt': edto,
						 'ress': response.total_seconds()})
					del event['beginTime']
					del event['endTime']

			records.append(event)
			nrec += 1
			if nrec == batch:
				kers.insert(records)
				records = []
				nrec = 0
			_nl += 1
		if len(records) > 0:
			kers.insert(records)
		return (sf.tell(), _nl)




store = MetaDataManager(metadataPath)

while True:
	stime = time.time()
	rawPathList = [item.strip() for item in rawPaths.split(',')]

	_allLines = 0
	_allBytes = 0
	_nfiles = 0


	for rawDataPath in rawPathList:
		smapiFiles = [f for f in os.listdir(rawDataPath) if targetFilesRE.match(f)]


		for f in smapiFiles:
			logging.info("Processing %s",f)
			finfo = store.query(f)
			if finfo:
				logging.info("Seen this file, starting at %s",finfo['lastbyte'])
				try:
					if os.stat(rawDataPath + f).st_size == finfo['lastbyte']:
						logging.info("No new data, same size, skipping")
						continue
					start = finfo['lastbyte']
				except OSError as e:
					logging.warning("There was an OSError checking file size")
					logging.warning("%s",e)
					continue
	
			else:
				logging.info("New file")
				start = 0
		
			try:
                                #Dated collection based loosly on the file date
                                #This needs to be checked later - leap of faith for now
                                _fs = f.rsplit('.',5)
                                _fd = datetime.datetime(datetime.date.today().year,int(_fs[1]),int(_fs[2]))
                                fullcol = colName + '_' + _fd.strftime('%m%d%y')
                                if not kers.name == fullcol:
                                    kers = db[fullcol]
				(final,_linesRead) = readInsert(rawDataPath + f, start)
				store.load(f, final)
				_allLines += _linesRead
				_allBytes += (final - start)
				_nfiles += 1
			except IOError as e:
				logging.warning("IOError in readInsert function")
				logging.warning("%s",e)
	
	
	
	etime = time.time()
	elapsed = etime - stime
	store.saveStats(mycopy, _allLines, _allBytes, elapsed, _nfiles)
	logging.info("Total time was: %g seconds records: %s  Kbytes: %s Files: %s",elapsed,_allLines, _allBytes/1024, _nfiles)
	
	logging.info("Total time was: %g minutes",elapsed/60)
	logging.info("Started at: %s",time.asctime(time.localtime(stime)))
	logging.info("Ended at: %s",time.asctime(time.localtime(etime)))
	state = checkIn()
	if not state == '1':
		break

	delta = stime + sleepCycle - time.time()
	if delta > 0:
		logging.info("Going to sleep for %s seconds", delta)
		time.sleep(delta)
	else:
		logging.info("Going to iterate right away, behind %s seconds",delta)
	


