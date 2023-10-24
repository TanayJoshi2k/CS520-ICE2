import unittest
from isTriangle import Triangle

class TestTriangleClass(unittest.TestCase):

    def test_scalene_triangle(self):
        result = Triangle.classify(3, 4, 5)
        self.assertEqual(result, Triangle.Type.SCALENE)

        result = Triangle.classify(10, 15, 20)
        self.assertEqual(result, Triangle.Type.SCALENE)

        result = Triangle.classify(1.5, 2.5, 3.5)
        self.assertEqual(result, Triangle.Type.SCALENE)

    def test_equilateral_triangle(self):
        result = Triangle.classify(2, 2, 2)
        self.assertEqual(result, Triangle.Type.EQUILATERAL)

        result = Triangle.classify(10, 10, 10)
        self.assertEqual(result, Triangle.Type.EQUILATERAL)

        result = Triangle.classify(20, 20, 20)
        self.assertEqual(result, Triangle.Type.EQUILATERAL)

    def test_isosceles_triangle(self):
        result = Triangle.classify(2, 3, 2)
        self.assertEqual(result, Triangle.Type.ISOSCELES)

        result = Triangle.classify(100, 100, 150)
        self.assertEqual(result, Triangle.Type.ISOSCELES)

        result = Triangle.classify(4, 4, 3)
        self.assertEqual(result, Triangle.Type.ISOSCELES)

    def test_invalid_triangle_with_neg_side(self):
        result = Triangle.classify(2, -1, 3)
        self.assertEqual(result, Triangle.Type.INVALID)

        result = Triangle.classify(-5, 10, 30)
        self.assertEqual(result, Triangle.Type.INVALID)

        result = Triangle.classify(-2, -1, -3)
        self.assertEqual(result, Triangle.Type.INVALID)

    def test_invalid_triangle_with_sum_of_two_sides_less_than_third(self):
        result = Triangle.classify(1, 2, 4)
        self.assertEqual(result, Triangle.Type.INVALID)

        result = Triangle.classify(5, 6, 20)
        self.assertEqual(result, Triangle.Type.INVALID)

        result = Triangle.classify(9, 10, 20)
        self.assertEqual(result, Triangle.Type.INVALID)

    def test_invalid_triangle_with_sum_of_two_sides_equal_to_third(self):
        result = Triangle.classify(1, 2, 3)
        self.assertEqual(result, Triangle.Type.INVALID)

        result = Triangle.classify(5, 5, 10)
        self.assertEqual(result, Triangle.Type.INVALID)

        result = Triangle.classify(10, 10, 20)
        self.assertEqual(result, Triangle.Type.INVALID)

if __name__ == '__main__':
    unittest.main()