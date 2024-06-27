import tkinter as tk
import requests
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    api_key = '7136c9ff19e161d760234a11d0c87315'  # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        data = response.json()
        weather_info = {
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        display_weather(weather_info)
    except Exception as e:
        messagebox.showerror('Error', f'Error fetching weather information: {e}')

def display_weather(weather_info):
    weather_display.config(text=f"Weather: {weather_info['description']}\n"
                                 f"Temperature: {weather_info['temperature']}°C\n"
                                 f"Humidity: {weather_info['humidity']}%\n"
                                 f"Wind Speed: {weather_info['wind_speed']} m/s")

# GUI Setup
root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

weather_display = tk.Label(root, text="")
weather_display.pack()

root.mainloop()


