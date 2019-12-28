#!/usr/bin/env python3
import sys

def get_coordinates(wire):
    coords = [[0,0]]
    for step in wire:
        step_dir = step[0]
        step_length = int(step[1:])
        new_coord = coords[-1].copy()
        if step_dir == "R":
            new_coord[0] += step_length
        elif step_dir == "L":
            new_coord[0] -= step_length
        elif step_dir == "U":
            new_coord[1] += step_length
        elif step_dir == "D":
            new_coord[1] -= step_length
        coords.append(new_coord)
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
