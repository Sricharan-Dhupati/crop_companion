import requests
from bs4 import BeautifulSoup
import datetime

 
# enter city name
city = input("Enter your village: ")
 
# creating url and requests instance
url = "https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content

# getting raw data
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
 
# formatting data
data = str.split('\n')
time = data[0]
sky = data[1]
 
# getting all div tag
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
strd = listdiv[5].text
 
# getting other required data
pos = strd.find('Wind')
other_data = strd[pos:]
 
# printing all data
print("Temperature is", temp)
print("Time: ", time)
print("Sky Description: ", sky)
print(other_data)

def get_season(date):
    month_day = date.month * 100 + date.day

    if 601 <= month_day <= 1031:
        return "Kharif"
    elif 1101 <= month_day <= 331:
        return "Rabi"
    elif 401 <= month_day <= 630:
        return "Zaid"
    else:
        return "Unknown Season"

# Example usage
date = datetime.date.today()
print(date)
print(get_season(date))  # Output: Winter