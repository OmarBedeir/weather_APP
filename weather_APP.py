

import tkinter as tk
import requests
def get_weather(city):
    #  "_API_KEY" 
    api_key = "fae60fc10a0349a563bb2770913bd1c7"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Check for errors in the response
        weather_data = response.json()

        # Update labels with weather information
        temperature_label.config(text=f"Temperature: {weather_data['main']['temp']}°C")
        humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")
        wind_speed_label.config(text=f"Wind Speed: {weather_data['wind']['speed']} km/h")
        pressure_label.config(text=f"Pressure: {weather_data['main']['pressure']} hPa")
        precipitation_label.config(text=f"Precipitation: {weather_data.get('rain', {}).get('1h', 0)} mm")
    except requests.exceptions.RequestException as e:
        # Handle errors such as no internet connection or invalid city
        temperature_label.config(text="Error fetching data")
        humidity_label.config(text="")
        wind_speed_label.config(text="")
        pressure_label.config(text="")
        precipitation_label.config(text="")
root = tk.Tk()
root.title("Weather App")

# Entry for entering the location
location_entry = tk.Entry(root, width=30)
location_entry.grid(row=0, column=0, padx=10, pady=10)

# Button to trigger weather information retrieval
search_button = tk.Button(root, text="Search", command=lambda: get_weather(location_entry.get()))
search_button.grid(row=0, column=1, padx=10, pady=10)

# Labels to display weather information
temperature_label = tk.Label(root, text="Temperature: ")
temperature_label.grid(row=1, column=0, padx=10, pady=5)

humidity_label = tk.Label(root, text="Humidity: ")
humidity_label.grid(row=2, column=0, padx=10, pady=5)

wind_speed_label = tk.Label(root, text="Wind Speed: ")
wind_speed_label.grid(row=3, column=0, padx=10, pady=5)

pressure_label = tk.Label(root, text="Pressure: ")
pressure_label.grid(row=4, column=0, padx=10, pady=5)

precipitation_label = tk.Label(root, text="Precipitation: ")
precipitation_label.grid(row=5, column=0, padx=10, pady=5)

root.mainloop()
