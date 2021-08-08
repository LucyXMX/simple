import src.simple
import unittest

class TestSimple(unittest.TestCase):

    def test_add(self):
        simple = src.simple.Simple()
        self.assertEqual(2.0,simple.add(1,1))