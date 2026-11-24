from triangle import classify_triangle, is_valid_triangle


def test_valid_triangle_sides():
    assert is_valid_triangle(3, 4, 5) is True


def test_equilateral_sides_are_valid():
    assert is_valid_triangle(5, 5, 5) is True


def test_degenerate_sides_are_invalid():
    assert is_valid_triangle(2, 3, 5) is False


def test_sides_that_violate_triangle_inequality_are_invalid():
    assert is_valid_triangle(2, 3, 6) is False
    assert is_valid_triangle(0, 3, 4) is False


def test_classifies_impossible_sides_as_invalid():
    message = "Invalid triangle: side lengths do not form a triangle"
    assert classify_triangle(1, 1, 2) == message
    assert classify_triangle(0, 1, 1) == message
    assert classify_triangle(-1, 1, 1) == message
    assert classify_triangle(2, 3, 6) == message


def test_classifies_equilateral_triangle():
    assert classify_triangle(5, 5, 5) == "Equilateral"


def test_classifies_isosceles_triangle():
    assert classify_triangle(5, 5, 3) == "Isosceles"


def test_classifies_scalene_triangle():
    assert classify_triangle(4, 5, 6) == "Scalene"
    assert classify_triangle(3, 4, 5) == "Right Scalene"



if __name__ == "__main__":
    test_valid_triangle_sides()
    test_equilateral_sides_are_valid()
    test_degenerate_sides_are_invalid()
    test_sides_that_violate_triangle_inequality_are_invalid()
    test_classifies_equilateral_triangle()
    test_classifies_isosceles_triangle()
    test_classifies_scalene_triangle()
    print("All tests passed!")
