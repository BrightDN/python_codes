import unittest
from src.nodes.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_plain(self):
        plain_text = LeafNode(None, "TitleText")
        self.assertEqual(plain_text.to_html(), "TitleText")
    
    def test_basic_tag(self):
        basic_tag = LeafNode("p", "paragraph")
        self.assertEqual(basic_tag.to_html(), "<p>paragraph</p>")
    
    def test_with_attr(self):
        basic_tags_w_attributes = LeafNode("p", "paragraph", {"class":"test"})
        self.assertEqual(basic_tags_w_attributes.to_html(), "<p class=\"test\">paragraph</p>")
        
    def test_link_href(self):
        link_w_href = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(link_w_href.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    def test_error_case(self):
        error_case_no_value = LeafNode(None, None)
        with self.assertRaises(ValueError):
            error_case_no_value.to_html()

if __name__ == "__main__":
    unittest.main()