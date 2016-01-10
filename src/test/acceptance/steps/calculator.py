from behave import *
from nose.tools import *


@given('The calculator is instantiated')
def step_impl(context):
    from app.logic.calculator import Calculator
    context.calculator = Calculator()

@when('The calculator add 10 with 20')
def step_impl(context):
    context.result = context.calculator.add(10, 20)

@then('The result is 30')
def step_impl(context):
    eq_(30, context.result)
