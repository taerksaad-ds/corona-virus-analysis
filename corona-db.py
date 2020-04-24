import sqlite3 
import csv 

conn = sqlite3.connect('wpou.db')
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS popworld (
    id integer primary key autoincrement,
    country text,
    sums integer,
);
""")


fname = input('wp.csv')

with open(fname) as csv_file:
   csv_reader = csv.reader (csv_file, delimiter=',')
   for row in csv_reader :
      print (row)
      country= row[0]
      sums= row[1]
      cur.execute (''' INSERT INTO popworld (id , country , sums) VALUES (?, ?, ?) ''' )
      conn.commit ()