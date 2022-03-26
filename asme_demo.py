import time
import board
import neopixel

from neopixel_tests import letter_test, image_test

# We're using GPIO18 and GPIO21 for the two boards
pin1 = board.D18
pin2 = board.D21

# Pixel order of the board we bought
order = neopixel.GRBW

# We bought 64 pixel boards
numpixels = 64

# Brightness and automatically set colors
bright = 0.2
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

# letter_test(board1, board2)
image_test(board1, board2)
