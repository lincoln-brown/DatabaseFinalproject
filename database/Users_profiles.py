import mysql.connector
from datetime import datetime
startTime = datetime.now()
macs=500000

userid=[]
ProfileId=[]
db_connection = mysql.connector.connect(
host="localhost",
user="DEVELOPER",
passwd="@Links1010",
database="MyBook"
)
for i in range(100000,600000):
	userid.append('UID'+str(i))
	ProfileId.append('PID'+str(i))

db_cursor = db_connection.cursor()
for i in range(500000):
	db_cursor.execute("INSERT INTO User_profile VALUES(%s,%s)", (userid[i],ProfileId[i]))

db_connection.commit()


pfid=ProfileId[0:20]
db_cursor = db_connection.cursor()
for i in range(len(pfid)):
	for j in range(len(pfid)):
		if i != j:
			db_cursor.execute("INSERT INTO Profile_friends VALUES(%s,%s,%s)", (pfid[i],pfid[j],'school'))


db_connection.commit()
print(datetime.now() - startTime)