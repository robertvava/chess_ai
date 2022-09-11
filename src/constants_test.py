import unittest as tst
from constants import convert_to_pixels, convert_to_rowcol
from math import floor

class TestExtra(tst.TestCase):
    
    def test_convert_to_rowcol(self):
        for i in range(10):
            for j in range(0, 10, -1):
                self.assertEqual((i, j), convert_to_rowcol(floor((i*100)+25), floor((j*100)+25)))
 

tst.main()
