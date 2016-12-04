from behave import *

@given(u'I have solved both puzzles for day 1')
def step_impl(context):
    import aoc2016.day1 as day1
    day1.step1 = lambda _input: 17
    day1.step2 = lambda _input: 42

@when(u'I execute the script for day 1')
def step_impl(context):
    import aoc2016
    aoc2016.main("day1")

@then(u'I get the results for both puzzles')
def step_impl(context):
    output = context.stdout_capture.getvalue()
    assert "Step 1" in output
    assert "17" in output
    assert "Step 2" in output
    assert "42" in output

@given(u'I have solved only puzzle 1 for day 1')
def step_impl(context):
    import aoc2016.day1 as day1
    day1.step1 = lambda _input: 17
    del day1.step2

@then(u'I get only the result for puzzle 1')
def step_impl(context):
    output = context.stdout_capture.getvalue()    
    assert "Step 1" in output
    assert "17" in output
    assert not "Step 2" in output

@given(u'I want to solve the puzzle for day 1')
def step_impl(context):
    pass

@when(u'I look for the module "day1"')
def step_impl(context):
    import aoc2016.day1 as day1
    context.day_module = day1

@then(u'I can parse the input by sending in a list of lines')
def step_impl(context):
    context.day_module.parse(["R2, L50", ""])
