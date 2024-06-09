from flask import Flask, jsonify

app = Flask(__name__)

# Define your machine data
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

@app.route('/machines', methods=['GET'])
def get_machines():
    return jsonify({"machines": machines})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
