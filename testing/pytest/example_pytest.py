print("hello.")

def setup_module(module):
    print("setting up module")

def teardown_module(module):
    print("tearing down module")

def setup_function(function):
    print("setting up test function")

def teardown_function(self):
    print("tearing down test function")

def test_hello():
    print("\ntesting the words 'hello' and 'goodbye'\n")
    assert "hello" > "goodbye"

def test_add():
    assert 1==2-1