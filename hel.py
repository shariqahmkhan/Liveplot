from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from datetime import datetime
import requests
import json
from collections import deque

x = []
y = []

plt.style.use('fivethirtyeight')
def get_data(i):
    weather = requests.get("http://api.weatherapi.com/v1/current.json?key=1be81c1236b342bd8c041735201904&q=delhi")
    weather_data = json.loads(weather.content)
    city_name = weather_data["location"]["name"]
    temp_c = weather_data["current"]["temp_c"]
    #print(type(temp_c))
    #y_val = temp_c
    y.append(temp_c)
    #print(x_val is None)
    x.append(datetime.now().second)
    #print(type(x_val))
    
    plt.plot(x,y)
    #temperature = (temp_c, datetime.now())
    
ani = FuncAnimation(plt.gcf(), get_data, interval = 1000)
print(ani)
plt.tight_layout()
plt.show()

# do something
