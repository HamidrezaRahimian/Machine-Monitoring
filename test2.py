import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# Sample data
machines = [
    {
        "name": "machine1",
        "status": "running",
        "progress": 95,
        "consumption": 85,
        "temperature": 35,
        "time": 120,
        "cpu_usage": 13,
        "id": 1001
    },
    {
        "name": "machine2",
        "status": "warning",
        "progress": 5,
        "consumption": 15,
        "temperature": 18,
        "time": 5,
        "cpu_usage": 4,
        "id": 1002
    },
    {
        "name": "machine3",
        "status": "running",
        "progress": 85,
        "consumption": 65,
        "temperature": 25,
        "time": 120,
        "cpu_usage": 4,
        "id": 1003
    },
    {
        "name": "machine4",
        "status": "fatal",
        "progress": 3,
        "consumption": 280,
        "temperature": 44,
        "time": 270,
        "cpu_usage": 73,
        "id": 1004
    }
]

# Function to plot gauge diagrams
def plot_gauge(machine):
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    
    labels = ['Progress', 'Consumption', 'Temperature', 'CPU Usage']
    data = [machine['progress'], machine['consumption'], machine['temperature'], machine['cpu_usage']]
    ranges = [(0, 100), (0, 300), (0, 50), (0, 100)]
    
    for ax, label, value, (min_val, max_val) in zip(axs.flatten(), labels, data, ranges):
        ax.set_aspect('equal', 'box')
        ax.set_title(label)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.add_artist(plt.Circle((0, 0), 1.2, color='lightgray', fill=True, linewidth=1.5, zorder=0))
        ax.add_artist(plt.Circle((0, 0), 1, color='white', fill=True, linewidth=0, zorder=1))
        ax.add_artist(plt.Circle((0, 0), 1, color='lightgreen', fill=True, linewidth=0, zorder=2, alpha=value/max_val))
        ax.text(0, -0.25, f'{value}', fontsize=12, ha='center')
        ax.text(0, 0.5, f'{label}', fontsize=14, ha='center')
    
    plt.tight_layout()
    plt.show()

# Dropdown widget for machine selection
machine_dropdown = widgets.Dropdown(
    options=[(machine['name'], machine) for machine in machines],
    description='Machine:',
)

# Event handler for dropdown change
def on_dropdown_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        selected_machine = change['new']
        plot_gauge(selected_machine)

machine_dropdown.observe(on_dropdown_change)

display(machine_dropdown)
