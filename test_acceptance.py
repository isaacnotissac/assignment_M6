import pytest
'''
Check lengths given for a triangle, and classify the triangle type.

If the triangle is invalid do not crash show a mesage 

Check if a triangle is a right angle
'''
def test_is_valid_triangle():
    from triangle import classify_triangle, is_valid_triangle

    assert is_valid_triangle(3, 4, 5) is True
    assert is_valid_triangle(1, 1, 2) is False, "Degenerate triangle sides should be rejected"
    assert is_valid_triangle(0, 1, 1) is False, "Zero-length sides should be rejected"
    assert is_valid_triangle(-1, 1, 1) is False, "Negative side lengths should be rejected"
    assert is_valid_triangle(2, 3, 6) is False, "Sides that violate the triangle inequality should be rejected"

    assert classify_triangle(5, 5, 5) == "Equilateral"
    assert classify_triangle(5, 5, 3) == "Isosceles"
    assert classify_triangle(4, 5, 6) == "Scalene"
    assert classify_triangle(3, 4, 5) == "Right Scalene"