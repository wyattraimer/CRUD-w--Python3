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

def getScatterData(field1,field2):
    query=f"select {field1},{field2} from housing"
    print(query)
    cursor.execute(query)
    data=cursor.fetchall()
    return data;

def getCorrData(field1,field2):
    query=f"SELECT corr({field1},{field2}) as c \
        , regr_intercept({field1},{field2}) b, \
        regr_slope({field1},{field2}) m FROM housing"
    cursor.execute(query)
    data=cursor.fetchone()
    return data

def showCorr(c,m,b,axs):
    axs.axis('off')
    fc=round(c,2)
    fb=round(b,2)
    fm=round(m,2)
    axs.text(0,0.75,f"C:{fc}")
    axs.text(0,0.5,f"B:{fb}")
    axs.text(0,0.25,f"M:{fm}")

def scatterData(field1,field2,axs): #make a scatter plot of field1 vs field2
    xys=getScatterData(field1,field2)

    xs=[]
    ys=[]
    for item in xys:
        xs.append(item[0])
        ys.append(item[1])
    axs.scatter(xs,ys,s=2)
#    axs.xlabel(field1)
#    axs.ylabel(field2)
#    axs.show()

def getLocations(targetLat,targetLong,k):
    query=f"Select latitude,longitude,sqrt(power(longitude - {targetLong},2)+power(latitude-{targetLat},2)) as d \
                    from housing order by d asc limit {k}"
    print(query)
    cursor.execute(query)
    data=cursor.fetchall()
    return data

def getAgeVsValue(targetValue,targetAge,k):
    cursor.execute(f"Select housing_median_age,median_house_value,abs(median_house_value - {targetValue})+abs(housing_median_age-{targetAge}) as d \
                    from housing order by d asc limit {k}")
    data=cursor.fetchall()
    return data
'''
#print(os.getenv("PASSWORD")) 
latsLongs=getLocations(56,-120,100)
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


tAge=input("Please enter the target Age of the home: ")
tValue=input("Please enter the target Value of the home: ")
targetAge=[float(tAge)]
targetValue=[float(tValue)]

agesValues=getAgeVsValue(targetValue[0],targetAge[0],100)

ages=[]
values=[]
for item in agesValues:
    ages.append(item[0])
    values.append(item[1])

plt.scatter(ages,values)
plt.scatter(targetAge,targetValue,marker='s')

plt.xlabel('Age')
plt.ylabel('Value')
plt.title('Age Vs Value Plot')

plt.show()
'''

fields=['longitude', # Actual DB Fields
'latitude',
'housing_median_age',
'total_rooms',
'total_bedrooms',
'population',
'households',
'median_income',
'median_house_value']

fieldLabels=['Longitude', # Human readable labels for fields
'Latitude',
'Median Age',
'Total Rooms',
'Total Bedrooms',
'Population',
'Households',
'Median Income',
'Median Value']

fig, axs = plt.subplots(len(fields),len(fields))
for f1 in range(len(fields)):
    for f2 in range(len(fields)):
        if (f1<f2):
            scatterData(fields[f2],fields[f1],axs[f1,f2])
            if (f1+2<=f2):
                axs[f1,f2].axis('off')
            else:
                axs[f1,f2].spines['top'].set_visible(False)
                axs[f1,f2].spines['right'].set_visible(False)
        elif (f1==f2):
            axs[f1,f2].axis('off')
            axs[f1,f2].text(0.0,0.5,fieldLabels[f1], verticalalignment='center')            
        else:
            data=getCorrData(fields[f1],fields[f2])
            showCorr(data[0],data[1],data[2],axs[f1,f2])
plt.show()
