"""The implementation of the 'when' steps for the user acceptance tests"""

from behave import then, given  # pylint: disable=no-name-in-module


# pylint: disable=missing-function-docstring
# pylint: disable=function-redefined
@then('she should be logged in and redirected to the account page')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:5000/account'
    assert 'Welcome, Test User' in context.browser.page_source


@then('a \'username exists\' error should be displayed')
def step_impl(context):
    assert 'There is already an account associated with this username.' in context.browser.page_source


@then('she should remain on the register page')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:5000/register'


@then('the persona should be saved in her account')
def step_impl(context):
    pass


@then('the persona should be deleted from her account')
def step_impl(context):
    pass


@then('the sound should be audible')
def step_impl(context):
    pass


@then('the sound should be muted')
def step_impl(context):
    pass


@then('the mute icon should be displayed')
def step_impl(context):
    pass


@then('the unmute icon should be displayed')
def step_impl(context):
    pass


@then('the main menu of the UI should be displayed in English')
def step_impl(context):
    pass


@then('the main menu of the UI should be displayed in French')
def step_impl(context):
    pass


@then('the account should be deleted')
def step_impl(context):
    pass


@then('she should be redirected to the login page')
@given('the user navigates to the login page')
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000/login')


@then('she should remain on the login page')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:5000/login'


@then('an "incorrect details" error should be displayed')
def step_impl(context):
    assert 'INCORRECT DETAILS: Please check your details and try again.' in context.browser.page_source
