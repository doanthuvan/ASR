# db.py
# Handle MySQL database connection and queries
# Author: Adam Mitchell
# Email:  adamstuartmitchell@gmail.com
#
#
# mysql> SHOW columns from mfcc_training_data;
# +----------------------+-------------+------+-----+---------+-------+
# | Field                | Type        | Null | Key | Default | Extra |
# +----------------------+-------------+------+-----+---------+-------+
# | idmfcc_training_data | int(11)     | NO   | PRI | NULL    |       |
# | filename             | mediumtext  | YES  |     | NULL    |       |
# | filepath             | text        | YES  |     | NULL    |       |
# | num_value            | varchar(45) | YES  |     | NULL    |       |
# | word_value           | varchar(45) | YES  |     | NULL    |       |
# | vector               | longtext    | YES  |     | NULL    |       |
# | time_added           | datetime    | YES  |     | NULL    |       |
# +----------------------+-------------+------+-----+---------+-------+

import MySQLdb as mysql


passwd = raw_input('Database password: ')
database = 'mfcc_training_data'


db = mysql.connect(host='localhost', user='root', passwd=passwd, db=database)
cu = db.cursor()
cu.execute('SHOW columns FROM mfcc_training_data;')
for col in cu.fetchall():
    print col