import requests
import sqlite3
import json

params = {
  'access_key': '2044e3ef665718f351d2a89204b2a224',
  'query': 'Eilat'
}
api_result = requests.get('http://api.weatherstack.com/current', params)
#print(api_result)
# getting data in the json format
if api_result.status_code == 200:
   api_response = api_result.json()

   data = json.dumps(api_response)
#print(data)

"""   # getting the main dict block
   location = api_response['location']
   current = api_response['current']

# enter city
   Region = location['region']
   temp = current['temperature']

   print(f"{Region:-^30}")
   print(f"temperature: {temp}")

else:
   #error in http request
   print("Error in the HTTP request")
"""
conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS stackweather (city varchar(3), data json)")
c.execute("insert into stackweather values (?, ?)",["1", json.dumps(api_response)])
conn.commit()
c.execute("select * from stackweather")
print(c.fetchone())
#conn.close()

"""
for city in data:
    c.execute("insert into stackweather values (?, ?)",
    [city[0], json.dumps(api_response)])
    conn.commit()


c.execute("select * from stackweather;")
conn.close()

def get_my_jsonified_data(key):
    with sqlite3.connect('test.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM stackweather WHERE column=?;", [city])
        datad = cursor.fetchall()
        print (json.dumps(datad))
"""