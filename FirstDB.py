import psycopg2

# CREATE RETRIEVE UPDATE DELETE (CRUD)

connection = psycopg2.connect(user="accounting",
                                password="password",
                                host="localhost",
                                database="Fall2025CSCI260")



cursor = connection.cursor()

def showLocations(data):
    print("\t x|\t y|\t id|")
    print("---------------")
    for row in data:
        for value in row:
            print("\t", value,"|",end="")
        print("")
    print("---------------")

# R in CRUD
def getLocations():
    cursor.execute("select id,x,y from location")
    data=cursor.fetchall()
    # print(data)
    return data

def putLocation(values):
    cursor.execute(f"insert into location (x,y) values ({values[0]},{values[1]})")

# C in CRUD
def getLocation():
    x=input("Please enter X: ")
    y=input("Please enter Y: ")
    return (x,y)

# d is a dictionary that includes id and either x,y or both
def putChange(d):
    first="update location set "
    id=d["id"]
    last=f"where id={id}"
    value1=""
    if "x" in d:
        value1=f"x={x}"
    value2=""
    if "y" in d:
        value1=f"y={y}"
    if "x" in d and "y" in d:
        value1=value1+","
    cursor.execute(first+value1+value2+last)

def updateLocation():
    choice=0
    print("0) Cancel ")
    print("1) Change X ")
    print("2) Change Y ")
    print("3) Change both ")
    choice=int(input("Enter your choice to change a parameter: "))
    if choice!=0:
        id=input("Enter id you want to update: ")
        if choice==1 or choice==3:
            x=input("Enter new X: ")
        if choice==2 or choice==3:
            y=input("Enter new Y: ")
        if choice==1:
            putChange( {"id":id,"x":x} )
        if choice==2:
            putChange( {"id":id,"y":y} )
        if choice==3:
            putChange( {"id":id,"x":x,"y":y} )

choice=1
while choice!=0:
    print("0) Quit ")
    print("1) Show Locations ")
    print("2) Add Location ")
    print("3) Update Location ")
    # print("4) Delete (to be completed)")
    print("5) Save and commit results ")
    choice=int(input("Enter your choice: "))
    if choice==1:
        showLocations(getLocations())
    if choice==2:
        putLocation(getLocation())
    if choice==3:
        updateLocation()
    # if choice==4:

    if choice==5:
        connection.commit()