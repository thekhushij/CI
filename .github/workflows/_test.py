import pytest

#funtion to test square
def square(n):
    return n**2

# funtion to test cube
def cube(n):
    return n**3
#function to test fithpower
def fithpower(n):
    return n**5

#testting the square function 
def test_square():
    assert square(2) == 4 , "test failed : sqaure of 2 should be 4"
    assert sqaure(3) == 9 , "test failed: square of 3 should be 9"

#testting the cube function 
def test_cube():
    assert cube(2) == 8 , "test failed : sqaure of 2 should be 8"
    assert cube(3) == 27 , "test failed: square of 3 should be 27"

#testting the fithpower function 
def test_fith_power():
    assert fithpower(2) == 32 , "test failed : sqaure of 2 should be 32"
    assert fithpower(3) == 243, "test failed: square of 3 should be 243"

#test for invalid input 
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")

