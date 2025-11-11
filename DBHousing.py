from dotenv import load_dotenv
import matplotlib.pyplot as plt
import psycopg2
import os

load_dotenv()

connection = psycopg2.connect(user="accounting",
                              password=os.getenv("PASSWORD"),
                              host="localhost",
                              database="Fall2025CSCI260")
cursor =connection.cursor() 

def getLocations():
    cursor.execute("Select latitude,longitude,sqrt(power(longitude - -120.14,2)+power(latitude-34.6,2)) as d \
                    from housing order by d asc limit 1000")
    data=cursor.fetchall()
    return data

def getAgeVsValue():
    cursor.execute("Select housing_median_age,median_house_value,abs(median_house_value - 241400.0)+abs(housing_median_age-52.0) as d \
                    from housing order by d asc limit 100")
    data=cursor.fetchall()
    return data

#print(os.getenv("PASSWORD")) 
latsLongs=getLocations()
#print(latsLongs)

lats=[]
longs=[]
for item in latsLongs:
    lats.append(item[0])
    longs.append(item[1])

#plt.scatter(lats,longs)

#plt.xlabel('Latitude')
#plt.ylabel('Longitude')
#plt.title('Location Plot')

#plt.show()

agesValues=getAgeVsValue()

ages=[]
values=[]
for item in agesValues:
    ages.append(item[0])
    values.append(item[1])

ageGood=[52.0]
valueGood=[241400.0]

plt.scatter(ages,values)
plt.scatter(ageGood,valueGood,marker='s')

plt.xlabel('Age')
plt.ylabel('Value')
plt.title('Age Vs Value Plot')

plt.show()
