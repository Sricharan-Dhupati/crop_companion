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

data = [
    ["Crop", "Season", "Market Price (INR per kg)", "Area Grown"],
    ["Rice", "Kharif", "18-20", "West Bengal, Punjab, Uttar Pradesh"],
    ["Wheat", "Rabi", "16-18", "Punjab, Haryana, Uttar Pradesh"],
    ["Maize", "Kharif", "14-16", "Karnataka, Andhra Pradesh, Maharashtra"],
    ["Sugarcane", "Kharif", "2.8-3", "Uttar Pradesh, Maharashtra, Karnataka"],
    ["Cotton", "Kharif", "50-55", "Gujarat, Maharashtra, Telangana"],
    ["Mustard", "Rabi", "40-45", "Rajasthan, Haryana, Madhya Pradesh"],
    ["Groundnut", "Kharif", "40-45", "Gujarat, Andhra Pradesh, Tamil Nadu"],
    ["Soybean", "Kharif", "35-40", "Madhya Pradesh, Maharashtra, Rajasthan"],
    ["Tea", "Kharif", "150-200", "Assam, West Bengal, Tamil Nadu"],
    ["Coffee", "Kharif", "120-150", "Karnataka, Kerala, Tamil Nadu"],
    ["Tomato", "Kharif", "20-25", "Maharashtra, Karnataka, Andhra Pradesh"],
    ["Onion", "Kharif", "15-20", "Maharashtra, Karnataka, Gujarat"],
    ["Potato", "Rabi", "10-15", "Uttar Pradesh, West Bengal, Bihar"],
    ["Chilli", "Kharif", "80-100", "Andhra Pradesh, Karnataka, Maharashtra"],
    ["Turmeric", "Kharif", "60-70", "Telangana, Maharashtra, Tamil Nadu"],
    ["Banana", "Perennial", "30-40", "Tamil Nadu, Maharashtra, Gujarat"],
    ["Mango", "Perennial", "50-70", "Uttar Pradesh, Andhra Pradesh, Maharashtra"],
    ["Papaya", "Perennial", "20-30", "Karnataka, Maharashtra, Gujarat"],
    ["Pomegranate", "Perennial", "80-100", "Maharashtra, Karnataka, Gujarat"],
    ["Grapes", "Perennial", "60-80", "Maharashtra, Karnataka, Tamil Nadu"],
    ["Apple", "Perennial", "100-150", "Himachal Pradesh, Jammu & Kashmir, Uttarakhand"],
    ["Pineapple", "Perennial", "30-40", "West Bengal, Assam, Kerala"]
]