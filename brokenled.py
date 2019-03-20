from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()
sense.low_light = True

r = [255,0,0]
o = [255,127,0]
y = [255,255,0]
g = [0,255,0]
b = [0,0,255]
i = [75,0,130]
v = [159,0,255]
e = [0,0,0]

color = r
 
image = [
e,e,e,e,e,e,e,e,
e,e,e,r,r,e,e,e,
e,r,r,o,o,r,r,e,
r,o,o,y,y,o,o,r,
o,y,y,g,g,y,y,o,
y,g,g,b,b,g,g,y,
b,b,b,i,i,b,b,b,
b,i,i,v,v,i,i,b
]

x = 0
y = 0
good_over_bad = 10
delay = 3
switch_delay = 1
counter = 0

sense.clear(color)

while True:
    sense.clear(e)
    time.sleep(switch_delay)
    if(randint(1, good_over_bad)== good_over_bad):
        sense.clear(color)
        x = randint(0, 9)
        y = randint(0, 9)
        sense.set_pixel(x, y, e)
    else:
        sense.clear(color)
    time.sleep(delay)
    +counter



