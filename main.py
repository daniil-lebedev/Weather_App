from api_key import owm
from pyowm.utils import config
from pyowm.utils import timestamps


#take the input from the user
takeInput = input("Please insert the name of the city here (e.g. Moscow, RU) : ")


# ---------- FREE API KEY examples ---------------------

owm 
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(takeInput)
w = observation.weather

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75

print('The weather is :',w)


