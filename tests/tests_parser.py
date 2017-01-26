import unittest

from parser import extract_occurrences_from_one_file


class TestParser(unittest.TestCase):
    def test_find_filename(self):
        string = '<html>this is some html<script src="my/web/server/myEmptyScript.js"></script></html>'
        result = extract_occurrences_from_one_file(string)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], 'myEmptyScript.js')

    def test_find_filename_incorrect_type(self):
        string = '<html>this is some html<script src="my/web/server/thisIsNotAJs.json"></script></html>'
        result = extract_occurrences_from_one_file(string)
        self.assertEqual(len(result), 0)

    def test_find_filename_css(self):
        string = '<html>this is some html<link rel="stylesheet" href="http://www.url.com/B/style.css"></html>'
        result = extract_occurrences_from_one_file(string)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], 'style.css')


if __name__ == '__main__':
    unittest.main()
