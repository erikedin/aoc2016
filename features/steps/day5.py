from behave import *
import aoc2016.securitydoor as securitydoor
import aoc2016.day5 as day5

@given(u'a door with door id "{door_id}"')
def step_impl(context, door_id):
    context.door_breaker = securitydoor.DoorBreaker(door_id)

@given(u'a second door with door id "{door_id}"')
def step_impl(context, door_id):
    context.door_breaker = securitydoor.SecondDoorBreaker(door_id)

@given(u'that a hash must start with five zeroes')
def step_impl(context):
    context.door_breaker.hash_condition = securitydoor.five_zeroes_condition

@given(u'I want to find the {password_char_index:d}th character in the hash')
def step_impl(context, password_char_index):
    context.door_breaker.password_char = securitydoor.PasswordCharIndex(password_char_index)

@given(u'I want the position and char from the {pos_th:d}th and {char_th:d}th positions with a password length of eight')
def step_impl(context, pos_th, char_th):
    context.door_breaker.password_char = securitydoor.SecondPasswordCharIndex(pos_th, char_th, 8)

@given(u'I want a eight-character password')
def step_impl(context):
    context.door_breaker.set_length(8)
    context.password_length = 8

@given(u'I use MD5 as the hash function')
def step_impl(context):
    context.door_breaker.hash_function = securitydoor.MD5()

@then(u'the current index should be {current_index:d}')
def step_impl(context, current_index):
    assert context.door_breaker.current_index == current_index

@when(u'I hash door id and the index')
def step_impl(context):
    context.hash = context.door_breaker.hash()

@then(u'I should get the password character {password_char}')
def step_impl(context, password_char):
    c = context.door_breaker.password_char.get_char(context.hash)
    assert c == password_char, "Expected {}, but got {}".format(password_char, c)

@given(u'that the current hash index is {current_index:d}')
def step_impl(context, current_index):
    context.door_breaker.current_index = current_index

@when(u'I want to find the next valid index')
def step_impl(context):
    context.door_breaker.find_next_valid_index()

@when(u'I find the password for the door')
def step_impl(context):
    context.password = context.door_breaker.find_password()

@then(u'the password should be {password}')
def step_impl(context, password):
    assert context.password == password, "Expected {}, but got {}".format(password, context.password)

@then(u'the password position should be {pos:d}')
def step_impl(context, pos):
    p = context.door_breaker.password_char.get_pos(context.hash)
    assert p == pos, "Expected {}, but got {}".format(pos, p)

@then(u'I should ignore the password character, because it is an invalid position')
def step_impl(context):
    assert context.door_breaker.password_char.get_pos(context.hash) == None

@given(u'a position in the password has been filled')
def step_impl(context):
    context.door_breaker.fill_password(0, 'a')

@when(u'I try to fill the same position')
def step_impl(context):
    context.door_breaker.fill_password(0, 'b')

@then(u'I should keep the existing password character')
def step_impl(context):
    assert context.door_breaker.password[0] == 'a', "Expected a, but got {}".format(context.door_breaker.password[0])
