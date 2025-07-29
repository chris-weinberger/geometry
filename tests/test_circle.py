from geometry.circle import calculate_area
from math import pi
import numpy as np

def test_area():
    r = 1
    area = calculate_area(r)
    assert area == pi, "The calculate is wrong"

    
    #r = -1
    #area = calculate_area(r)
    #assert area == np.nan