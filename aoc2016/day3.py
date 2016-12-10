"""
Solution for day 3 of AoC 2016.
"""

from aoc2016.triangles import Triangle, TriangleCounter, make_triangles_by_column

def parse(lines):
    """
    >>> parse(["    4   21  894", "  419  794  987", "  424  797  125"])
    [(4, 21, 894), (419, 794, 987), (424, 797, 125)]
    """
    split_lines = [x.split() for x in lines]
    return [(int(x[0]), int(x[1]), int(x[2])) for x in split_lines]

def step1(input):
    ts = [Triangle(*x) for x in input]
    counter = TriangleCounter(ts)
    return len(counter.possibles())

def step2(input):
    ts = make_triangles_by_column(input)
    counter = TriangleCounter(ts)
    return len(counter.possibles())