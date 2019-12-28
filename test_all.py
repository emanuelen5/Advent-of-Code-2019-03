from main import check, get_intersection, get_intersections_and_indices, get_coordinates, get_move_type, get_wire_distances, get_coordinate_distance
from main import MOVE_HORIZONTAL, MOVE_DIAGONAL, MOVE_VERTICAL
import unittest

class TestCoordinates(unittest.TestCase):
    def check_from_input(self, actual, wire_str):
        self.assertEqual(actual, get_coordinates(wire_str.split(",")))

    def test_direction(self):
        self.check_from_input([[0,0], [1,0]], "R1")
        self.check_from_input([[0,0], [-1,0]], "L1")
        self.check_from_input([[0,0], [0,1]], "U1")
        self.check_from_input([[0,0], [0,-1]], "D1")

    def test_several(self):
        self.check_from_input([[0,0], [1,0], [1,1], [0,1], [0,0]], "R1,U1,L1,D1")

class TestWireDistance(unittest.TestCase):
    def check_from_input(self, actual, wire_str):
        self.assertEqual(actual, get_wire_distances(wire_str.split(",")))

    def test_simple(self):
        self.check_from_input([0, 1, 2, 3, 4], "R1,U1,L1,D1")

class TestCoordinateDistance(unittest.TestCase):
    def test_simple(self):
        pass

class TestMoveType(unittest.TestCase):
    def test_horizontal(self):
        self.assertEqual(MOVE_HORIZONTAL, get_move_type([0,0], [1,0]))
        self.assertEqual(MOVE_VERTICAL, get_move_type([0,0], [0,1]))
        self.assertEqual(MOVE_DIAGONAL, get_move_type([0,0], [1,1]))
        self.assertEqual(None, get_move_type([0,0], [0,0]))

class TestIntersection(unittest.TestCase):
    def test_single(self):
        self.assertEqual([1,1], get_intersection([0,1], [2,1], [1,0], [1,2]))
        self.assertEqual([1,1], get_intersection([1,0], [1,2], [0,1], [2,1]))

    def test_none(self):
        self.assertEqual(None, get_intersection([0,1], [2,1], [5,0], [5,2]))
        self.assertEqual(None, get_intersection([1,0], [1,2], [0,5], [2,5]))

class TestIntersectionsAndIndices(unittest.TestCase):
    def test_single_horizontal(self):
        self.assertEqual([[[1,1], [0,0]]], get_intersections_and_indices([[0,1], [2,1]], [[1,0], [1,2]]))

    def test_single_vertical(self):
        self.assertEqual([[[1,1], [0,0]]], get_intersections_and_indices([[1,0], [1,2]], [[0,1], [2,1]]))

    def test_several(self):
        self.assertEqual([[[1,1], [0,0]], [[2,2], [1,1]]], get_intersections_and_indices([[1,0], [1,2], [3,2]], [[0,1], [2,1], [2,3]]))

class TestAOC(unittest.TestCase):
    def check_from_input(self, actual, wire1_str, wire2_str):
        wire1 = wire1_str.split(",")
        wire2 = wire2_str.split(",")
        self.assertEqual(actual, check(wire1, wire2))

    def test_examples(self):
        self.check_from_input(30, "R8,U5,L5,D3", "U7,R6,D4,L4")
        self.check_from_input(610, "R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83")
        self.check_from_input(410, "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")

if __name__ == '__main__':
    unittest.main()
