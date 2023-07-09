import requests

joke_api = "https://api.yomomma.info/"
fact_api = "https://uselessfacts.jsph.pl/api/v2/facts/random"
techy_api = "https://techy-api.vercel.app/api/json"
weather_api = "https://goweather.herokuapp.com/weather/Coimbatore"
weather = "https://wttr.in/coimbatore?format=j1"

def get_joke():
    data = requests.get(joke_api).json()['joke']
    print(data)

def get_fact():
    data = requests.get(fact_api).json()['text']
    print(data)

def get_techy():
    data = requests.get(weather_api).json()
    print(data)

def get_weather():
    data = requests.get(techy_api).json()['message']
    print(data)

if __name__ =="__main__":
    # get_fact()
    # get_joke()
    # get_techy()
    # get_weather()
    data =  requests.get(weather).json()
    print(data['current_condition'])