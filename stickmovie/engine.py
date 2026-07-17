import time

from renderer import clear_screen
from scenes import intro_scene


FPS = 12


def start():
    while True:
        clear_screen()

        frame = intro_scene()

        print(frame)

        time.sleep(1 / FPS)
