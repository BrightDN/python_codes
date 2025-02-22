import unittest
from src.markup_parsing import extract_markdown_images, extract_markdown_links

class TestMarkupParsing(unittest.TestCase):
    def setUp(self):
        self.text_has_none_to_return = "No links or images here!"
        self.text_one_to_return = "Only one ![image](www.example.com/img1) and one [linkText](www.example.com)"
        self.text_two_to_return = "Has two images, namingly: ![image](www.example.com/img1) and ![image](www.example.com/img2) one two links, namingly [linkText1](www.example.com) and [linkText2](www.example.com)"
        self.text_empty = ""
        self.text_spaces_in_test_subject = "Only one ![image](www.ex ample.com/img1) and one [linkText]( www.exampl e.com)"

    def test_empty_string(self):
        self.assertEqual(extract_markdown_images(self.text_empty), [])
        self.assertEqual(extract_markdown_links(self.text_empty), [])

    def test_no_image(self):
        self.assertEqual(extract_markdown_images(self.text_has_none_to_return), [])

    def test_one_image(self):
        self.assertEqual(extract_markdown_images(self.text_one_to_return), [("image", "www.example.com/img1")])

    def test_multiple_images(self):
        self.assertEqual(extract_markdown_images(self.text_two_to_return), [("image", "www.example.com/img1"), ("image", "www.example.com/img2")])

    def test_no_links(self):
        self.assertEqual(extract_markdown_links(self.text_has_none_to_return), [])

    def test_one_link(self):
        self.assertEqual(extract_markdown_links(self.text_one_to_return), [("linkText", "www.example.com")])

    def test_multiple_links(self):
        self.assertEqual(extract_markdown_links(self.text_two_to_return), [("linkText1", "www.example.com"), ("linkText2", "www.example.com")])

    def test_spaces_in_url(self):
        self.assertEqual(extract_markdown_images(self.text_spaces_in_test_subject), [("image", "www.example.com/img1")])
        self.assertEqual(extract_markdown_links(self.text_spaces_in_test_subject), [("linkText", "www.example.com")])

if __name__ == '__main__':
    unittest.main()