
movements = {
    1: {'U': 1, 'D': 4, 'L': 1, 'R': 2},
    2: {'U': 2, 'D': 5, 'L': 1, 'R': 3},
    3: {'U': 3, 'D': 6, 'L': 2, 'R': 3},
    4: {'U': 1, 'D': 7, 'L': 4, 'R': 5},
    5: {'U': 2, 'D': 8, 'L': 4, 'R': 6},
    6: {'U': 3, 'D': 9, 'L': 5, 'R': 6},
    7: {'U': 4, 'D': 7, 'L': 7, 'R': 8},
    8: {'U': 5, 'D': 8, 'L': 7, 'R': 9},
    9: {'U': 6, 'D': 9, 'L': 8, 'R': 9},
}

class Keypad(object):
    def __init__(self):
        self.key = 5
        self.code = 0
    
    def move(self, instruction):
        from_here = movements[self.key]
        self.key  = from_here[instruction]
    
    def follow(self, lines_of_instructions):
        for instructions in lines_of_instructions:
            for i in instructions:
                self.move(i)
            self.code = self.code * 10 + self.key
        