# Weather app☁️

This is a simple weather application which runs in your terminal!

## Installation⚙️

Just clone the repo to your local machine🖥️

```bash
git clone https://github.com/daniil-lebedev/Weather_App.git
```

## Running it🏃

I am using an api provided by the cool guys at [PYOWM](https://github.com/csparpa/pyowm.git)! Thanks a lot for building this. You are amazing!

You should also get your free API key at [OpenWeather](https://openweathermap.org).

The code below is what you use to build your amazing application!


```python
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('your free OWM API key')
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('London,GB')
w = observation.weather

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75

# Will it be clear tomorrow at this time in Milan (Italy) ?
forecast = mgr.forecast_at_place('Milan,IT', 'daily')
answer = forecast.will_be_clear_at(timestamps.tomorrow())

```

## Contributing🖌️
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Major thanks
Yet again thank you to [Readme 101](https://www.makeareadme.com) for helping with README.md file.
