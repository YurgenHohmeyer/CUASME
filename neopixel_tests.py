import os
import cv2
import time
from neopixel_utils import setpixels, OFF


def simple_test(boards: list):
	"""Simple test shows R G B

	Parameters
	----------
	boards : list
		List of boards to run the test on
	"""
	for board in boards:
		board.fill((255, 0, 0, 0))
		board.show()
	time.sleep(2)

	for board in boards:
		board.fill((0, 255, 0, 0))
		board.show()
	time.sleep(2)

	for board in boards:
		board.fill((0, 0, 255, 0))
		board.show()
	time.sleep(2)

	for board in boards:
		board.fill((0, 0, 0, 0))
		board.show()


def letter_test(board1, board2):
	"""CU AS ME letter test

	Parameters
	----------
	board1 : NeoPixel
		First neopixel board
	board2 : NeoPixel
		Second neopixel board
	"""
	cuGold = (255, 206, 0, 0)
	cuGreen = (0, 220, 10, 0)
	backgroundColor = (0, 0, 0, 0)
	i = 1
	while i < 5:
		# Letter C
		board1.fill(backgroundColor)
		setpixels(board1, [10, 11, 12, 13, 18, 26, 34, 42,
		                   slice(50, 54)], cuGold)

		# Letter U
		board2.fill(backgroundColor)
		setpixels(board2,
		          [10, 13, 18, 21, 26, 29, 34, 37, 42, 45, 50,
		           slice(51, 54)], cuGreen)
		board1.show()
		board2.show()
		time.sleep(2)

		# Letter A
		board1.fill(backgroundColor)
		setpixels(
		    board1,
		    [slice(10, 14), 18, 21,
		     slice(26, 30), 34, 37, 42, 45, 50, 53], cuGreen)

		# Letter S
		board2.fill(backgroundColor)
		setpixels(board2,
		          [slice(10, 14), 18,
		           slice(26, 29), 37, 45,
		           slice(50, 54)], cuGold)
		board1.show()
		board2.show()
		time.sleep(2)

		# Letter M
		board1.fill(backgroundColor)
		setpixels(board1, [
		    9, 10, 13, 14,
		    slice(17, 23), 25, 27, 28, 30, 33, 38, 41, 46, 49, 54
		], cuGold)

		# Letter E
		board2.fill(backgroundColor)
		setpixels(board2,
		          [slice(10, 14), 18,
		           slice(26, 30), 34, 42,
		           slice(50, 54)], cuGreen)
		board1.show()
		board2.show()
		time.sleep(2)
		i += 1

	board1.fill(OFF)
	board2.fill(OFF)
	board1.show()
	board2.show()


def image_test(board1, board2):
	"""Run a Pong-style "Animation" on the lightboards

	Parameters
	----------
	board1 : NeoPixel
		First board
	board2 : NeoPixel
		Second board
	"""
	for img in sorted(os.scandir('pong_imgs'), key=lambda e: e.name):

		if img.is_dir():
			continue

		if not img.name.lower().endswith('.png'):
			continue
		print(img.name)
		for side in ['left', 'right']:
			image = cv2.imread(os.path.join('pong_imgs', side, img.name))

			fill_colors = []

			for y in range(0, 8):
				for x in range(0, 8):

					pixel_color = [0, 0, 0, 0]

					for channel in range(0, 3):
						pixel_color[channel] = image[y][x][channel]

					fill_colors.append(pixel_color)

			for i, color in enumerate(fill_colors):
				board = board1
				if side == 'right':
					board = board2

				setpixels(board, i, color)

		board1.show()
		board2.show()

		time.sleep(1)
