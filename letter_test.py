import time
import board
import neopixel

# We're using GPIO18 and GPIO21 for the two boards
pin1 = board.D18
pin2 = board.D21

# Pixel order of the board we bought
order = neopixel.GRBW

# We bought 64 pixel boards
numpixels = 64

# Brightness and automatically set colors
bright = 0.5
aw = False

# Board setup
board1 = neopixel.NeoPixel(pin1, numpixels, brightness=bright, auto_write=aw, pixel_order=order)
board2 = neopixel.NeoPixel(pin2, numpixels, brightness=bright, auto_write=aw, pixel_order=order)

def setpixels(board, locs, color):
    if isinstance(locs, slice):
        board[locs] = [color] * len(board[locs])
    elif isinstance(locs, list):
        for loc in locs:
            setpixels(board, loc, color)
    else:
        board[locs] = color

# For Neopixel Raspberry Pi Code
cuGold = (255,206,0,0)
cuGreen = (0,220,10,0)
backgroundColor = (0,0,0,0)
OFF = (0,0,0,0)

letterColor = cuGold
i = 1
while i < 5:
    # Letter C
    board1.fill(backgroundColor)
    setpixels(board1, [10,11,12,13,18,26,34,42,slice(50,54)], letterColor)

    # Letter U
    board2.fill(backgroundColor)
    setpixels(board2, [10,13,18,21,26,29,34,37,42,45,50,slice(51,54)], cuGreen)
    board1.show()
    board2.show()
    time.sleep(2)

    # Letter A
    board1.fill(backgroundColor)
    setpixels(board1, [slice(10,14),18,21,slice(26,30),34,37,42,45,50,53], cuGreen)

    # Letter S
    board2.fill(backgroundColor)
    setpixels(board2, [slice(10,14),18,slice(26,29),37,45,slice(50,54)], letterColor)
    board1.show()
    board2.show()
    time.sleep(2)

    # Letter M
    board1.fill(backgroundColor)
    setpixels(board1, [9,10,13,14,slice(17,23),25,27,28,30,33,38,41,46,49,54], letterColor)

    # Letter E
    board2.fill(backgroundColor)
    setpixels(board2, [slice(10,14),18,slice(26,30),34,42,slice(50,54)], cuGreen)
    board1.show()
    board2.show()
    time.sleep(2)
    i += 1

board1.fill(OFF)
board2.fill(OFF)
board1.show()
board2.show()
