#!/usr/bin/env python3
import sys

def get_coordinates(wire):
    coords = [[0,0]]
    return coords

def get_intersections(coords1, coords2):
    intersections = [[0,0], [1,1]]
    return intersections

def check(wire1, wire2):
    coords1 = get_coordinates(wire1)
    coords2 = get_coordinates(wire2)
    intersections = get_intersections(coords1, coords2)
    distances = [sum(i) for i in intersections]
    return min(intersections)

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("puzzle_input_file")
    ns = parser.parse_args()

    with open(ns.puzzle_input_file) as f:
        wires = f.readlines()
        assert len(wires) == 2, "There should be exactly two lines of input"
        wire1 = wires[0].split(",")
        wire2 = wires[1].split(",")

    distance = check(wire1, wire2)
    print(f"Distance to closest intersection: {distance}")

if __name__=="__main__":
    main()
