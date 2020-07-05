import pymysql

# If you want to use an interactive approach, you can use them
# DB_Server = input("Please enter server name or IP of the DB Server: ")
# DB_Name = input("Please enter the name of the DB Server: ")
# DB_User = input("Please enter a user name you want connection to hte DB: ")
# DB_Password = input("Please enter the password of the user: ")

DB_Server = "testdbsvr.sh.local"
DB_Name = "db"
DB_User = "admin"
DB_Password = "xxxxxxxxxx"

print("Connecting to database...")

db = pymysql.connect(host=DB_Server, db=DB_Name, user=DB_User, passwd=DB_Password)

print("Succesfully Connected to database")

db.close
