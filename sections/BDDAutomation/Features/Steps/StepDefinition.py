from behave import *

@given(u'User id on Registration page')
def step_impl(context):
    context.driver.get("https://www.thetestingworld.com/testings")
    

@when(u'User enters username')
def step_impl(context):
    context.driver.find_element_by_name('fld_username').send_keys('abcd')


@when(u'User enters email id')
def step_impl(context):
    context.driver.find_element_by_name('fld_email').send_keys('aabcd@gmail.com')


@when(u'User enters password')
def step_impl(context):
    context.driver.find_element_by_name('fld_password').send_keys('aabcd@gmail.com')


@when(u'User click on singnup button')
def step_impl(context):
    context.driver.find_element_by_xpath('//input[@type="submit" and @value="Sign up"]').click()


@then(u'User should be registered successfully')
def step_impl(context):
    print('Registered')

@when(u'User enters duplicate username')
def step_impl(context):
    print('Not Registered')