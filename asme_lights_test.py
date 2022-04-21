# ASME Light Board Test

import cv2
import pygame
import math
import time

# WRITTEN FOR PYGAME TEST

left = [(0, 0, 0)] * 64
right = [(0, 0, 0)] * 64

# Setting Parameters and Creating Initial Window
winBase = 800
winHeight = winBase / 2
dx = winHeight // 8
pygame.init()
win = pygame.display.set_mode((winBase, winHeight))
pygame.display.set_caption('ASME Light Board Test')
win.fill((0, 0, 0))

# FROM ASME HELPERS FILE

# Fill board with this value to turn off pixels
# E.g. BOARD_LEFT.fill(OFF)
OFF = (0, 0, 0, 0)


def setpixels(board, string, locs, color):
	"""Sets locations on a board to a given color.

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
			setpixels(board, string, loc, color)
	else:
		board[locs] = color

	for i in range(len(left)):
		if string == 'left':
			pygame.draw.circle(win, board[i],
			                   (dx * (i % 8) + (dx / 2),
			                    dx * math.ceil((i + 1) / 8 - 1) + (dx / 2)),
			                   dx // 4)
		elif string == 'right':
			pygame.draw.circle(win, board[i],
			                   (dx * (i % 8) + (dx / 2) + (winBase / 2),
			                    dx * math.ceil((i + 1) / 8 - 1) + (dx / 2)),
			                   dx // 4)

	pygame.display.update()


def show_image(imgpath, board, string):
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

	for i in range(len(left)):
		if string == 'left':
			pygame.draw.circle(win, board[i],
			                   (dx * (i % 8) + (dx / 2),
			                    dx * math.ceil((i + 1) / 8 - 1) + (dx / 2)),
			                   dx // 4)
		elif string == 'right':
			pygame.draw.circle(win, board[i],
			                   (dx * (i % 8) + (dx / 2) + (winBase / 2),
			                    dx * math.ceil((i + 1) / 8 - 1) + (dx / 2)),
			                   dx // 4)

	pygame.display.update()


# WRITTEN FOR PYGAME TEST

# Running
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	""" Enter Code at this level for assigning pixel colors
    
    """
	cuGold = (255, 206, 0, 0)
	cuGreen = (0, 220, 10, 0)
	backgroundColor = (0, 0, 0, 0)
	i = 1
	while i < 5:
		# Letter C
		setpixels(left, 'left', slice(0, 63), backgroundColor)
		setpixels(right, 'right', slice(0, 63), backgroundColor)
		setpixels(left, 'left',
		          [10, 11, 12, 13, 18, 26, 34, 42,
		           slice(50, 54)], cuGold)

		# Letter U
		setpixels(right, 'right',
		          [10, 13, 18, 21, 26, 29, 34, 37, 42, 45, 50,
		           slice(51, 54)], cuGreen)
		time.sleep(2)

		# Letter A
		setpixels(left, 'left', slice(0, 63), backgroundColor)
		setpixels(right, 'right', slice(0, 63), backgroundColor)
		setpixels(
		    left, 'left',
		    [slice(10, 14), 18, 21,
		     slice(26, 30), 34, 37, 42, 45, 50, 53], cuGreen)

		# Letter S
		setpixels(right, 'right',
		          [slice(10, 14), 18,
		           slice(26, 29), 37, 45,
		           slice(50, 54)], cuGold)
		time.sleep(2)

		# Letter M
		setpixels(left, 'left', slice(0, 63), backgroundColor)
		setpixels(right, 'right', slice(0, 63), backgroundColor)
		setpixels(left, 'left', [
		    9, 10, 13, 14,
		    slice(17, 23), 25, 27, 28, 30, 33, 38, 41, 46, 49, 54
		], cuGold)

		# Letter E
		setpixels(right, 'right',
		          [slice(10, 14), 18,
		           slice(26, 30), 34, 42,
		           slice(50, 54)], cuGreen)
		time.sleep(2)
		i += 1

	# Ex Code
	# DELETE AND REPLACE
	setpixels(left, 'left', [0, 3, 8, slice(12, 18)], (0, 255, 0))
	time.sleep(2)
	setpixels(right, 'right', [0, 4, 7, 45, 60, 61, 62], (0, 0, 255))

pygame.quit()
