import unittest
from unittest.mock import patch
from io import StringIO
import io
import sys
import fibonnachi as code

class TestFizzBuzz(unittest.TestCase):

    @patch("sys.stdin", StringIO("1\n2\n"))
    def test_input_is_added_to_list(self):
        
        sys.stdout = io.StringIO()
        self.assertEqual(code.get_input(),[1,2])

    @patch("sys.stdin", StringIO("1\n2\n6\n"))
    def test_fibo_sequence(self):
        
        sys.stdout = io.StringIO()
        self.assertEqual(code.fibo(),[1,2,3,5,8,13])

if __name__ == '__main__':
    unittest.main()