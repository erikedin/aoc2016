import aoc2016.securitydoor as sd 

def parse(lines): return lines[0]

def step1(input):
    door_breaker = sd.DoorBreaker(input)
    door_breaker.password_char = sd.PasswordCharIndex(6)
    door_breaker.hash_condition = sd.five_zeroes_condition
    door_breaker.hash_function = sd.MD5()
    door_breaker.length = 8

    return door_breaker.find_password() 

def step2(input):
    door_breaker = sd.SecondDoorBreaker(input)
    door_breaker.password_char = sd.SecondPasswordCharIndex(6, 7, 8)
    door_breaker.hash_condition = sd.five_zeroes_condition
    door_breaker.hash_function = sd.MD5()
    door_breaker.set_length(8)

    return door_breaker.find_password()     