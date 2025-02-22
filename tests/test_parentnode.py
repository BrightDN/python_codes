import unittest
from src.parentnode import ParentNode
from src.leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def setUp(self):
        self.one_child = ParentNode("div", [LeafNode("p", "text")])
        self.multiple_children = ParentNode("div", [LeafNode("p", "text"), LeafNode("p", "text")])
        self.none_tag = ParentNode(None, [LeafNode("p", "text")])
        self.no_children = ParentNode("div", None)
        self.nested_parent = ParentNode("div", [
            ParentNode("section", [
            LeafNode("p", "nested")
            ])
        ])
    
        self.empty_children = ParentNode("div", [])  # Empty list, not None
    
        self.mixed_children = ParentNode("div", [
            LeafNode("p", "leaf"),
            ParentNode("span", [LeafNode("b", "nested")])
        ])

    def test_one_child(self):
        self.assertEqual(self.one_child.to_html(), "<div><p>text</p></div>")

    def test_multiple_children(self):
        self.assertEqual(self.multiple_children.to_html(), "<div><p>text</p><p>text</p></div>")

    def test_none_tag(self):
        with self.assertRaises(ValueError) as context:
            self.none_tag.to_html()
        self.assertEqual(str(context.exception), "Your tag must not be of None-type")

    def test_no_children(self):
        with self.assertRaises(ValueError) as context:
            self.no_children.to_html()
        self.assertEqual(str(context.exception), "You must have children!")

    def test_nested_parent(self):
        self.assertEqual(self.nested_parent.to_html(), "<div><section><p>nested</p></section></div>")

    def test_empty_children_list(self):
        self.assertEqual(self.empty_children.to_html(), "<div></div>")

    def test_mixed_children(self):
        self.assertEqual(self.mixed_children.to_html(), "<div><p>leaf</p><span><b>nested</b></span></div>")

if __name__ == '__main__':
    unittest.main()