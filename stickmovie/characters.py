class Character:
    def __init__(self, name, poses):
        self.name = name
        self.poses = poses
        self.current_pose = 0

    def pose(self):
        return self.poses[self.current_pose]

    def next_pose(self):
        self.current_pose += 1

        if self.current_pose >= len(self.poses):
            self.current_pose = 0


HERO = Character(
    "hero",
    [
        r"""
  o
 /|\
 / \
""",
        r"""
 \o
  |\
 / \
""",
        r"""
  o/
 /|
 / \
""",
        r"""
 \o/
  |
 / \
"""
    ]
)
