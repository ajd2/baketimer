from flask import Flask, request, render_template
import datetime
from dateutil import parser

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def bake_page():
    return render_template("index.html")

@app.route('/calculation')

def baking_times():
    start= request.args
    starttime = start["time"]
    realtime = parser.parse(starttime)  #takes input from index.html and converts into readable time

# sets time intevals for each step of recipe with 12-hour rise time
    dough_ready12 = realtime + datetime.timedelta(hours=12)
    plast_wait12 = dough_ready12 + datetime.timedelta(minutes=15)
    oven_time12 = plast_wait12 + datetime.timedelta(minutes=90)
    dough_oven_time12 = oven_time12 + datetime.timedelta(minutes=30)
    lid_off12 = dough_oven_time12 + datetime.timedelta(minutes=30)
    last_check12 = lid_off12 + datetime.timedelta(minutes=15)

# sets time intevals for each step of recipe with 18-hour rise time
    dough_ready18 = realtime + datetime.timedelta(hours=18)
    plast_wait18 = dough_ready18 + datetime.timedelta(minutes=15)
    oven_time18 = plast_wait18 + datetime.timedelta(minutes=90)
    dough_oven_time18 = oven_time18 + datetime.timedelta(minutes=30)
    lid_off18 = dough_oven_time18 + datetime.timedelta(minutes=30)
    last_check18 = lid_off18 + datetime.timedelta(minutes=15)

# converts times into "8:30pm" format
    def formatted_time(a):
        return str(a.strftime('%I:%M %p'))

#creates variables of all the times in the "8:30pm format"
    realtime1 = formatted_time(realtime)

    dough_ready = formatted_time(dough_ready12)
    plast_wait = formatted_time(plast_wait12)
    oven_time = formatted_time(oven_time12)
    dough_oven_time = formatted_time(dough_oven_time12)
    lid_off = formatted_time(lid_off12)
    last_check = formatted_time(last_check12)

    dough_ready1 = formatted_time(dough_ready18)
    plast_wait1 = formatted_time(plast_wait18)
    oven_time1 = formatted_time(oven_time18)
    dough_oven_time1 = formatted_time(dough_oven_time18)
    lid_off1 = formatted_time(lid_off18)
    last_check1 = formatted_time(last_check18)

#inputs variables as text into calculation.html

    return render_template("calculation.html", realtime1=realtime1, dough_ready=dough_ready, plast_wait=plast_wait, oven_time=oven_time, dough_oven_time=dough_oven_time, lid_off=lid_off, last_check=last_check, dough_ready1=dough_ready1, plast_wait1=plast_wait1, oven_time1=oven_time1, dough_oven_time1=dough_oven_time1, lid_off1=lid_off1, last_check1=last_check1)
