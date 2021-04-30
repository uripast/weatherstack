import requests
import sqlite3
import json
import config

api_result = requests.get('http://api.weatherstack.com/current', config.params)
#test successful response
if api_result.status_code == 200:
   api_response = api_result.json()

#data is a json file
   data = json.dumps(api_response)
   response_dict = json.loads(data)

#connect to sqlite
conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS stack_weather (city varchar(30), country varchar(30),region varchar(30), temp integer)")
c.execute("insert into stack_weather values (?,?,?,?)",
          [response_dict["location"]['name'],
           response_dict["location"]['country'],
           response_dict["location"]['region'],
           response_dict["current"]['temperature']])
conn.commit()
c.execute("select * from stack_weather")
print(c.fetchone())
conn.close()

