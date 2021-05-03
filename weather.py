import requests
import sqlite3
import json
import config
import unittest

def weather_run():
    return __name__
api_result = requests.get('http://api.weatherstack.com/current', config.params)
#write into json file
def my_json_file():
    api_response = api_result.json()
    data = json.dumps(api_response)
    return(data)
    response_dict = json.loads(my_json_file())
print(my_json_file())

response_dict = json.loads(my_json_file())
#enter data to db
def dynamic_data_entry():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS stack_weather (city varchar(30), country varchar(30),region varchar(30), temp integer)")
    c.execute("insert into stack_weather values (?,?,?,?)",
          [response_dict["location"]['name'],
           response_dict["location"]['country'],
           response_dict["location"]['region'],
           response_dict["current"]['temperature']])
    conn.commit()
    conn.close()
#query from db
def get_data_sql():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("select * from stack_weather")
    return (c.fetchall())
    conn.close()
print(get_data_sql())

class TestSum(unittest.TestCase):
    def test_api():
    #test succuessful api response
        if api_result.status_code == 200:
            api_response = api_result.json()
    # test when city not exists
        elif api_result.status_code == 404:
            print("city not found")
        return
    #check db entered value
    def test_data_entry():
        unittest.get_data_sql()>1 #pass
        return
    #check correction of the db
    def data_correct():
        unittest.get_data_sql()==1
        return

#main function to execute all
if __name__ == "__main__":
    weather_run()
    dynamic_data_entry()
    get_data_sql()
    unittest.main()