pg2sql
======

Converts a Postgresql database to a individual .sql files per object


License and Copyright

Public Domain and No copyright held - Developed by the Albuquerque Seismology Laboratory, part of the United States Geological Survey

Usage

-h or --host= for server address  
-U or --username= for username  
-p or --port= for server port  
-d or --dbname= for database name  
-f or --folder= for folder path. It must end with a /  

Example: python pg2sql.py --host=127.0.0.1 --dbname=myDatabase --port=5432 --username=myUser --folder=output/

Example: python pg2sql.py -h 127.0.0.1 -d myDatabase -p 5432 -U myUser -f output/

