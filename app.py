import time
import gpiozero
from flask import Flask, render_template, request

RELAY_PIN1 = 12
RELAY_PIN2 = 16
RELAY_PIN3 = 20
RELAY_PIN4 = 21


app = Flask(__name__)
relay1 = gpiozero.OutputDevice(RELAY_PIN1, active_high=False, initial_value=False)
relay2 = gpiozero.OutputDevice(RELAY_PIN2, active_high=False, initial_value=False)
relay3 = gpiozero.OutputDevice(RELAY_PIN3, active_high=False, initial_value=False)
relay4 = gpiozero.OutputDevice(RELAY_PIN4, active_high=False, initial_value=False)

@app.route('/')
def index():
    templateData = { 'r1' : "on" if relay1.value else "off",
    'r2' : 'on' if relay2.value else 'off',
    'r3' : 'on' if relay3.value else 'off',
    'r4' : 'on' if relay4.value else 'off' }
    return render_template('index.html', **templateData)

@app.route('/<device>')
def do(device):
    if device == "r1":
        relay1.toggle()
    if device == "r2":
        relay2.toggle()
    if device == "r3":
        relay3.toggle()
    if device == "r4":
        relay4.toggle()
    templateData = { 'r1' : "on" if relay1.value else "off",
    'r2' : 'on' if relay2.value else 'off',
    'r3' : 'on' if relay3.value else 'off',
    'r4' : 'on' if relay4.value else 'off' }
    return render_template('index.html', **templateData)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
"""
    print("relay test start complete on 3.5 sec")
    relay1.on()
    time.sleep(0.5)
    relay2.on()
    time.sleep(0.5)
    relay3.on()
    time.sleep(0.5)
    relay4.on()
    print ("all on ")
    time.sleep(0.5)
    relay1.off()
    time.sleep(0.5)
    relay2.off()
    time.sleep(0.5)
    relay3.off()
    time.sleep(0.5)
    relay4.off()
    print("all off ")
    print("quit test")
"""
#    app.run(debug=True, host='0.0.0.0')
