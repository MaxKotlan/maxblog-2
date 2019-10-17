from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

@given(u'we have a browser looking at "{url}"')
def step_impl(context, url):
    context.browser = webdriver.Chrome()
    context.browser.get(url)

@given(u'the browser title contains "{title}"')
def step_impl(context, title):
    assert title in context.browser.title

@when(u'we search for "{target}"')
def step_impl(context, target):
    search_box = context.browser.find_element_by_name("q")
    search_box.clear()
    search_box.send_keys(target)
    search_box.send_keys(Keys.RETURN)

@when(u'we search using "{name}" for "{target}"')
def step_impl(context, target, name):
    search_box = context.browser.find_element_by_name(name)
    search_box.clear()
    search_box.send_keys(target)
    search_box.send_keys(Keys.RETURN)

@then(u'we get a "{s}" message')
def step_impl(context, s):
    assert s in context.browser.page_source        
    
@then(u'we don\'t get a "{s}" message')
def step_impl(context):
    assert s not in context.browser.page_source        
