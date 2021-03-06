import os
import json
import requests
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route('/')
def index():
    # upcoming =\
    #   requests.get("http://api.songkick.com/api/3.0/artists/864070/calendar.json?apikey=zdpZeMNcromcrzB4&order=desc")
    # past =\
    #   requests.get("http://api.songkick.com/api/3.0/artists/864070/gigography.json?apikey=zdpZeMNcromcrzB4&order=desc")
    return render_template('home.html')
			   # results_upcoming=upcoming.json(),
			   # results_past=past.json())

@app.route('/epk')
def epk():
    # upcoming =\
    #   requests.get("http://api.songkick.com/api/3.0/artists/864070/calendar.json?apikey=zdpZeMNcromcrzB4&order=desc")
    # past =\
    #   requests.get("http://api.songkick.com/api/3.0/artists/864070/gigography.json?apikey=zdpZeMNcromcrzB4&order=desc")
    return render_template('epk.html')
			   # results_upcoming=upcoming.json(),
			   # results_past=past.json())

@app.route('/reel')
def reel():
    return render_template('reel.html')

@app.route('/tour_dates')
def tour_dates():
    return render_template('_tour_dates.html')

@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"

if __name__ == '__main__':
    app.run(app.config['IP'], app.config['PORT'])
