import json
import csv

# Your JSON data
data = {
    "machines": [
        {
            "name": "machine1",
            "status": "running",
            "progress ": 95,
            "consumption": 85,
            "temprature": 35,
            "time": 120,
            "cpu-usage": 13,
            "id": 1001
        },
        {
            "name": "machine2",
            "status": "warning",
            "progress ": 5,
            "consumption": 15,
            "temprature": 18,
            "time": 5,
            "cpu-usage": 4,
            "id": 1002
        },
        {
            "name": "machine3",
            "status": "running",
            "progress ": 85,
            "consumption": 65,
            "temprature": 25,
            "time": 120,
            "cpu-usage": 4,
            "id": 1003
        },
        {
            "name": "machine4",
            "status": "fatal",
            "progress ": 3,
            "consumption": 280,
            "temprature": 44,
            "time": 270,
            "cpu-usage": 73,
            "id": 1004
        }
    ]
}

# Convert JSON to CSV
csv_file = "machines_data.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(data["machines"][0].keys())
    # Write data
    for machine in data["machines"]:
        writer.writerow(machine.values())

print(f"Data has been written to {csv_file}")
