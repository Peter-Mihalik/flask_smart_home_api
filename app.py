from flask import Flask, redirect, request
from flask.helpers import make_response, url_for
from flask.templating import render_template
import requests as rq
import json
import time
import math


def time_to_minutes(cur_time: str) -> int:
    cur_time = cur_time.split(':')
    if cur_time[0][0] == '0':
        hours = cur_time[0][1]
    else:
        hours = cur_time[0]
    if cur_time[1][0] == '0':
        minutes = cur_time[1][1]
    else:
        minutes = cur_time[1]
    time_minutes = int(hours) * 60 + int(minutes)
    return time_minutes


def sunrise(current_time: str, time_in_minutes: int):
    # Start Sunrise
    if current_time == '05:53':  # 05:53 is one hour and half before sunrise in the time of making this
        tmps = []
        for key, value in devices.items():
            ip = value['light']
            url = 'http://home_automation.iamroot.eu/device/'+ip+'/color_temperature/2300'
            temp = rq.get(url).json()['color_temperature']
            tmps.append(temp)
        return str(tmps)
    # Adjust light tempreature while sunrise
    if 443 > time_in_minutes and time_in_minutes > 353:
        # 443 is 05:53 (Sunrise) in minutes 353 is one hour and half before sunrise in minutes
        tmps = []
        for key, value in devices.items():
            # Get current tempreature
            ip = value['light']
            url = 'http://home_automation.iamroot.eu/device/'+ip
            color_temp = rq.get(url).json()['color_temperature']
            # Change Tempreature
            url = 'http://home_automation.iamroot.eu/device/' + \
                ip+'/color_temperature/'+str(color_temp+46)
            color_temp_new = rq.get(url).json()['color_temperature']
            tmps.append(color_temp_new)
        return str(tmps)
    # End Sunrise
    if current_time == '07:23':  # 07:23 is time of the sunrise
        tmps = []
        for key, value in devices.items():
            ip = value['light']
            url = 'http://home_automation.iamroot.eu/device/'+ip+'/color_temperature/6500'
            temp = rq.get(url).json()['color_temperature']
            tmps.append(temp)
        return str(tmps)
    return 'Not the right time for the sunrise'


def sunset(current_time: str, time_in_minutes: int):
    # Start Sunset
    if current_time == '14:20':  # 14:20 is one hour and half before sunset in the time of making this
        tmps = []
        for key, value in devices.items():
            ip = value['light']
            url = 'http://home_automation.iamroot.eu/device/'+ip+'/color_temperature/6500'
            temp = rq.get(url).json()['color_temperature']
            tmps.append(temp)
        return str(tmps)
    # Adjust light tempreature while sunset
    if 950 > time_in_minutes and time_in_minutes > 860:
        # 950 is 15:50 (Sunset) in minutes 860 is one hour and half before sunset in minutes
        tmps = []
        for key, value in devices.items():
            # Get current tempreature
            ip = value['light']
            url = 'http://home_automation.iamroot.eu/device/'+ip
            color_temp = rq.get(url).json()['color_temperature']
            # Change Tempreature
            url = 'http://home_automation.iamroot.eu/device/' + \
                ip+'/color_temperature/'+str(color_temp-46)
            color_temp_new = rq.get(url).json()['color_temperature']
            tmps.append(color_temp_new)
        return str(tmps)
    # End Sunset
    if current_time == '15:50':  # '15:50' is t
        tmps = []
        for key, value in devices.items():
            ip = value['light']
            url = 'http://home_automation.iamroot.eu/device/'+ip+'/color_temperature/2300'
            temp = rq.get(url).json()['color_temperature']
            tmps.append(temp)
        return str(tmps)
    return 'Not the right time for the sunset'


app = Flask('Smart Home', template_folder='templates/')

