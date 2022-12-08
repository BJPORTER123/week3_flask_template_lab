from flask import render_template, request, redirect 
from app import app
from models.instance_of_events import events
from models.events import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=['POST'])
def create(): 
    name = request.form['name']
    guests = request.form['guests']
    location = request.form['location']
    description = request.form['description']
    date = request.form['date']
    reoccuring = request.form['reoccuring']
    new_event = Event(name, guests, location, description, date, reoccuring)
    events.append(new_event)
    return redirect('/events')

