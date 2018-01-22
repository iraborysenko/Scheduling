class ESecond:
    def __init__(self, title, deadline, length, start):
        self.title = title
        self.deadline = deadline
        self.length = length
        self.start = start

    def __repr__(self):
        return repr((self.title, self.deadline, self.length, self.start))