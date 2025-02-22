import unittest
from src.parsing.text.split_textnodes import split_nodes_delimiter
from src.nodes.textnode import TextNode, TextType

class TestSplitTextNodes(unittest.TestCase):
    def setUp(self):
        self.not_text_type = [TextNode("This is bold text", TextType.BOLD)]
        self.bold = [TextNode("This has **bold** text", TextType.TEXT)]
        self.bold_with_gap = [TextNode("This has ** bold ** text", TextType.TEXT)]
        self.empty = [TextNode("This has **** text", TextType.TEXT)]
        self.italic = [TextNode("This has *italic* text", TextType.TEXT)]
        self.code = [TextNode("This has `code` text", TextType.TEXT)]
        self.no_delimiter = [TextNode("No delimiter", TextType.TEXT)]
        self.multiple = [TextNode("This **has** multiple **bold** parts", TextType.TEXT)]
        self.multiple_in_row = [TextNode("This **has****multiple bold** parts", TextType.TEXT)]
        self.multiple_nodes = [TextNode("This is the **first** textnode", TextType.TEXT), TextNode("This is the **second** textnode", TextType.TEXT)]

    def test_not_text_type(self):
        self.assertEqual(split_nodes_delimiter(self.not_text_type, "**", TextType.BOLD), [TextNode("This is bold text", TextType.BOLD)])

    def test_bold(self):
        self.assertEqual(split_nodes_delimiter(self.bold, "**", TextType.BOLD), [TextNode("This has", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode("text", TextType.TEXT)])

    def test_bold_with_gap(self):
        self.assertEqual(split_nodes_delimiter(self.bold_with_gap, "**", TextType.BOLD), [TextNode("This has", TextType.TEXT), TextNode(" bold ", TextType.BOLD), TextNode("text", TextType.TEXT)])

    def test_empty(self):
        self.assertEqual(split_nodes_delimiter(self.empty, "**", TextType.BOLD), [TextNode("This has", TextType.TEXT), TextNode("", TextType.BOLD), TextNode("text", TextType.TEXT)])

    def test_italic(self):
        self.assertEqual(split_nodes_delimiter(self.italic, "*", TextType.ITALIC), [TextNode("This has", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode("text", TextType.TEXT)])    

    def test_code(self):
        self.assertEqual(split_nodes_delimiter(self.code, "`", TextType.CODE), [TextNode("This has", TextType.TEXT), TextNode("code", TextType.CODE), TextNode("text", TextType.TEXT)])

    def test_no_delimiter(self):
        self.assertEqual(split_nodes_delimiter(self.no_delimiter, "**", TextType.BOLD), [TextNode("No delimiter", TextType.TEXT)])

    def test_multiple_delimiter_pairs(self):
        self.assertEqual(split_nodes_delimiter(self.multiple, "**", TextType.BOLD), [TextNode("This", TextType.TEXT), TextNode("has", TextType.BOLD), TextNode("multiple", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode("parts", TextType.TEXT)])
    
    def test_multiple_delimiter_pairs_in_row(self):
        self.assertEqual(split_nodes_delimiter(self.multiple_in_row, "**", TextType.BOLD), [TextNode("This", TextType.TEXT), TextNode("has", TextType.BOLD), TextNode("multiple bold", TextType.BOLD), TextNode("parts", TextType.TEXT)])

    def test_multiple_nodes(self):
        self.assertEqual(split_nodes_delimiter(self.multiple_nodes, "**", TextType.BOLD), [TextNode("This is the", TextType.TEXT), TextNode("first", TextType.BOLD), TextNode("textnode", TextType.TEXT), TextNode("This is the", TextType.TEXT), TextNode("second", TextType.BOLD), TextNode("textnode", TextType.TEXT)])

    def test_invalid_delim(self):
        with self.assertRaises(Exception):
            split_nodes_delimiter([TextNode("random input", TextType.TEXT)], "//", TextType.BOLD)

    def test_missing_closing(self):
        with self.assertRaises(Exception):
            split_nodes_delimiter([TextNode("Only *one delimiter", TextType.TEXT)], "*", TextType.ITALIC)

if __name__ == '__main__':
    unittest.main()