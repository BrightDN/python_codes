import unittest
from src.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "test", {"class": "paragraph"}, None)
        node2 = HTMLNode("p", "test", None)
        self.assertEqual(node.props_to_html(), " class=\"paragraph\"")
        self.assertNotEqual(node.props_to_html(), "class=\"paragraph\"")
        self.assertEqual(node2.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()