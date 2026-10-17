# assuming a, b, and c are side lengths

def is_valid_triangle(a, b ,c):
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

def classify_triangle(a, b, c):
    if (a == b and b == c):
        return "Equilateral"
    elif (a == b or a == c or b == c):
        return "Isosceles"
    else:
        sides = sorted((a, b, c))
        if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
            return "Right Scalene"
        return "Scalene"