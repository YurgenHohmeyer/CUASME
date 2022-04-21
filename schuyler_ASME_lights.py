import time
from asme_helpers import OFF
import board
import neopixel

from neopixel_utils import setpixels

# We're using GPIO18 and GPIO21 for the two boards
pin1 = board.D18
pin2 = board.D21

# Pixel order of the board we bought
order = neopixel.GRBW

# We bought 64 pixel boards
numpixels = 64

# Brightness and automatically set colors
bright = 0.75
aw = False

# Board setup
board1 = neopixel.NeoPixel(pin1,
                           numpixels,
                           brightness=bright,
                           auto_write=aw,
                           pixel_order=order)
board2 = neopixel.NeoPixel(pin2,
                           numpixels,
                           brightness=bright,
                           auto_write=aw,
                           pixel_order=order)

while True:
	setpixels(board1, [10, 11, 17, 26, 35, 41, 42, 14, 22, 30, 38, 46, 31],
	          (168, 22, 212, 0))
	time.sleep(2)
	setpixels(board2, [16, 32, 41, 9, 29, 37, 45, 11, 20, 22, 15],
	          (168, 22, 212, 0))
	time.sleep(4)
	board1.fill(OFF)
	board2.fill(OFF)
