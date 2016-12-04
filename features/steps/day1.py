from behave import *
from aoc2016.santasagent import SantasAgent, Direction, Turn

@given(u'that I have been airdropped into the city')
def step_impl(context):
    context.me = SantasAgent()

@given(u'that I am at {e:d} blocks E and {n:d} blocks N')
def step_impl(context, e, n):
    context.me.position = (e, n)

@given(u'that I am facing {direction}')
def step_impl(context, direction):
    context.me.facing(Direction.parse(direction))

@when(u'I follow the instructions "{instructions}"')
def step_impl(context, instructions):
    context.me.follow(instructions)

@then(u'I should be at {e:d} blocks E and {n:d} blocks N')
def step_impl(context, e, n):
    assert context.me.east()  == e
    assert context.me.north() == n

@then(u'the distance should be {distance:d}')
def step_impl(context, distance):
    assert context.me.distance() == distance

@when(u'I walk {distance:d} blocks')
def step_impl(context, distance):
    context.me.walk(distance)

@when(u'I turn {turn}')
def step_impl(context, turn):
    context.me.turn(Turn.parse(turn))

@then(u'I should be facing {direction}')
def step_impl(context, direction):
    assert context.me.direction == Direction.parse(direction)

@when(u'I read the instructions "{instructions}"')
def step_impl(context, instructions):
    context.turns_and_distances = context.me.read(instructions)

@then(u'I should get the turns and distances')
def step_impl(context):
    expected = [(Turn.parse(row[0]), int(row[1])) 
                for row in context.table]
    assert context.turns_and_distances == expected

@when(u'I follow the instructions "{instructions}" and stop at the first location I visit twice')
def step_impl(context, instructions):
    context.me.follow_to_first_visit_twice(instructions)

@then(u'I should have visited the locations')
def step_impl(context):
    expected_visits = [(int(row[0]), int(row[1])) for row in context.table]
    assert context.me.visits == expected_visits
