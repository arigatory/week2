from flask import Flask
from flask import render_template

from data import tours
from data import departures

app = Flask(__name__)


@app.route('/')
def render_index():
    output = render_template('index.html', tours=tours, departures=departures)
    return output


@app.route('/tours/<int:id>/')
def render_tour(id):
    return render_template('tour.html', tour=tours[id], departures=departures)


@app.route('/departures/<departure>/')
def render_departure(departure):
    filtered_tours = {key: value for (key, value) in tours.items() if value['departure'] == departure}
    return render_template('departure.html', departures=departures, departure=departure, tours=filtered_tours)


app.run("0.0.0.0",5000)
