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
