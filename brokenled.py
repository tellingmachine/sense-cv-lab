from sense_hat import SenseHat

sense = SenseHat()
sense.low_light = True

r = 255
g = 255
b = 255

print(sense.gamma)

sense.clear((0, 0, b))