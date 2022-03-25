import time
import board
import neopixel

pixel_pin = board.D18

ORDER = neopixel.GRBW

pixels1 = neopixel.NeoPixel(pixel_pin, 64, brightness=0.2, auto_write=True, pixel_order=ORDER)
pixels2 = neopixel.NeoPixel(board.D21, 64, brightness=0.2, auto_write=True, pixel_order=ORDER)

pixels1.fill((255,0,0,0))
pixels2.fill((0,255,0,0))
time.sleep(2)

pixels1.fill((0,255,0,0))
pixels2.fill((0,0,255,0))
time.sleep(2)

pixels1.fill((0,0,255,0))
pixels2.fill((255,0,0,0))
time.sleep(2)


pixels1.fill((0,0,0,0))
pixels2.fill((0,0,0,0))
