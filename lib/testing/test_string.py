# test_string_functions.py

from string_functions import return_string, interpolate_string

def test_return_string():
    assert return_string() == "Hello, world!"

def test_interpolate_string():
    assert interpolate_string("Alice") == "Welcome, Alice!"
