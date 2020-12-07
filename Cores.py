class Cores(object):
    def __init__(self, text):
        self.text = text

    def red(self):
        print(f"\033[31m{self.text}\033[0m")
