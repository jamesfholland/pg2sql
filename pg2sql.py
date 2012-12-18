#Author: James Holland jholland@usgs.gov
#License: Public Domain

import sys
import getopt
import getpass
import Database

queries = {
    "getFunctions" : """
SELECT routine_name
FROM information_schema.routines
WHERE specific_schema NOT IN
('pg_catalog', 'information_schema')
AND type_udt_name != 'trigger'
""",
    "getFunctionDef" : """
SELECT pg_catalog.pg_get_functiondef(%s::regproc)
"""
}

def printHelp():
    print 'Use below options:'
    print '-h or --host= for server address'
    print '-U or --username= for username'
    print '-p or --port= for server port'
    print '-d or --dbname= for database name'
    print '-f or --folder= for folder path. It must end with a /'

def getFunctions(database, folder):
    #db_args = (stationIDs, metricID, startDate, endDate)
    result = database.select(queries['getFunctions'])
    for fun in result:
        writeFile(fun[0]+'.sql', str(database.select(queries['getFunctionDef'], [fun[0]])[0][0]), folder)


def getSchema(host, user, port, db, pwd, folder):
    database = Database.Database(host+','+user+','+pwd+','+db+','+port)
    getFunctions(database, folder)
    

def writeFile(fname, fcontent, folder):
    fo = open(folder+fname, 'w')
    fo.write(fcontent)
    fo.close()

def main():
    host='localhost'
    user='default'
    port='5432'
    db='default'
    folder='./'
    
    lparams = 'h:U:p:d:f:'
    wparams = ['host=', 'username=', 'port=', 'dbname=', 'help', 'folder']
    try:
        options, extras = getopt.getopt(sys.argv[1:],lparams,wparams)
    except getopt.GetoptError as err:
        print str(err)
        printHelp()
        sys.exit(2)
    for param, val in options:
        if param in ['-h', '--host']:
            host = val
        elif param in ['-U', '--username']:
            user = val
        elif param in ['-p', '--port']:
            port = val
        elif param in ['-d', '--dbname']:
            db = val
        elif param in ['-f', '--folder']:
            folder = val
        elif param in ['--help']:
            help()
        else:
            print 'Unknown command'
            printHelp()
    pwd=getpass.getpass('Database Password: ')
    print host,user,port,db
    getSchema(host, user, port, db, pwd, folder)

if __name__ == "__main__":
    main()

