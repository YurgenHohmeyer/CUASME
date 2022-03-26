from time import time
import cv2

# Turn off pixels
OFF = (0, 0, 0, 0)


def setpixels(board, locs, color):
	"""Sets locations on a neopixel board to a given color.

	Parameters
	----------
	board : NeoPixel
		NeoPixel board to set colors on
	locs : Union(slice, list, int)
		Location, slice of locations, or list of locations to set
	color : Tuple
		Tuple of RGB(W) colors to set
	"""
	if isinstance(locs, slice):
		board[locs] = [color] * len(board[locs])
	elif isinstance(locs, list):
		for loc in locs:
			setpixels(board, loc, color)
	else:
		board[locs] = color


def show_image(imgpath, board):
	"""Show an image on the board

	Parameters
	----------
	imgpath : PathLike
		Path to the image to show
	board : NeoPixel
		Neopixel board to show image on
	"""
	image = cv2.imread(imgpath)
	resized = cv2.resize(image, (8,8), interpolation=cv2.INTER_AREA)

	fill_colors = []

	for y in range(0, 8):
		for x in range(0, 8):

			pixel_color = [0, 0, 0, 0]

			for channel in range(0, 3):
				pixel_color[channel] = resized[y][x][channel]

			fill_colors.append(pixel_color)

	for i, color in enumerate(fill_colors):
		setpixels(board, i, color)

	board.show()
	time.sleep(10)
	board.fill(OFF)
