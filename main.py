#!/usr/bin/env python3
import sys

MOVE_HORIZONTAL = "H"
MOVE_VERTICAL   = "V"
MOVE_DIAGONAL   = "D"

DIR_LEFT  = "L"
DIR_RIGHT = "R"
DIR_UP    = "U"
DIR_DOWN  = "D"

def get_coordinates(wire):
    coords = [[0,0]]
    for step in wire:
        step_dir = step[0]
        step_length = int(step[1:])
        new_coord = coords[-1].copy()
        if step_dir == DIR_RIGHT:
            new_coord[0] += step_length
        elif step_dir == DIR_LEFT:
            new_coord[0] -= step_length
        elif step_dir == DIR_UP:
            new_coord[1] += step_length
        elif step_dir == DIR_DOWN:
            new_coord[1] -= step_length
        coords.append(new_coord)
    return coords

def get_move_type(coord_from, coord_to):
    if coord_from == coord_to:
        return None
    elif coord_from[1] == coord_to[1]:
        return MOVE_HORIZONTAL
    elif coord_from[0] == coord_to[0]:
        return MOVE_VERTICAL
    else:
        return MOVE_DIAGONAL

def get_intersection_solution(h_coord_from, h_coord_to, v_coord_from, v_coord_to):
    h_move_span = sorted([h_coord_from[0], h_coord_to[0]])
    v_move_span = sorted([v_coord_from[1], v_coord_to[1]])
    if h_move_span[0] <= v_coord_from[0] <= h_move_span[1] and v_move_span[0] <= h_coord_from[1] <= v_move_span[1]:
        return [v_coord_from[0], h_coord_from[1]]
    else:
        return None

def get_intersection(coord1_from, coord1_to, coord2_from, coord2_to):
    move_type1 = get_move_type(coord1_from, coord1_to)
    move_type2 = get_move_type(coord2_from, coord2_to)
    if move_type1 == MOVE_HORIZONTAL and move_type2 == MOVE_VERTICAL:
        return get_intersection_solution(coord1_from, coord1_to, coord2_from, coord2_to)
    elif move_type1 == MOVE_VERTICAL and move_type2 == MOVE_HORIZONTAL:
        return get_intersection_solution(coord2_from, coord2_to, coord1_from, coord1_to)
    else:
        return None

def get_intersections(coords1, coords2):
    intersections = []
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
