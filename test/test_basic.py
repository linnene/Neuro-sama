import sys
import os
import unittest

# Add src to path so we can import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from neuro_sama import hello

class TestNeuroSama(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello from neuro-sama package!")

if __name__ == '__main__':
    unittest.main()
