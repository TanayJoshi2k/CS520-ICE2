import unittest
from isTriangle import Triangle

class TestTriangleClass(unittest.TestCase):

    def test_scalene_triangle(self):
        
        self.assertEqual(Triangle.classify(3, 4, 5), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(10, 15, 20), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(15, 25, 35), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(10, 11, 15), Triangle.Type.SCALENE)

    def test_equilateral_triangle(self):
        
        self.assertEqual(Triangle.classify(2, 2, 2), Triangle.Type.EQUILATERAL)
        self.assertEqual(Triangle.classify(100, 100, 100), Triangle.Type.EQUILATERAL)
        
    def test_isosceles_triangle(self):
        self.assertEqual(Triangle.classify(2, 3, 2), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(10, 10, 15), Triangle.Type.ISOSCELES)
        
    def test_invalid_triangle(self):
        self.assertEqual(Triangle.classify(2, -1, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-2, -1, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(0, 1, 2), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 0, -1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(10, 10, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(0, 0, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(0, 1, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-1, 0, -1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 0, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 2, 4), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-1, -1, 2), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(0, 0, -1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 2, 5), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-2, -1, -3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 2, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(0, 0, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 1, 2), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 1, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 2, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(20, 50, 30), Triangle.Type.INVALID)
        
if __name__ == '__main__':
    unittest.main()