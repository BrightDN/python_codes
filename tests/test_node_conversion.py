import unittest
from src.htmlnode import HTMLNode
from src.textnode import TextNode, TextType
from src.leafnode import LeafNode

class TestNodeConversion(unittest.TestCase):
    def setUp(self):
        self.classic = HTMLNode.text_node_to_html_node(TextNode("text", TextType.TEXT))
        self.bold = HTMLNode.text_node_to_html_node(TextNode("text", TextType.BOLD))
        self.italic = HTMLNode.text_node_to_html_node(TextNode("text", TextType.ITALIC))
        self.code = HTMLNode.text_node_to_html_node(TextNode("text", TextType.CODE))
        self.img = HTMLNode.text_node_to_html_node(TextNode("text", TextType.IMAGE, "www.example.com"))
        self.link = HTMLNode.text_node_to_html_node(TextNode("text", TextType.LINK, "www.example.com"))

    def test_classic(self):
        self.assertEqual(self.classic, LeafNode(None, "text"))

    def test_bold(self):
        self.assertEqual(self.bold, LeafNode("b", "text"))

    def test_italic(self):
        self.assertEqual(self.italic, LeafNode("i", "text"))

    def test_code(self):
        self.assertEqual(self.code, LeafNode("code", "text"))

    def test_img(self):
        self.assertEqual(self.img, LeafNode("img", "", {"src": "www.example.com", "alt":"text"}))

    def test_link(self):
        self.assertEqual(self.link, LeafNode("a", "text", {"href":"www.example.com"}))

    def test_wrong(self):
        with self.assertRaises(Exception):
            HTMLNode.text_node_to_html_node(TextNode("text", TextType.DOESNTEXIST, "www.example.com"))
    
    def test_img_no_url(self):
        with self.assertRaises(Exception):
            HTMLNode.text_node_to_html_node(TextNode("text", TextType.IMAGE))

    def test_link_no_url(self):
        with self.assertRaises(Exception):
            HTMLNode.text_node_to_html_node(TextNode("text", TextType.LINK))

if __name__ == '__main__':
    unittest.main()