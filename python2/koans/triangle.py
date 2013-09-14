#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    sides = sorted([a, b, c])
    invalid_side = (sides[0] <= 0)
    smaller_sides = sides[0] + sides[1]
    side_too_big = (smaller_sides <= sides[2])
    if invalid_side:
        raise TriangleError, "Triangles cannot have negative sides"
    if side_too_big:
        error_msg = "Longest side ({0}) has to be"
        "less than {1}".format(sides[2], smaller_sides)
        raise TriangleError, "One of the sides of this triangle ({0}) is too big"

    unique_sides = set(sides)
    num_sides = len(unique_sides)
    if num_sides == 1: return 'equilateral'
    if num_sides == 2: return 'isosceles'
    return 'scalene'


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
