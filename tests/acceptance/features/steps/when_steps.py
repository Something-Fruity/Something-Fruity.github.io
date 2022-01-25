"""The implementation of the 'when' steps for the user acceptance tests"""

from behave import when, given  # pylint: disable=no-name-in-module


# pylint: disable=missing-function-docstring
# pylint: disable=function-redefined
@when('the user clicks register in the menu')
def step_impl(context):
    context.browser.find_element_by_link_text('Register').click()


@when('the player navigates to the persona page')
def step_impl(context):
    pass


@when('she clicks the create persona button')
def step_impl(context):
    pass


@when('she enters a persona name and image and clicks save')
def step_impl(context):
    pass


@when('she clicks the delete button next to an existing persona')
def step_impl(context):
    pass


@when("she clicks the mute/unmute icon")
def step_impl(context):
    pass


@when("she clicks the language setting")
def step_impl(context):
    pass


@when("she chooses English from the menu")
def step_impl(context):
    pass


@when("she chooses French from the menu")
def step_impl(context):
    pass


@when('she enters her details and clicks the \'Register\' button')
def step_impl(context):
    username = context.browser.find_element_by_id('username')
    password = context.browser.find_element_by_id('pass')
    confirm_password = context.browser.find_element_by_id('confirm-pass')
    f_name = context.browser.find_element_by_id('f_name')
    surname = context.browser.find_element_by_id('surname')
    email = context.browser.find_element_by_id('email')
    register_button = context.browser.find_element_by_id('submit')

    username.send_keys('Test User')
    password.send_keys('123456')
    confirm_password.send_keys('123456')
    f_name.send_keys('name')
    surname.send_keys('surname')
    email.send_keys('email@email.com')
    register_button.click()


@when('the user clicks delete')
def step_impl(context):
    context.browser.find_element_by_id('delete').click()
    pass


@given('the user enters her details')
@when('the user enters her details')
def step_impl(context):
    username = context.browser.find_element_by_id('username')
    password = context.browser.find_element_by_id('password')
    username.send_keys('Test User')
    password.send_keys('123456')


@when('the user enters an incorrect password details')
def step_impl(context):
    username = context.browser.find_element_by_id('username')
    password = context.browser.find_element_by_id('password')
    username.send_keys('Test User')
    password.send_keys('wrong password')


@given('she clicks login')
@when('she clicks login')
def step_impl(context):
    login_button = context.browser.find_element_by_id('submit')
    login_button.click()
