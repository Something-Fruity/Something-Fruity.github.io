"""The implementation of the 'given' steps from the user acceptance tests"""

from behave import given  # pylint: disable=no-name-in-module


# pylint: disable=missing-function-docstring
# pylint: disable=function-redefined
@given('the user is on the main landing page')
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000/')


@given('an account exists for a username')
def step_impl(context):
    pass


@given('a player is logged in')
def step_impl(context):
    pass


@given('the user sound is not muted')
def step_impl(context):
    pass


@given('the user sound is muted')
def step_impl(context):
    pass


@given('the user navigates to the settings page')
def step_impl(context):
    pass


@given('the sound is muted')
def step_impl(context):
    pass


@given('the user navigates to the login page')
def step_impl(context):
    pass


@given('the user logs in')
def step_impl(context):
    pass


@given('a user has deleted her account')
def step_impl(context):
    pass
