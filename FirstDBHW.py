import psycopg2

#Create, Retrieve, Update, Delete

connection = psycopg2.connect(user="accounting",
                              password="password",
                              host="localhost",
                              database="Fall2025CSCI260")

cursor =connection.cursor()

def showLocations(data):
    print("\t id|\t x|\t y|")
    print("------------------------------------")
    for row in data:
        for value in row:
            print("\t",value,"|",end="")
        print("")
    print("------------------------------------")

def getLocations(): # R in CRUD
    cursor.execute("Select id,x,y from location")
    data=cursor.fetchall()
    #print(data)
    return data

def putLocation(values):
    cursor.execute(f"insert into location (x,y) values ({values[0]},{values[1]})")

def getLocationFromUser():  # C in CRUD 
    x=input("Please enter X:")
    y=input("Please enter Y:")
    return (x,y)

def getIdFromUser():
    id=input("Please enter ID to DELETE: ")
    return id

def deleteId(id):
    cursor.execute(f"delete from location where id = {id}")
    print(f"Record with id {id} has been deleted. Make sure to commit changes.")

def putChange(d): # d is a dictionary that include id and either x, y or both
    first="update location set "
    id=d["id"]
    last=f" where id={id}"
    value1=""
    if "x" in d:
        x=d["x"]
        value1=f"x={x}"
    value2=""
    if "y" in d:
        y=d["y"]
        value2=f"y={y}"
    if ("x" in d) and ("y" in d):
        value1=value1+","
    cursor.execute(first+value1+value2+last)

def updateLocation():
    choice=0
    print("0) Cancel")
    print("1) Change X")
    print("2) Change Y")
    print("3) Change Both")
    choice=int(input("Enter your choice to change a parameter"))
    if choice!=0:
        id=input("Enter id you want to update:")
        if choice==1 or choice==3:
            x=input("Enter new X:")
        if choice==2 or choice==3:
            y=input("Enter new Y:")
        if choice==1: 
            putChange( {"id":id,"x":x} )
        if choice==2:
            putChange( {"id":id,"y":y} )
        if choice==3:
            putChange( {"id":id,"x":x,"y":y})

choice=1
while choice!=0:
    print("0) Quit")
    print("1) Show Locations R")
    print("2) Add Location C")
    print("3) Update Location U")
    print("4) Delete")
    print("5) Commit current changes")
    choice=int(input("Enter your choice: "))
    if choice==1:
        showLocations(getLocations())
    if choice==2:
        putLocation(getLocationFromUser())
    if choice==3:
        updateLocation()
    if choice==4:
        deleteId(getIdFromUser())
    if choice==5:
        connection.commit()