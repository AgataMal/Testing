from behave import *

@given("Is Saturday")
def is_saturday(context):
    pass

@when("Is afternoon")
def is_afternoon(context):
    assert True is not False


@then("Have a drink")
def drink(context):
    assert context.failed is False