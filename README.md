# Triangle Classifier

## Project Overview

This project implements a triangle classifier in Python. It takes three side lengths as input, determines whether they form a valid triangle, and classifies valid triangles based on their side lengths. It also identifies right triangles using the Pythagorean theorem.

The project includes:
- A triangle classification implementation (`triangle.py`).
- Unit tests (`test_triangle.py`).
- An end-to-end customer acceptance test (`test_acceptance.py`).
- A requirements file (`requirements.txt`).

## Project Structure

    triangle-classifier/
    │
    ├── triangle.py
    ├── test_triangle.py
    ├── test_acceptance.py
    ├── requirements.txt
    └── README.md

## How to Run the Project

### 1. Requirements

- Python 3.8 or higher
- pytest

### 2. Install Dependencies

Run the following command:

    pip install -r requirements.txt

### 3. Run the Tests

To run all unit and acceptance tests:

    pytest -v

## Triangle Classification Rules

The classifier uses the following rules:

| Condition | Expected Result |
|---|---|
| Any side is less than or equal to zero | Invalid |
| Triangle inequality is not satisfied | Invalid |
| All three sides are equal | Equilateral |
| Exactly two sides are equal | Isosceles |
| All three sides are different | Scalene |
| Triangle satisfies the Pythagorean theorem | Prefix classification with "Right" |

The triangle inequality requires that the sum of any two sides must be strictly greater than the third side.

For right triangles, a floating-point tolerance is used instead of exact equality (`==`) to account for decimal values.

### Why an Equilateral Triangle Can Never Be Right

An equilateral triangle has three equal sides and three equal angles. Each angle must measure 60 degrees. A right triangle must have one angle measuring 90 degrees. Therefore, an equilateral triangle can never be a right triangle.

## Part 1 – Implementation

The `triangle.py` file contains two functions:

- `is_valid_triangle(a, b, c) -> bool`: Checks whether three side lengths form a valid triangle.
- `classify_triangle(a, b, c) -> str`: Returns the appropriate triangle classification.

Possible classifications include:
- `Invalid`
- `Equilateral`
- `Isosceles`
- `Scalene`
- `Right Scalene`
- `Right Isosceles`

## Part 2 – Unit Tests

Unit tests are written in `test_triangle.py` using pytest.

The tests cover the following equivalence classes and boundary conditions:

| Test Category | Example Input | Expected Result |
|---|---|---|
| Invalid negative side | (-1, 2, 2) | Invalid |
| Invalid zero side | (0, 3, 3) | Invalid |
| Triangle inequality failure | (1, 2, 3) | Invalid |
| Equilateral | (5, 5, 5) | Equilateral |
| Isosceles | (5, 5, 3) | Isosceles |
| Scalene | (4, 5, 6) | Scalene |
| Right Scalene | (3, 4, 5) | Right Scalene |
| Right triangle with non-integer sides | (5, 5, 5√2) | Right Isosceles |

The tests also verify that degenerate triangles, where the sum of two sides equals the third side, are rejected.

### Copilot Review Log

GitHub Copilot was used to draft unit tests. Each suggestion was reviewed against the project requirements before being accepted, edited, or rejected.

| Test | Copilot Suggested? | Kept / Edited / Rejected | Why |
|---|---|---|---|
| test_right_triangle | Yes | Edited | Copilot asserted with `==`; changed to `math.isclose` to correctly handle floating-point tolerance. |

The review process focused on whether the suggested tests matched the assignment specifications, rather than simply matching the current implementation.

## Part 3 – Customer Acceptance Test

The acceptance test is located in `test_acceptance.py`.

### Customer Requirements

The customer operates a stained-glass studio. Customers enter three side lengths and need to know the shape of the piece and whether it is buildable.

The customer also needs right-angle pieces identified because they require reinforced corners.

### Testable Acceptance Criteria

1. **Triangle validity:** When customers enter three side lengths that do not form a valid triangle, the system must return `Invalid` without crashing.

2. **Shape classification:** When customers enter valid side lengths, the system must return the correct classification: Equilateral, Isosceles, or Scalene.

3. **Right-angle identification:** When customers enter side lengths that satisfy the Pythagorean theorem within the defined floating-point tolerance, the classification must include the `Right` prefix so the studio can identify pieces requiring reinforced corners.

### Acceptance Test

The `test_acceptance.py` file tests the customer requirements end-to-end by calling `classify_triangle()` and checking the returned classifications.

This test verifies that invalid pieces are identified, valid pieces receive the correct shape classification, and right-angle pieces are flagged appropriately.

**Note:** Acceptance testing is based on the customer's requirements and is written independently of GitHub Copilot.

## Part 4 – GitHub Repository Submission

The project is submitted as a public GitHub repository containing all five required files:

- `triangle.py`
- `test_triangle.py`
- `test_acceptance.py`
- `requirements.txt`
- `README.md`

The repository should contain at least three meaningful commits documenting the development process.

Suggested commit messages:

    1. Implement triangle validation and classification
    2. Add unit tests and review Copilot suggestions
    3. Add customer acceptance test and project documentation

## AI Use Disclosure

**Tool Used:** GitHub Copilot

**Purpose:** GitHub Copilot was used to help draft unit tests for Part 2.

**Verification:** Every Copilot suggestion was reviewed against the assignment requirements. Suggestions were accepted, edited, or rejected based on correctness. Particular attention was given to floating-point comparisons when identifying right triangles.

**Part 3:** No AI tool was used to write the customer acceptance test. The acceptance criteria and test were developed independently based on the customer's requirements.