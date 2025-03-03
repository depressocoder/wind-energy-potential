import math
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

#Wind power calculation

def calculate_wind_energy():
    try:
        #Input Values
        wind_speed = float(entry_wind_speed.get()) #wind speed in m/s
        blade_radius = float(entry_blade_radius.get()) #Turbine blade radius in meters
        efficiency = float(entry_efficiency.get()) #Turbine efficiency in %
        air_density = 1.225 #Air density in kg/m^3

        #calculate area swept by the blades
        swept_area = math.pi * (blade_radius ** 2)

        #power output of the turbine : P = 0.5 * ρ * A * v³ * η
        power_output = 0.5 * air_density * swept_area * (wind_speed ** 3) *(efficiency/100)

        #convert watts to kwh
        energy_per_day = power_output * 24/1000 #kwh/day
        energy_per_month = energy_per_day * 30 #kwh/month
        energy_per_year = energy_per_month * 12 #kwh/year

        #display results
        result_text.set(
            f"Power Output:{power_output:.2f} W\n"
            f"Energy Per Day:{energy_per_day:.2f} kWh\n"
            f"Energy Per Month:{energy_per_month:.2f} kWh\n"
            f"Energy Per Year:{energy_per_year:.2f} kWh"
        )

        #plot generation curve
        plot_graph(energy_per_day, energy_per_month, energy_per_year)

    except ValueError:
        results_text.set("Please enter valid input values")

#Function to plot generation curve
def plot_graph(daily, monthly, yearly):
    labels = ['Daily Energy(kwh)', 'Monthly Energy(kwh)', 'Yearly Energy(kwh)']
    values = [daily, monthly, yearly]
    colors = ['red', 'blue', 'green']

    fig,ax = plt.subplots()
    ax.bar(labels,values,color=colors)
    ax.set_xlabel('Energy Kwh')
    ax.set_ylabel('Wind Energy Potential')

    #clear new graph display new one
    for widget in frame_graph.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=frame_graph)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

#GUI set up
root = tk.Tk()
root.title("Wind Energy Potential Calculator")
root.geometry("500x500")
root.configure(bg="white")

style = ttk.Style()
style.configure("TLabel",font=("Arial", 12))
style.configure("TButton",font=("Arial", 12),padding = 5)
style.configure("TEntry",font=("Arial", 12),padding = 5)

#input fields

fields = ["Wind Speed(m/s)", "Turbine Blade Radius(m)", "Turbine Efficiency(%)"]
entries = []

for i, field in enumerate(fields):
    ttk.Label(root, text=field , background="white").grid(row = i, column = 0, padx=10, pady= 10, sticky=tk.W)
    entry = ttk.Entry(root)
    entry.grid(row = i, column = 1, padx=10, pady= 10, sticky=tk.W)
    entries.append(entry)

entry_wind_speed, entry_blade_radius, entry_efficiency = entries

#calculate button

calculate_button = ttk.Button(root, text="Calculate", command=calculate_wind_energy)
calculate_button.grid(row=len(fields), column=0, columnspan=2, pady=10)


# Result Display
result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text, background="#f0f0f0", justify=tk.LEFT)
result_label.grid(row=len(fields) + 1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

# Graph Frame
frame_graph = tk.Frame(root, bg="#f0f0f0")
frame_graph.grid(row=len(fields) + 2, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI
root.mainloop()




 