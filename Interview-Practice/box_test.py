import unittest
from box import get_box_coordinates

class GetBoxCoordinatesTest(unittest.TestCase):
    def test_no_box_is_present(self):
        self.assertEqual(get_box_coordinates(image_seven), None)

    def test_box_is_not_on_edge(self):
        self.assertEqual(get_box_coordinates(image_one), { "start": (0 , 0), "end": (0 , 0) })
        self.assertEqual(get_box_coordinates(image_two), { "start": (0 , 0), "end": (6 , 6) })
        self.assertEqual(get_box_coordinates(image_three), { "start": (2 , 3), "end": (3 , 5) })

    def test_box_is_present_and_on_edge(self):
        self.assertEqual(get_box_coordinates(image_four), { "start": (2 , 4), "end": (4 , 5) })
        self.assertEqual(get_box_coordinates(image_five), { "start": (2 , 4), "end": (3 , 6) })
        self.assertEqual(get_box_coordinates(image_six), { "start": (2 , 4), "end": (4 , 6) })

if __name__ == "__main__":
    unittest.main()

image_one = [
    [0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

image_two = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

image_three = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

image_four = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 1]
]

image_five = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1]
]

image_six = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0]
]

image_seven = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]
]