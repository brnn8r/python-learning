#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
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


class Triangle(object):

    def __init__(self, name, first_side, second_side, third_side):
        self._name = name
        self._first_side = first_side
        self._second_side = second_side
        self._third_side = third_side

    @property
    def name(self):
        return self._name


class EquilateralTriangle(Triangle):

    def __init__(self, side):
        super().__init__('equilateral', side, side, side)


class IsoscelesTriangle(Triangle):

    def __init__(self, first_side, second_side, third_side):
        super().__init__('isosceles', first_side, second_side, third_side)


class ScaleneTriangle(Triangle):

    def __init__(self, first_side, second_side, third_side):
        super().__init__('scalene', first_side, second_side, third_side)


class TriangleBuilder(object):

    def __init__(self, first_side, second_side, third_side):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    def __call__(self):

        if self.first_side <= 0 or self.second_side <= 0 or self.third_side <= 0:
            raise TriangleError("Triangle side length must be positive")

        # order side lengths from smaller to larger to make a canonical side length ordering
        self.first_side, self.second_side, self.third_side = sorted([self.first_side, self.second_side, self.third_side])

        if self.first_side + self.second_side < self.third_side:
            raise TriangleError("This triangle would fail the triangle inequality a + b > c")

        if self.first_side == self.second_side and self.second_side == self.third_side and self.first_side == self.third_side:
            return EquilateralTriangle(self.first_side)

        if self.first_side != self.second_side and self.first_side != self.third_side and self.second_side != self.third_side:
            return ScaleneTriangle(self.first_side, self.second_side, self.third_side)

        return IsoscelesTriangle(self.first_side, self.second_side, self.third_side)


def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    builder = TriangleBuilder(a, b, c)

    return builder().name


# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
