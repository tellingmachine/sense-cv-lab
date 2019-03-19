from sense_hat import SenseHat
import time

sense = SenseHat()
sense.low_light = True

r = 255
g = 255
b = 255


sense.clear((r, 0, b))

sense.set_pixel(2, 2, [0, 0, 0])

time.sleep(3)

sense.set_pixel(2, 2, [r, 0, b])
