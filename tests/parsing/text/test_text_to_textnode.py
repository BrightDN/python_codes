import unittest
from src.parsing.text.text_to_textnode import text_to_textnode
from src.nodes.textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def setUp(self):
        self.plain = "Plain text"
        self.image = "this has ![alt text](url.com)"
        self.link = "this has a [clickable](url.com)"
        self.code = "this has `code` text"
        self.bold = "this has **bold text**"
        self.italic = "this has *italic text*"
        self.mixed = "this is a mixed code text that is as following: `[clickable](url.com)`"
        self.multiple = "this has **bold** and *italic* text"
        self.stitchy = "this is **bold**ly done"
        self.empty = ""



    def test_plain(self):
        self.assertEqual(text_to_textnode(self.plain), [TextNode("Plain text", TextType.TEXT)])

    def test_image(self):
        self.assertEqual(text_to_textnode(self.image), [TextNode("this has ", TextType.TEXT), TextNode("alt text", TextType.IMAGE, "url.com")])

    def test_link(self):
        self.assertEqual(text_to_textnode(self.link), [TextNode("this has a ", TextType.TEXT), TextNode("clickable", TextType.LINK, "url.com")])

    def test_code(self):
        self.assertEqual(text_to_textnode(self.code), [TextNode("this has ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" text", TextType.TEXT)])

    def test_bold(self):
        self.assertEqual(text_to_textnode(self.bold), [TextNode("this has ", TextType.TEXT), TextNode("bold text", TextType.BOLD)])

    def test_italic(self):
        self.assertEqual(text_to_textnode(self.italic), [TextNode("this has ", TextType.TEXT), TextNode("italic text", TextType.ITALIC)])

    def test_mixed(self):
        self.assertEqual(text_to_textnode(self.mixed), [TextNode("this is a mixed code text that is as following: ", TextType.TEXT), TextNode("[clickable](url.com)", TextType.CODE)])

    def test_empty(self):
        self.assertEqual(text_to_textnode(self.empty), [])

    def test_stitchy(self):
        self.assertEqual(text_to_textnode(self.stitchy), [TextNode("this is ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode("ly done", TextType.TEXT)])

    def test_multiple(self):
        self.assertEqual(text_to_textnode(self.multiple), [TextNode("this has ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" and ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" text", TextType.TEXT)])
if __name__ == '__main__':
    unittest.main()