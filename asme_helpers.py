"""Helpers for ASME Lightboard Python Event

See function definitions for help on what they do/what you can use them for.

NOTE: Install `opencv-python` module for reading images.

Author: Yurgen C. Hohmeyer // hohmeyyc@clarkson.edu
Feel free to email me with any questions!
"""

import cv2

# Fill board with this value to turn off pixels
# E.g. BOARD_LEFT.fill(OFF)
OFF = (0, 0, 0, 0)


def setpixels(board, locs, color):
	"""Sets locations on a board to a given color.

	Parameters
	----------
	board : NeoPixel
		NeoPixel board to set colors on
	locs : Union(slice, list, int)
		Location, slice of locations, or list of locations to set
	color : Tuple
		Tuple of RGB(W) colors to set
		r	Red brightness, 0 = minimum (off), 255 = maximum.
		g	Green brightness, 0 = minimum (off), 255 = maximum.
		b	Blue brightness, 0 = minimum (off), 255 = maximum.
		w	White brightness, 0 = minimum (off), 255 = maximum.
	"""
	if isinstance(locs, slice):
		board[locs] = [color] * len(board[locs])
	elif isinstance(locs, list):
		for loc in locs:
			setpixels(board, loc, color)
	else:
		board[locs] = color


def show_image(imgpath, board):
	"""Show an image on the board.

	Shrinks an image to 64x64 pixels and sets each pixel to the color of the image.

	Parameters
	----------
	imgpath : PathLike
		Path to the image to show
	board : NeoPixel
		Neopixel board to show image on
	"""
	image = cv2.imread(imgpath)
	resized = cv2.resize(image, (8, 8), interpolation=cv2.INTER_AREA)

	fill_colors = []

	for y in range(0, 8):
		for x in range(0, 8):

			pixel_color = [0, 0, 0, 0]

			for channel in range(0, 3):
				pixel_color[channel] = resized[y][x][channel]

			fill_colors.append(pixel_color)

	for i, color in enumerate(fill_colors):
		setpixels(board, i, color)
