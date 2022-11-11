from bs4 import BeautifulSoup
from requests import get
from datetime import datetime, timedelta

def find_day_temp(whitch_day, day_number): # get weather status for specific day
    for day in bs.find_all('a', href="/en/pl/opole/274945/daily-weather-forecast/274945?day=" + str(day_number)):
        day_temp = {whitch_day: day.find('div', {'class': 'high'}).get_text().strip()}
    return day_temp

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62"
}

URL = "https://www.accuweather.com/en/pl/opole/274945/" + datetime.now().strftime("%B") + "-weather/274945" # link to web for info about weather
page = get(URL, headers=headers) # connect to page

if page.status_code == 200:
    bs = BeautifulSoup(page.content, "html.parser")
    days_temp = {}
    
    today = datetime.today().strftime("%d/%m/%Y")
    tommorow = datetime.now() + timedelta(days=1)
    days_temp.update(find_day_temp(today, 1))
    days_temp.update(find_day_temp(tommorow.strftime("%d/%m/%Y"), 2))

print(days_temp)