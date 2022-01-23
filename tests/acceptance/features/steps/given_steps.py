"""The implementation of the 'given' steps from the user acceptance tests"""
from behave import *


# GIVEN
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
