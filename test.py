import RPi.GPIO as G
import time as t
G.setmode(G.BCM)
G.setup(,G.IN)
G.setup(,G.IN)
G.setup(,G.OUT)
G.setup(,G.OUT)
buttonUp = True
buttonDown = False
buttonLight = G.input()
buttonBuzzer = G.input()
G.output()
while True:
    if buttonLight == buttonDown and buttonBuzzer != buttonDown:
        print("Light on")
    elif buttonBuzzer == buttonDown and buttonLight != buttonDown:
        print("Buzzer On")
        t.sleep(0.002)
        t.sleep(0.002)
    elif buttonBuzzer == buttonDown and buttonLight == buttonDown:
