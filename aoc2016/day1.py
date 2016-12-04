"""
Solution for day 1 of AoC 2016.
"""

from santasagent import SantasAgent

def parse(lines):
    return lines[0]

def step1(instructions):
    agent = SantasAgent()
    agent.follow(instructions)
    return agent.distance()