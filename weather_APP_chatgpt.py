import tkinter as tk
from tkinter import messagebox
import requests

class WeatherApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Weather App")

        self.location_entry = tk.Entry(self.root, width=30)
        self.location_entry.grid(row=0, column=0, padx=10, pady=10)

        self.search_button = tk.Button(self.root, text="Search", command=self.get_weather)
        self.search_button.grid(row=0, column=1, padx=10, pady=10)

        self.temperature_label = tk.Label(self.root, text="Temperature: ")
        self.temperature_label.grid(row=1, column=0, padx=10, pady=5)

        self.humidity_label = tk.Label(self.root, text="Humidity: ")
        self.humidity_label.grid(row=2, column=0, padx=10, pady=5)

        self.wind_speed_label = tk.Label(self.root, text="Wind Speed: ")
        self.wind_speed_label.grid(row=3, column=0, padx=10, pady=5)

        self.pressure_label = tk.Label(self.root, text="Pressure: ")
        self.pressure_label.grid(row=4, column=0, padx=10, pady=5)

        self.precipitation_label = tk.Label(self.root, text="Precipitation: ")
        self.precipitation_label.grid(row=5, column=0, padx=10, pady=5)

        # Unit conversion variable
        self.units_var = tk.StringVar(value="metric")

        # Unit conversion dropdown
        units_label = tk.Label(self.root, text="Units: ")
        units_label.grid(row=6, column=0, padx=10, pady=5)

        units_menu = tk.OptionMenu(self.root, self.units_var, "metric", "imperial")
        units_menu.grid(row=6, column=1, padx=10, pady=5)

        # History feature
        history_label = tk.Label(self.root, text="Search History: ")
        history_label.grid(row=7, column=0, padx=10, pady=5)

        self.history_listbox = tk.Listbox(self.root, width=30, height=5)
        self.history_listbox.grid(row=7, column=1, padx=10, pady=5)

        view_history_button = tk.Button(self.root, text="View History", command=self.show_history)
        view_history_button.grid(row=8, column=0, columnspan=2, pady=10)

        # Initialize history list
        self.history = []

        self.root.mainloop()

    def get_weather(self):
        city = self.location_entry.get()
        if not city:
            messagebox.showwarning("Warning", "Please enter a city name.")
            return

        try:
            api_key = "fae60fc10a0349a563bb2770913bd1c7"
            base_url = "http://api.openweathermap.org/data/2.5/weather"
            params = {"q": city, "appid": api_key, "units": self.units_var.get()}
            response = requests.get(base_url, params=params)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            weather_data = response.json()

            # Update labels with weather information
            self.temperature_label.config(text=f"Temperature: {weather_data['main']['temp']}°C")
            self.humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")
            self.wind_speed_label.config(text=f"Wind Speed: {weather_data['wind']['speed']} km/h")
            self.pressure_label.config(text=f"Pressure: {weather_data['main']['pressure']} hPa")
            self.precipitation_label.config(text=f"Precipitation: {weather_data.get('rain', {}).get('1h', 0)} mm")

            # Add to history
            self.history.append(city)
            self.update_history_listbox()

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def update_history_listbox(self):
        # Clear and update the history listbox
        self.history_listbox.delete(0, tk.END)
        for item in self.history:
            self.history_listbox.insert(tk.END, item)

    def show_history(self):
        # Display a messagebox with the full search history
        history_text = "\n".join(self.history)
        messagebox.showinfo("Search History", f"Search History:\n\n{history_text}")

if __name__ == "__main__":
    app = WeatherApp()
