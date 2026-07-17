class Dialogue:
    def __init__(self):
        self.speaker = ""
        self.text = ""

    def set(self, speaker, text):
        self.speaker = speaker
        self.text = text

    def clear(self):
        self.speaker = ""
        self.text = ""

    def draw(self):
        if not self.text:
            return ""

        width = max(len(f"{self.speaker}: {self.text}") + 2, 30)

        top = "+" + "-" * width + "+"
        middle = f"| {self.speaker}: {self.text}"
        middle += " " * (width - len(middle) + 1) + "|"
        bottom = "+" + "-" * width + "+"

        return "\n".join([top, middle, bottom])


dialogue = Dialogue()
