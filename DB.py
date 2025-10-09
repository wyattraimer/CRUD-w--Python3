import psycopg2

# CREATE RETRIEVE UPDATE DELETE (CRUD)

connection = psycopg2.connect(user="accounting",
                                password="password",
                                host="localhost",
                                database="Fall2025CSCI260")

cursor = connection.cursor()

# R in CRUD
def getLocations():
    cursor.execute("select id,x,y from location")
    data=cursor.fetchall()
    # print(data)
    return data

def putLocation(values):
    cursor.execute(f"insert into location (x,y) values ({values[0]},{values[1]})")

# d is a dictionary that includes id and either x,y or both
def putChange(d):
    first="update location set "
    id=d["id"]
    last=f" where id={id}"
    value1=""
    if "x" in d:
        x=d["x"]
        value1=f"x={x}"
    value2=""
    if "y" in d:
        value1=f"y={y}"
    if "x" in d and "y" in d:
        value1=value1+","
    cursor.execute(first+value1+value2+last)

def commitChanges():
    connection.commit()