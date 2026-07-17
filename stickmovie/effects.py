import random


class Effect:
    def __init__(self, frames, speed=4, loop=False):
        self.frames = frames
        self.speed = speed
        self.loop = loop

        self.frame = 0
        self.timer = 0
        self.finished = False

    def update(self):
        if self.finished:
            return

        self.timer += 1

        if self.timer >= self.speed:
            self.timer = 0
            self.frame += 1

            if self.frame >= len(self.frames):
                if self.loop:
                    self.frame = 0
                else:
                    self.frame = len(self.frames) - 1
                    self.finished = True

    def draw(self):
        return self.frames[self.frame]


def random_rain(width=60):
    return "".join(random.choice(["|", "/", "\\", " "]) for _ in range(width))


EXPLOSION = Effect(
    [
        "   .   ",
        "  ***  ",
        " ***** ",
        "*******",
        " ***** ",
        "  ***  ",
        "   .   ",
    ],
    speed=2,
)

SMOKE = Effect(
    [
        " . ",
        " .. ",
        " ... ",
        "  .. ",
        " . ",
        "   ",
    ],
    speed=3,
    loop=True,
      )
