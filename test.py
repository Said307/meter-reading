import unittest
import meter


class TestRun(unittest.TestCase):
 
    def test_arg_parser(self):
        """ Test that parse function identifies sourcefile from sysargv"""
        mock_sysarg = ['rawdata.txt']
        parser = meter.parse(mock_sysarg)
        self.assertEqual(parser.sourcefile,'rawdata.txt')


if __name__ == '__main__':
    unittest.main()