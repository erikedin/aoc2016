from keypad import Keypad

def parse(lines):
    return [x.strip() for x in lines]

def step1(input):
    keypad = Keypad()
    keypad.follow(input)
    return keypad.code