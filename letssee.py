import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import numpy as np
import pandas as pd
import ipywidgets as widgets
from ipywidgets import interact

# Sample JSON data
data = {
    "machines": 
    [
        {
            "name": "machine1",
            "status": "running",
            "progress": 95,
            "consumption": 85,
            "temprature": 35,
            "time": 120,
            "cpu-usage": 13,
            "id": 1001
        },
        {
            "name": "machine2",
            "status": "warning",
            "progress": 5,
            "consumption": 15,
            "temprature": 18,
            "time": 5,
            "cpu-usage": 4,
            "id": 1002
        },
        {
            "name": "machine3",
            "status": "running",
            "progress": 85,
            "consumption": 65,
            "temprature": 25,
            "time": 120,
            "cpu-usage": 4,
            "id": 1003
        },
        {
            "name": "machine4",
            "status": "fatal",
            "progress": 3,
            "consumption": 280,
            "temprature": 44,
            "time": 270,
            "cpu-usage": 73,
            "id": 1004
        }
    ]
}

# Convert to DataFrame
df = pd.json_normalize(data, 'machines')

# Clean column names
df.columns = df.columns.str.strip()

# Function to create a gauge chart
def create_gauge(ax, value, label, min_val=0, max_val=100):
    """
    Create a gauge chart.
    
    Parameters:
    ax (matplotlib.axes._subplots.AxesSubplot): The axes on which to plot the gauge.
    value (float): The value to be displayed on the gauge.
    label (str): The label for the gauge.
    min_val (float): The minimum value of the gauge.
    max_val (float): The maximum value of the gauge.
    """
    # Create background
    ax.add_patch(Wedge((0.5, 0.5), 0.4, 0, 180, facecolor='lightgray'))
    
    # Create filled part of the gauge
    theta = (value - min_val) / (max_val - min_val) * 180
    ax.add_patch(Wedge((0.5, 0.5), 0.4, 0, theta, facecolor='steelblue'))
    
    # Create needle
    ax.plot([0.5, 0.5 + 0.35 * np.cos(np.deg2rad(180 - theta))],
            [0.5, 0.5 + 0.35 * np.sin(np.deg2rad(180 - theta))], 
            lw=2, color='black')
    
    # Add label and value
    ax.text(0.5, 0.25, f'{value}%', horizontalalignment='center', fontsize=14, weight='bold')
    ax.text(0.5, 0.15, label, horizontalalignment='center', fontsize=12)
    
    # Remove ticks and spines
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

# Function to display data for a selected machine
def display_machine_data(machine_name):
    machine_data = df[df['name'] == machine_name].iloc[0]
    
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    fig.suptitle(f'Machine: {machine_name}', fontsize=16)
    
    create_gauge(axes[0], machine_data['progress'], 'Progress')
    create_gauge(axes[1], machine_data['consumption'], 'Consumption')
    create_gauge(axes[2], machine_data['temprature'], 'Temperature')
    create_gauge(axes[3], machine_data['cpu-usage'], 'CPU Usage')
    
    plt.show()

# Interactive widget for machine selection
machine_names = df['name'].tolist()
interact(display_machine_data, machine_name=widgets.Dropdown(options=machine_names, description='Machine:'))
