from behave import *

@given(u'that I have been airdropped into the city')
def step_impl(context):
    raise NotImplementedError(u'STEP: background')

@given(u'that I am at {e:d} blocks E and {n:d} blocks N')
def step_impl(context, e, n):
    raise NotImplementedError(u'STEP: that I am at')

@given(u'that I am facing {direction}')
def step_impl(context, direction):
    raise NotImplementedError(u'STEP: that I am facing')

@when(u'I follow the instructions "{instructions}"')
def step_impl(context, instructions):
    raise NotImplementedError(u'STEP: I follow the instructions')

@then(u'I should be at {e:d} blocks E and {n:d} blocks N')
def step_impl(context, e, n):
    raise NotImplementedError(u'STEP: I should be at')

@then(u'the distance should be {distance:d}')
def step_impl(context, distance):
    raise NotImplementedError(u'STEP: the distance should be')

@when(u'I walk {distance:d} blocks')
def step_impl(context, distance):
    raise NotImplementedError(u'STEP: I walk')

@when(u'I turn {turn}')
def step_impl(context, turn):
    raise NotImplementedError(u'STEP: I turn')

@then(u'I should be facing {direction}')
def step_impl(context, direction):
    raise NotImplementedError(u'STEP: I should be facing')
