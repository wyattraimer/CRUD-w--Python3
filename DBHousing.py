from dotenv import load_dotenv
import matplotlib.pyplot as plt
import psycopg2
import os

load_dotenv()

connection=psycopg2.connect(user="accounting", password=os.getenv("PASSWORD"), host="localhost", database="Fall2025CSCI260")

cursor=connection.cursor()

def getLocations():
    cursor.execute("select latitude, longitude from housing where ocean_proximity='NEAR BAY'")
    data=cursor.fetchall()
    return data

print(os.getenv("PASSWORD"))
latsLongs=getLocations()
# print(latsLongs)

lats=[]
longs=[]

for ll in latsLongs:
    lats.append(ll[0])
    longs.append(ll[1])

plt.scatter(lats, longs)

plt.xlabel('Latitude')
plt.ylabel('Longituide')
plt.title('Location Plot')

plt.show()
