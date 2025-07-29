from geometry.circle import calculate_area, calculate_circ
from math import pi
import numpy as np

def test_area():
    r = 1
    area = calculate_area(r)
    assert area == pi, "The calculate is wrong"


def test_circ():
    r = 1
    circ = calculate_circ(r)
    ans = 2*pi
    assert circ == ans