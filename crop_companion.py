from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import datetime
# from translate import Translator

# headers = {"UserAgent": UserAgent().random}

# mobile_tracker_key = [
#     "Mobile Phone",
#     "Telecoms Circle / State",
#     "Network",
#     "Service Type / Signal",
#     "Address / Current GPS Location",
#     "Circle Capital",
# ]


# class Track_Mobile_Number:
#     def __init__(self, indian_mobile_number):
#         self.url = "https://www.findandtrace.com/trace-mobile-number-location"
#         self.mobile_number = indian_mobile_number
#         if self.verify_number:
#             self.data = {
#                 "mobilenumber": self.mobile_number,
#                 "submit": self.mobile_number,
#             }
#         else:
#             raise Exception("Invalid Mobile Number")

#     @property
#     def verify_number(self):

#         return bool(len(self.mobile_number) == 10 and self.mobile_number.isdigit())

#     @property
#     def track(self) -> dict:
#         html = requests.post(self.url, data=self.data, headers=headers)
#         soup = BeautifulSoup(html.text, "html.parser")
#         if soup.find("title").text.strip() != "404 NOT FOUND":
#             mobile_tracker_valve = [i.text.strip() for i in soup.find_all("td")]
#             mobile_tracker = dict(zip(mobile_tracker_key, mobile_tracker_valve))
#             # if i == "Service Type / Signal":
#             #     state = mobile_tracker_valve
#             return mobile_tracker
#         raise Exception("Mobile Number Not Found")


# if __name__ == "__main__":
#     try:
#         number = sys.argv[1]
#     except (IndexError, KeyError):
#         number = str(input("Enter the Mobile number to track: "))
#     X = Track_Mobile_Number(number).track
#     for i in X:
#         print(f"{i} --> {X[i]}")
        
 
# enter state name


def get_weather(state):
    # creating url and requests instance
    url = "https://www.google.com/search?q="+"weather"+state
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

def get_crop_suggestions(state, season):
    crops = [
        {"Crop": "Apple", "Season": "Perennial", "Market Price (INR per kg)": 150, "Area Grown": ["Himachal Pradesh", "Jammu & Kashmir", "Uttarakhand"]},
        {"Crop": "Pomegranate", "Season": "Perennial", "Market Price (INR per kg)": 100, "Area Grown": ["Maharashtra", "Karnataka", "Gujarat"]},
        {"Crop": "Chilli", "Season": "Kharif", "Market Price (INR per kg)": 100, "Area Grown": ["Andhra Pradesh", "Karnataka", "Maharashtra"]},
        {"Crop": "Grapes", "Season": "Perennial", "Market Price (INR per kg)": 80, "Area Grown": ["Maharashtra", "Karnataka", "Tamil Nadu"]},
        {"Crop": "Turmeric", "Season": "Kharif", "Market Price (INR per kg)": 70, "Area Grown": ["Telangana", "Maharashtra", "Tamil Nadu"]},
        {"Crop": "Mango", "Season": "Perennial", "Market Price (INR per kg)": 70, "Area Grown": ["Uttar Pradesh", "Andhra Pradesh", "Maharashtra"]},
        {"Crop": "Cotton", "Season": "Kharif", "Market Price (INR per kg)": 55, "Area Grown": ["Gujarat", "Maharashtra", "Telangana"]},
        {"Crop": "Mustard", "Season": "Rabi", "Market Price (INR per kg)": 45, "Area Grown": ["Rajasthan", "Haryana", "Madhya Pradesh"]},
        {"Crop": "Groundnut", "Season": "Kharif", "Market Price (INR per kg)": 45, "Area Grown": ["Gujarat", "Andhra Pradesh", "Tamil Nadu"]},
        {"Crop": "Banana", "Season": "Perennial", "Market Price (INR per kg)": 40, "Area Grown": ["Tamil Nadu", "Maharashtra", "Gujarat"]},
        {"Crop": "Pineapple", "Season": "Perennial", "Market Price (INR per kg)": 40, "Area Grown": ["West Bengal", "Assam", "Kerala"]},
        {"Crop": "Sunflower", "Season": "Rabi", "Market Price (INR per kg)": 35, "Area Grown": ["Karnataka", "Andhra Pradesh", "Maharashtra"]},
        {"Crop": "Papaya", "Season": "Perennial", "Market Price (INR per kg)": 30, "Area Grown": ["Karnataka", "Maharashtra", "Gujarat"]},
        {"Crop": "Tomato", "Season": "Kharif", "Market Price (INR per kg)": 25, "Area Grown": ["Maharashtra", "Karnataka", "Andhra Pradesh"]},
        {"Crop": "Peas", "Season": "Rabi", "Market Price (INR per kg)": 25, "Area Grown": ["Uttar Pradesh", "Madhya Pradesh", "Bihar"]},
        {"Crop": "Rice", "Season": "Kharif", "Market Price (INR per kg)": 20, "Area Grown": ["West Bengal", "Punjab", "Uttar Pradesh"]},
        {"Crop": "Wheat", "Season": "Rabi", "Market Price (INR per kg)": 18, "Area Grown": ["Punjab", "Haryana", "Uttar Pradesh"]},
        {"Crop": "Jowar", "Season": "Kharif", "Market Price (INR per kg)": 18, "Area Grown": ["Maharashtra", "Karnataka", "Madhya Pradesh"]},
        {"Crop": "Onion", "Season": "Kharif", "Market Price (INR per kg)": 20, "Area Grown": ["Maharashtra", "Karnataka", "Gujarat"]},
        {"Crop": "Barley", "Season": "Rabi", "Market Price (INR per kg)": 20, "Area Grown": ["Rajasthan", "Uttar Pradesh", "Haryana"]},
        {"Crop": "Maize", "Season": "Kharif", "Market Price (INR per kg)": 16, "Area Grown": ["Karnataka", "Andhra Pradesh", "Maharashtra"]},
        {"Crop": "Bajra", "Season": "Kharif", "Market Price (INR per kg)": 15, "Area Grown": ["Rajasthan", "Maharashtra", "Gujarat"]},
        {"Crop": "Potato", "Season": "Rabi", "Market Price (INR per kg)": 15, "Area Grown": ["Uttar Pradesh", "West Bengal", "Bihar"]},
        {"Crop": "Sugarcane", "Season": "Kharif", "Market Price (INR per kg)": 3, "Area Grown": ["Uttar Pradesh", "Maharashtra", "Karnataka"]}
    ]

    # Filter crops based on the state and season
    filtered_crops = [crop for crop in crops if state in crop["Area Grown"] and (crop["Season"] == season or crop["Season"] == "Perennial")]

    # Sort crops by market price in descending order
    sorted_crops = sorted(filtered_crops, key=lambda x: x["Market Price (INR per kg)"], reverse=True)

    return sorted_crops

def main():
    state = input("Enter your state: ")
    try:
        if state:
            print(f"State: {state}")
            get_weather(state)
            season = get_season(datetime.date.today())
            print(f"Current Season: {season}")
            crop_suggestions = get_crop_suggestions(state, season)
            print("Crop Suggestions (sorted by market price):")
            for crop in crop_suggestions:
                print(f"{crop['Crop']} - {crop['Market Price (INR per kg)']} INR per kg")
        else:
            print("Unable to determine the state.")

    except Exception:
        print("Invalid state name!")
        exit(0)

if __name__ == "__main__":
    main()

# translator= Translator(to_lang="Telugu")
# translation = translator.translate("Good Morning!")
# print (translation)

