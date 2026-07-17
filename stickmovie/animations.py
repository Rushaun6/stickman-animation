class Animation:
    def __init__(self, character, speed=6):
        self.character = character
        self.speed = speed
        self.frame = 0

    def update(self):
        self.frame += 1

        if self.frame >= self.speed:
            self.frame = 0
            self.character.next_pose()

    def sprite(self):
        return self.character.pose()
