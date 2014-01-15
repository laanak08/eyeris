import sqlite3
import datetime
import logging
import ConfigParser
import os.path
import os

class MetaDataManager(object):
    """handles storing and retrieval of metadata of processed files
        hides the schema and DB used"""
    @staticmethod
    def createDB(dbpath):
        """Create the initial database at the given path"""
        conn = sqlite3.connect(dbpath + 'metadata')
        c = conn.cursor()
        c.execute('DROP TABLE IF EXISTS stats')
        c.execute('''CREATE TABLE stats (
                endtime TIMESTAMP NOT NULL,
                copy NOT NULL,
		records,
		bytes,
                elapsed,
                nfiles)''')
        conn.commit()
        conn.close()
        #error handling missing
        return True

    def __init__(self, dbpath):
        self.conn = sqlite3.connect(dbpath + 'metadata')
        self.bmarkdir = os.path.join(dbpath,'bmarks')
	if not os.path.isdir(self.bmarkdir):
		os.mkdir(self.bmarkdir)
        

    def query(self, filename):
        """Ask about a filename, return last position or False"""
	#this needs better error handling for IO errors
	fp = os.path.join(self.bmarkdir,filename+'.bm')
	if os.path.isfile(fp):
		with open(fp) as bf:
			for l in bf:
				last = l
		return {'lastbyte': int(last)}
	else:
		return False

            

    def load(self, filename, lastbyte):
        """Updates or inserts data about the file"""
	fp = os.path.join(self.bmarkdir,filename+'.bm')
	with open(fp, 'a') as bf:
		bf.write("%s\n" % lastbyte)
        
        return True
        
    def saveStats(self, copy, records, bytes, elapsed, nfiles):
        """Records the amount of data processed """
        
        c = self.conn.cursor()
        values = (datetime.datetime.now(), copy, records, bytes, elapsed, nfiles)
        c.execute('INSERT INTO stats VALUES (?,?,?,?,?,?)', (values))
        self.conn.commit()
        return True

    def __del__(self):
        self.conn.close()

if __name__ == '__main__':
	config = ConfigParser.ConfigParser()
	config.read('../basic.cfg')
	thispath = config.get('MySection','metadataPath')
	#thispath = '/cpm/projects/smapi/bin/new'
	MetaDataManager.createDB(thispath)

	


	
