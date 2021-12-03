from trafficSimulator import *
from flask import Flask, render_template, request, jsonify
import json, logging, os, atexit

app = Flask(__name__, static_url_path='')

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))


@app.route('/')
def root():
    return jsonify([{"message":"Pruebas Tec, from IBM Cloud!"}])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)

sim = Simulation()

sim.create_roads([
    ((0, 100), (148, 100)),
    ((148, 100), (300, 100)),

    ((300, 95), (158, 95)),
    ((158, 95), (0, 95)),
    
    ((150, 0), (150, 92)),
    ((150, 92), (150, 200)),

    ((155, 200), (155, 102)),
    ((155, 102), (155, 0))
])

sim.create_gen({
    'vehicle_rate': 30,
    'vehicles': [
        [1, {"path": [0, 1]}],
        [1, {"path": [2, 3]}],
        [1, {"path": [4, 5]}],
        [1, {"path": [6, 7]}]
    ]
})

sim.create_signal([[0], [4]])
sim.create_signal([[2], [6]])


win = Window(sim)
win.offset = (-150, -110)
win.run(steps_per_update=10)