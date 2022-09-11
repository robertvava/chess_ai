import unittest as tst
from src.constants import convert_to_pixels, convert_to_rowcol

class TestExtra(tst.TestCase):

    def test_convert_to_pixels(self):
        self.assertEqual((0, 1), convert_to_pixels(76, 125))
