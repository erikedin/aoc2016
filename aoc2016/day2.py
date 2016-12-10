from keypad import Keypad

def parse(lines):
    return [x.strip() for x in lines]

def step1(input):
    keypad_look = """  1  \n 234 \n56789\n ABC \n  D  """
    keys = Keypad.parse_keys(keypad_look)
    keypad = Keypad(keys)
    keypad.follow(input)
    return keypad.code