devices = {
    'livingroom': {
        'light': '9b18303c-5630-4256-ba63-88bc530a38e1',
        'switch': '36260ff6-c936-4bc3-a6d0-8445b606af12',
        'motion-sensor': '16791e0b-69c2-4e62-919f-f1eb0296ca6a',
        'smart-plug': '8615d7a5-ac68-49a6-bf29-40e693fa28e7'},
    'kitchen': {
        'light': '993b94a8-a92d-4758-8a32-787ae008d3a6',
        'switch': '287beef9-da2d-4a7f-9518-de2185915a90',
        'motion-sensor': '070e5685-65fc-48b6-8fc4-d3e8c19ed36d',
        'smart-plug': 'ffdf6351-4589-40d3-b822-b301772f5421'},
    'bathroom': {
        'light': 'ff042c4b-28d9-4ebe-aa37-b3de61ac80cc',
        'switch': '5f8be8b8-5594-4f36-be43-6c130cca8396',
        'smart-plug': 'c1df3780-d7da-4df6-936a-f4f809d1f0d9'},
    'karsobs room': {
        'light': '95c81245-37f5-455b-b045-3b4665cf5176',
        'switch': 'a3cebc1c-ead8-4e36-9c04-1d54e29de872',
        'smart-plug': '3b388755-8dbf-4919-aba3-884ad1888fc4'},
    'karliks room': {
        'light': '4515542a-68de-4a33-b20d-39d34e2582be',
        'switch': '403af07c-e5c2-43a8-9243-d60bfe2e966f',
        'smart-plug': '06a521df-3394-4b00-b78c-19c9ffa84585'},
    'julias room': {
        'light': 'c5c82596-a1c1-494b-b713-ccf4d5782d10',
        'switch': '92921bd8-e37f-4cd0-a7c0-db5c5b708a20',
        'smart-plug': '800378e2-875d-40a8-983d-af8029e8a28b'},
    'karloss room': {
        'light': '1b9ac043-bb23-4620-83da-8a681be3ca19',
        'switch': 'de5ecd73-9e95-40e6-9b92-5a7e62587f35',
        'smart-plug': '9a84b84a-1838-4346-adc5-cfe45da9fbaf'}
}


@app.route('/')
def home_page():
    user = request.cookies.get('user')
    if user == None:
        return redirect(url_for('login_page'))
    else:
        # GET LIGHTS STATES
        lights = []
        for key, value in devices.items():
            req = rq.get('http://home_automation.iamroot.eu/device/' +
                         value['light']).text
            lights.append((key, json.loads(req)))
        return render_template('index.html', user=user, lights=lights)


@app.route('/login', methods=['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        user = request.form['name']

        resp = make_response(redirect(url_for('home_page')))
        resp.set_cookie('user', user)
        return resp
    else:
        return render_template('login.html')


@app.route('/device-table', methods=['POST', 'GET'])
def device_table_page():
    user = request.cookies.get('user')
    if user == None:
        return redirect(url_for('login_page'))
    else:
        return render_template('device-table.html', devices=devices, url='http://home_automation.iamroot.eu/device/')


@app.route('/detect-motion', methods=['POST', 'GET'])
def detect_motion():
    if request.method == 'POST':
        ip = request.form['ip']
        req = rq.get(
            'http://home_automation.iamroot.eu/device/' + ip + '/trigger')
        return redirect(url_for('home_page'))
    else:
        return render_template('detect-motion.html')


@app.route('/switch-light', methods=['POST', 'GET'])
def switch_light():
    if request.method == 'POST':
        ip = request.form['ip']
        req = rq.get('http://home_automation.iamroot.eu/device/'+ip+'/trigger')
        return redirect(url_for('home_page'))


# Need to create cron for one minute interval to /cron endpoint
@app.route("/cron")
def cron():
    # do here anything, that should be done periodically
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    time_in_minutes = time_to_minutes(current_time)
    # Sunset
    sunset_res = sunset(current_time, time_in_minutes)
    sunrise_res = sunrise(current_time, time_in_minutes)
    if not 'sunset' in sunset_res:
        return sunset_res
    elif not 'sunrise' in sunrise_res:
        return sunrise_res
    else:
        return sunset_res + '<br>' + sunrise_res
