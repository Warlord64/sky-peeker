from flask import Flask,render_template,request,abort
import json
import urllib.request

app = Flask(__name__)
#converting kelvin to celcius
def tocelcius(temperature_in_kelvin):
    return str(round(temperature_in_kelvin - 273.15, 3))

@app.route('/',methods=['POST', 'GET'])
def weather():
    #api key
    api_key = open('api_key', 'r').read()

    #city
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'kanpur'

    #getting json data from the api
    url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key).read()

    # converting json data to dictionary
    data = json.loads(url)
    weather_info = {
        "temp": str(data['main']['temp']) + 'k',

        "temp_cel": tocelcius(data['main']['temp']) + 'C',

        "pressure": str(data['main']['pressure']),

        "humidity": str(data['main']['humidity']),

        "cityname":str(city),

        "country_code": str(data['sys']['country']),

        "coordinate": str(data['coord']['lon']) + ' ' + str(data['coord']['lat']),
    }
    return render_template('index.html',weather_info=weather_info)
