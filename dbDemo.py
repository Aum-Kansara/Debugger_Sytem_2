import mysql.connector
from dotenv import load_dotenv
from os import getenv

load_dotenv()

db = mysql.connector.connect(
  host ="localhost",
  user =getenv("MYSQL_USER"),
  passwd =getenv("MYSQLDB_PASSWORD"),
  database=getenv("DB_NAME")
)
 

cursor=db.cursor()


# Insertion
# name="viraj"
# passwd="123"
# cursor.execute(f"insert into test(name,pass) values ('{name}','{passwd}')")
# db.commit()



# fetch Values
# query="select * from test"
# cursor.execute()
# print(cursor.fetchall())


# Update
# query = "UPDATE TEST SET NAME = 'viraj2' WHERE Name ='viraj'"
# cursor.execute(query)
# db.commit()

# Deletion
# query = "DELETE FROM TEST WHERE NAME = 'aum'"
# cursor.execute(query)
# db.commit()


# Disconnecting from the server
db.close()