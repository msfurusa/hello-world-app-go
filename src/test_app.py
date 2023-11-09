# Import the function you want to test from the app module
from app import hello_world

# A simple test function
def test_hello_world():
    # Call the function and check the expected result
    result = hello_world()
    assert result == "Hello, World!"

# Additional tests can be added here
