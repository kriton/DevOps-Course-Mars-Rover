import os
from flask import Flask, render_template, request, redirect, url_for
import requests
from datetime import date,timedelta

app = Flask(__name__)

@app.route('/')
def index():
    api_key=os.getenv('API_KEY')
    nasa=requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}").json()
    return render_template('index.html', landing_image=nasa['url'])

@app.route('/mars')
def mars():
    api_key=os.getenv('API_KEY')
    nasa_mars=requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date.today() - timedelta(days=1)}&api_key={api_key}").json()
    return render_template('mars.html',mars_image=nasa_mars['photos'])
