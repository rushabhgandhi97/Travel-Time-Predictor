import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","12345","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

user=raw_input("Enter the username :")
passwd=raw_input("Enter the password :")
user=str(user)
#sql="select * from users where logid='"+str(user)+"';"


try:
   # Execute the SQL command
   cursor.execute("select * from users where log_id='"+str(user)+"';")
   # Fetch all the rows in a list of lists.
   result=cursor.fetchone()
   print(result[0],result[1])
   if(result[1]==str(passwd)):
   	print ("Login Succesfull")
   else:
   	print("Wrong password")
except:
   print "Invalid Username or Password"

# disconnect from server
db.close()	
