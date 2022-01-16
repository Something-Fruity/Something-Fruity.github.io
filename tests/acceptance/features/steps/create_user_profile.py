from behave import *


# GIVEN
@given('the user navigates to the main landing page')
def step_impl(context):
	context.browser.get('http://127.0.0.1:5000/')


@given('an account exists for a username')
def step_impl(context):
	pass


# WHEN
@when('the user clicks register in the menu')
def step_impl(context):
	context.browser.find_element_by_link_text('Register').click()


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


# THEN
@then('she will be logged in and redirected to the account page')
def step_impl(context):
	assert context.browser.current_url == 'http://127.0.0.1:5000/account'
	assert 'Welcome, Test User' in context.browser.page_source


@then('a \'username exists\' error will be displayed')
def step_impl(context):
	assert 'There is already an account associated with this username.' in context.browser.page_source


@then('she will remain on the register page')
def step_impl(context):
	assert context.browser.current_url == 'http://127.0.0.1:5000/register'


