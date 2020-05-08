import mysql.connector
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