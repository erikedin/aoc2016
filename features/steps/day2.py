from behave import *
from aoc2016.keypad import Keypad
import aoc2016.day2 as day2

@given(u'I am at a keypad')
def step_impl(context):
    context.keypad = Keypad()

@given(u'I start at key {key:d}')
def step_impl(context, key):
    context.keypad.key = key

@when(u'I follow the keypad instructions')
def step_impl(context):
    parsed_instructions = day2.parse(context.text.split())
    context.keypad.follow(parsed_instructions)

@then(u'I should get the bathroom code {code:d}')
def step_impl(context, code):
    assert context.keypad.code == code, "Expected {}, got {}".format(code, context.keypad.code)

@then(u'I should be at {key:d}')
def step_impl(context, key):
    assert context.keypad.key == key

@when(u'I move according to instruction {instruction}')
def step_impl(context, instruction):
    context.keypad.move(instruction)

