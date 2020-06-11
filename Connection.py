import pymysql

# DB_Server = input("Please enter server name or IP of the DB Server: ")
# DB_Name = input("Please enter the name of the DB Server: ")
# DB_User = input("Please enter a user name you want connection to hte DB: ")
# DB_Password = input("Please enter the password of the user: ")

DB_Server = "15.83.246.104"
DB_Name = "db"
DB_User = "admin"
DB_Password = "Shanghai2010"

print("Connecting to database...")

db = pymysql.connect(host=DB_Server, db=DB_Name, user=DB_User, passwd=DB_Password)

print("Succesfully Connected to database")

db.close
