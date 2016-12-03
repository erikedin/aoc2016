class Turn(object):
    R = 0
    L = 1

    @classmethod
    def parse(clazz, t):
        turns = { 'R': Turn.R, 'L': Turn.L }
        try: return turns[t]
        except KeyError: raise ValueError()

class Direction(object):
    N = ( 0,  1)
    E = ( 1,  0)
    S = ( 0, -1)
    W = (-1,  0)

    @classmethod
    def parse(clazz, direction):
        dirs = { 'N': Direction.N, 'E': Direction.E, 
                 'S': Direction.S, 'W': Direction.W }
        try: return dirs[direction]
        except KeyError: raise ValueError()

class SantasAgent(object):
    def __init__(self):
        self.facing(Direction.N)
        self.position = (0, 0)
    
    def east(self): return self.position[0]
    def north(self): return self.position[1]

    def facing(self, direction):
        self.direction = direction

    def turn(self, towards):
        if towards == Turn.R:
            turns = { Direction.N: Direction.E,
                      Direction.E: Direction.S,
                      Direction.S: Direction.W,
                      Direction.W: Direction.N }
        elif towards == Turn.L:
            turns = { Direction.N: Direction.W,
                      Direction.E: Direction.N,
                      Direction.S: Direction.E,
                      Direction.W: Direction.S }
        else:
            raise ValueError

        self.direction = turns[self.direction]

    def walk(self, distance):
        walked = self.direction[0] * distance, self.direction[1] * distance
        self.position = self.position[0] + walked[0], self.position[1] + walked[1]
    
    def read(self, instructions):
        s = instructions.split(',')
        s = [x.strip() for x in s]
        return [(Turn.parse(x[0]), int(x[1:]))
                for x in s]
    
    def distance(self):
        return abs(self.position[0]) + abs(self.position[1])

    def follow(self, instructions):
        turns_and_distances = self.read(instructions)
        for towards, distance in turns_and_distances:
            self.turn(towards)
            self.walk(distance)