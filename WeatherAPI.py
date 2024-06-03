import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw 
import requests

def get_weather():
    city = city_entry.get()
    api_key = "42f7575d177c39bf6156e2b68c84381d" 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            temperature = data["main"]["temp"]
            min_temperature = data["main"]["temp_min"]
            max_temperature = data["main"]["temp_max"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            description = data["weather"][0]["description"]
            
           
            weather_info_label.config(text=f"Weather in {city}: {description.capitalize()} \n\n"
                                            f"🌡️ Temperature: {temperature}°C\n"
                                            f"🔻 Min Temperature: {min_temperature}°C\n"
                                            f"🔺 Max Temperature: {max_temperature}°C\n"
                                            f"💧 Humidity: {humidity}%\n"
                                            f"💨 Wind Speed: {wind_speed} m/s",
                                            fg="#333", font=("Helvetica", 12), justify="left", padx=20, pady=10)
        else:
            messagebox.showerror("Error", f"City not found: {data['message']}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


root = tk.Tk()
root.title("Weather Report System")


bg_image = Image.open("banner.png")
bg_image = bg_image.resize((640, 480), Image.ANTIALIAS)  
bg_image = ImageTk.PhotoImage(bg_image)


canvas = tk.Canvas(root, width=600, height=4
                   00)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=bg_image)


city_frame = tk.Frame(root, bg="#f0f0f0")
city_frame.pack(padx=20, pady=(10, 5), fill="x")
city_label = tk.Label(city_frame, text="Enter a city:", bg="#f0f0f0", fg="#333", font=("Helvetica", 14))
city_label.pack(side="left")
city_entry = tk.Entry(city_frame, font=("Helvetica", 14))
city_entry.pack(side="left", fill="x", expand=True)


get_weather_button = tk.Button(root, text="Get Weather", command=get_weather, bg="#4CAF50", fg="white", font=("Helvetica", 14))
get_weather_button.pack(pady=(5, 10), fill="x")


weather_info_label = tk.Label(root, bg="#f0f0f0", fg="#333", font=("Helvetica", 12), justify="left", padx=20, pady=10)
weather_info_label.pack(fill="both", expand=True)


footer_label = tk.Label(root, text="Made by Mangal Krishna Singh Bhadoriya", bg="#333", fg="white", font=("Helvetica", 10))
footer_label.pack(fill="x", padx=1, pady=5)

root.mainloop()
