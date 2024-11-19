import tkinter as tk
from tkinter import messagebox
import joblib

# Load the trained model
try:
    model = joblib.load('weather_prediction_model.pkl')
except FileNotFoundError:
    messagebox.showerror("Error", "Model file not found. Please ensure 'weather_prediction_model.pkl' is in the same directory.")
    exit()

def predict_rainfall():
    try:
        # Retrieve and validate input values
        temperature = float(entry_temperature.get().strip())
        humidity = float(entry_humidity.get().strip())
        wind_speed = float(entry_wind_speed.get().strip())
        pressure = float(entry_pressure.get().strip())
        
        # Call your model's prediction function here
        prediction = model.predict([[temperature, humidity, wind_speed, pressure]])
        
        # For demonstration, let's assume we get a prediction result
        # prediction = "Rain"  # replace with actual model prediction
        
        # Display result in the GUI
        result_text.set(f"Prediction: {prediction}")
        
    except ValueError:
        messagebox.showerror("Invalid input", "Please input valid numerical values.")

# Create the main window
window = tk.Tk()
window.title("Weather Prediction System")
window.geometry("400x400")
window.config(bg="#f2f2f2")

# Title label
title_label = tk.Label(window, text="Weather Prediction System", font=('Helvetica', 16, 'bold'), bg="#f2f2f2")
title_label.pack(pady=10)

# Input fields with frames
input_frame = tk.Frame(window, bg="#f2f2f2")
input_frame.pack(pady=10)

label_temperature = tk.Label(input_frame, text="Temperature (°C):", bg="#f2f2f2")
label_temperature.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_temperature = tk.Entry(input_frame)
entry_temperature.grid(row=0, column=1, padx=10, pady=5)

label_humidity = tk.Label(input_frame, text="Humidity (%):", bg="#f2f2f2")
label_humidity.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_humidity = tk.Entry(input_frame)
entry_humidity.grid(row=1, column=1, padx=10, pady=5)

label_wind_speed = tk.Label(input_frame, text="Wind Speed (km/h):", bg="#f2f2f2")
label_wind_speed.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_wind_speed = tk.Entry(input_frame)
entry_wind_speed.grid(row=2, column=1, padx=10, pady=5)

label_pressure = tk.Label(input_frame, text="Pressure (hPa):", bg="#f2f2f2")
label_pressure.grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_pressure = tk.Entry(input_frame)
entry_pressure.grid(row=3, column=1, padx=10, pady=5)

# Prediction button
predict_button = tk.Button(window, text="Predict Rainfall", command=predict_rainfall, font=('Helvetica', 12), bg="#4CAF50", fg="white")
predict_button.pack(pady=20)

# Display prediction result
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, font=('Helvetica', 12, 'bold'), bg="#f2f2f2")
result_label.pack(pady=10)

# Run the application
window.mainloop()
