import os
import requests
from dotenv import load_dotenv
import re

# Load API key from .env file

load_dotenv(dotenv_path=r"C:/Users/som/Desktop/Sharm/Study/Colleges/Duke/STudy/PYTHON/Assignments/my-local-repo/Week5/D1/Weather_App/.gitignore/.env")
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    # 1. Create the API endpoint URL
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    # 2. Set query parameters
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"           # temperature in Celsius
    }

    # 3. Make the request
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:     #checks whether API call was successful(200 is the standard code for "OK").
        # 4. Parse JSON
        data = response.json()

        # 5. Extract key info
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        desc_lower = description.lower()
        # Advice suggestion logic
        if temp <= 10:
            advice = "🧥 It's chilly — wear a jacket."
        elif 10 < temp <= 20:
            if "rain" in desc_lower:
                advice = "🌧️ Showers expected — carry an umbrella."
            else:
                advice = "🧢 Mild day — a hat might be nice."
        else:  # temp > 20
            if "rain" in desc_lower:
                advice = "☔ Warm but rainy — take an umbrella."
            else:
                advice = "😎 Warm and clear — enjoy the day!"
        
        print(f"\n📍 Below are the weather conditions for ")

        #Highlight keywords using regex and ANSI bold
        output = (
            f"City: {city.capitalize()}\n"
            f"🌡️     Temperature: {temp}°C\n"
            f"💧    Humidity: {humidity}%\n"
            f"📝    Description: {description.capitalize()}\n"
            f"🔔    Suggestion: {advice}")
        output = re.sub(r"(Temperature|Humidity|Description|Suggestion)", r"\033[1m\1\033[0m", output)
        print("\n" + output + "\n")

    else:
        print("❌ Could not retrieve weather data. Check city name.")

if __name__ == "__main__":
    print("*" *80)
    print(" Stay informed on the weather conditions in any city! ")
    print("*" *80)
    city = input("Enter the name of the city, to know it's weather : ")
    city = re.sub(r"[^a-zA-Z\s]", "", city).strip()
    if not city:
        print("❌ Invalid input. Please enter a real city name.")
    else:
        get_weather(city)
