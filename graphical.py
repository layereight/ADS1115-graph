#!/usr/bin/env python3
#
#
# typical run:
#
# sudo ./graphical.py 1024 768
#

import sys
import time
import pygame
import Adafruit_ADS1x15


GAIN = 1
MAX = 26450

if __name__ == '__main__':

    screen_width = int(sys.argv[1])
    screen_height = int(sys.argv[2])

    margin_x = screen_width * 0.1
    margin_y = screen_height * 0.1

    bar_width = screen_width - 2 * margin_x
    bar_height = screen_height - 2 * margin_y

    RATIO = bar_width / MAX

    screen = pygame.display.set_mode((screen_width, screen_height))

    # Create an ADS1115 ADC (16-bit) instance.
    adc = Adafruit_ADS1x15.ADS1115()

    try:
        while True:

            value = adc.read_adc(0, gain=GAIN)

            width = RATIO * value

            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (0, 250, 0), (margin_x, margin_y, bar_width, bar_height), 5)
            pygame.draw.rect(screen, (0, 250, 0), (margin_x, margin_y, width, bar_height), 0)

            pygame.display.flip()

            # ~60Hz
            time.sleep(0.017)
    finally:
        pygame.quit()
