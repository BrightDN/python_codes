import unittest
from src.parsing.markdown.markdown_to_html_node import markdown_to_html_node
from src.nodes.parentnode import ParentNode
from src.nodes.leafnode import LeafNode

class TestMarkdownToHtmlNode(unittest.TestCase):
    def setUp(self):
        self.only_p = "paragraph"
        self.only_p_with_children = "paragraph with **bold** and *italic* parts"
        self.only_img = "![alt text](www.img.com)"
        self.only_link = "[click](www.link.com)"
        self.only_quote = "> quote\n> second line"
        self.only_code = "```codeblock```"
        self.only_heading = "# heading 1"
        self.only_heading2 = "## heading 2"
        self.only_ordered_list = "1. List item\n2. Other list item"
        self.only_unordered_list = "- List item\n- Other list item"
        self.multi_block = "paragraph\n\nother paragraph"


    def test_paragraph_no_children(self):
        self.assertEqual(markdown_to_html_node(self.only_p), ParentNode("div", [ParentNode("p", [LeafNode(None, "paragraph")])]))

    def test_paragraph_with_children(self):
        self.assertEqual(markdown_to_html_node(self.only_p_with_children), ParentNode("div", [ParentNode("p", [LeafNode(None, "paragraph with "), LeafNode("b", "bold"), LeafNode(None, " and "), LeafNode("i", "italic"), LeafNode(None, " parts")])]))

    def test_image(self):
        self.assertEqual(markdown_to_html_node(self.only_img), ParentNode("div", [ParentNode("p", [LeafNode("img", "", {"src":"www.img.com", "alt":"alt text"})])]))

    def test_link(self):
        self.assertEqual(markdown_to_html_node(self.only_link), ParentNode("div", [ParentNode("p", [LeafNode("a", "click", {"href":"www.link.com"})])]))

    def test_quoteblock(self):
        self.assertEqual(markdown_to_html_node(self.only_quote), ParentNode("div", [ParentNode("blockquote", [LeafNode(None, "quote"), LeafNode(None, "second line")])]))

    def test_codeblock(self):
        self.assertEqual(markdown_to_html_node(self.only_code), ParentNode("div", [ParentNode("pre", [LeafNode("code", "codeblock")])]))

    def test_heading1(self):
        self.assertEqual(markdown_to_html_node(self.only_heading), ParentNode("div", [LeafNode("h1", "heading 1")]))

    def test_heading2(self):
        self.assertEqual(markdown_to_html_node(self.only_heading2), ParentNode("div", [LeafNode("h2", "heading 2")]))

    def test_ordered_list(self):
        self.assertEqual(
        markdown_to_html_node(self.only_ordered_list),
        ParentNode("div", [
            ParentNode("ol", [
                ParentNode("li", [LeafNode(None, "List item")]),
                ParentNode("li", [LeafNode(None, "Other list item")])
            ])
        ])
    )
        
    def test_unordered_list(self):
        self.assertEqual(
        markdown_to_html_node(self.only_unordered_list),
        ParentNode("div", [
            ParentNode("ul", [
                ParentNode("li", [LeafNode(None, "List item")]),
                ParentNode("li", [LeafNode(None, "Other list item")])
            ])
        ])
    )
    def test_multiblock(self):
        self.assertEqual(markdown_to_html_node(self.multi_block), ParentNode("div", [ParentNode("p", [LeafNode(None, "paragraph")]), ParentNode("p", [LeafNode(None, "other paragraph")])]))

if __name__ == '__main__':
    unittest.main()