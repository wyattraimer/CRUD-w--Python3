from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

connection=psycopg2.connect(user="accounting", password=os.getenv("PASSWORD"), host="localhost", database="Fall2025CSCI260")

cursor=connection.cursor()

def getLocations():
    cursor.execute("select latitude, longitude from housing")
    data=cursor.fetchall()