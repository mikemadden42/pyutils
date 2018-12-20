#!/usr/bin/env python
"""Automote mouse clicks"""

# Kudos to Michael Sexton for the initial script.

# https://codepen.io/nfxpnk/pen/vERyxK
# https://unixpapa.com/js/testmouse.html

import time
from pynput.mouse import Button, Controller


def main():
    """Automote mouse clicks"""
    mouse = Controller()

    print("GET READY!")
    time.sleep(10)

    # Press and release
    while True:
        mouse.press(Button.left)
        mouse.release(Button.left)
        print("click")
        time.sleep(10)


if __name__ == '__main__':
    main()
