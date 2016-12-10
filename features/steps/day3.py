from behave import *
from aoc2016.triangles import Triangle, TriangleCounter
import aoc2016.day3 as day3

@given(u'a triangle with sides {s1:d} {s2:d} {s3:d}')
def step_impl(context, s1, s2, s3):
    context.triangle = Triangle(s1, s2, s3)

@when(u'I test if it is possible')
def step_impl(context):
    context.is_possible = context.triangle.is_possible()

@then(u'I should find that it is impossible')
def step_impl(context):
    assert not context.is_possible

@when(u'I change the order of the sides')
def step_impl(context):
    s1 = context.triangle.s1
    s2 = context.triangle.s2
    s3 = context.triangle.s3
    context.triangles = [
        Triangle(s1, s2, s3),
        Triangle(s1, s3, s2),
        Triangle(s2, s1, s3),
        Triangle(s2, s3, s1),
        Triangle(s3, s1, s2),
        Triangle(s3, s2, s1)
        ]

@then(u'I all possibilities should all be impossible or all be possible')
def step_impl(context):
    possibles = [t.is_possible() for t in context.triangles]
    assert all(possibles) or not any(possibles)

@given(u'the triangle input')
def step_impl(context):
    sides = day3.parse(context.text.split('\n'))
    context.triangles = [Triangle(*s) for s in sides]

@when(u'I count the number of possible triangles')
def step_impl(context):
    context.triangle_counter = TriangleCounter(context.triangles)

@then(u'I should get {n:d} possible triangles')
def step_impl(context, n):
    assert len(context.triangle_counter.possibles()) == n
