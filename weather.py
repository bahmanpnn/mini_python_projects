import requests
import time
import sqlite3
def sql_connector():
    con=sqlite3.connect('mydatabase.db')
    curs=con.cursor()
    return con,curs
def create_table(con,curs):
    curs.execute("create table if not exists weather(city_name TEXT,date_time TEXT,temp FLOAT,humidity int )")
    con.commit()
def insert_data(con,curs,data):
    curs.execute("insert into weather Values(?,?,?,?)",tuple([v for k,v in data.items()]))
    con.commit()
def process_data_for_human(data):
    output_dic={'city':data['name'],'datetime':time.ctime(int(data['dt'])),'temp':data['main']['temp'],'humidity':data['main']['humidity']}
    return output_dic
def get_weather_data(city='tehran',appid=''):
  
    URL =f"https://api.openweathermap.org/data/2.5/weather"
    PARAMS = {'q':city,'appid':appid}

    r = requests.get(url = URL,params=PARAMS)
    data = r.json()
    return process_data_for_human(data)

con,curs=sql_connector()
create_table(con,curs)
while True:
    data_weather=get_weather_data('gorgan')
    insert_data(con,curs,data_weather)
    print(data_weather)
    time.sleep(3)


#way2

# app_id=''
# city='gorgan'
# # api-endpoint
# # URL =f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={app_id}'
# # URL ='https://api.openweathermap.org/data/2.5/weather?q={city}&appid={app_id}'
# URL ='https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city,app_id)
  
# # location given here
# # location = "delhi technological university"
  
# # defining a params dict for the parameters to be sent to the API
# # PARAMS = {'address':location}
  
# # sending get request and saving the response as response object
# # r = requests.get(url = URL, params = PARAMS)
# r = requests.get(url = URL)
  
# # extracting data in json format
# data = r.json()
# print(data)
