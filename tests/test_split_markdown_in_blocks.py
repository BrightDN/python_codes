import unittest
from src.split_markdown_in_blocks import split_markdown_in_blocks

class TestSplitMarkdownInBlocks(unittest.TestCase):
    def setUp(self):
        self.empty = ""
        self.one_block = "# This is one block"
        self.trailing_text = "  # This is one block   "
        self.trailing_text_multiline = "  # This is one block   \nWith 2 lines"
        self.multiblocks = "#first block\n\n\nsecond block\nwith more than 1 line"
        self.empty_blocks = "# first block\n\n\n\n\n\n\nnew block"
        self.only_new_lines = "\n\n\n\n\n"
        self.single_trailing_new_line = "# Heading\n\n\n"
        self.mixed_white_space = "# Heading\n   \n\n\t\nSecond block"

    def test_empty(self):
        self.assertEqual(split_markdown_in_blocks(self.empty), [])

    def test_one_block(self):
        self.assertEqual(split_markdown_in_blocks(self.one_block), ["# This is one block"])

    def test_trailing_text(self):
        self.assertEqual(split_markdown_in_blocks(self.trailing_text), ["# This is one block"])

    def test_trailing_text_multiline(self):
        self.assertEqual(split_markdown_in_blocks(self.trailing_text_multiline), ["# This is one block\nWith 2 lines"])

    def test_multiblocks(self):
        self.assertEqual(split_markdown_in_blocks(self.multiblocks), ["#first block", "second block\nwith more than 1 line"])

    def test_empty_blocks(self):
        self.assertEqual(split_markdown_in_blocks(self.empty_blocks), ["# first block", "new block"])

    def test_only_new_lines(self):
        self.assertEqual(split_markdown_in_blocks(self.only_new_lines), [])

    def test_single_trailing_new_line(self):
        self.assertEqual(split_markdown_in_blocks(self.single_trailing_new_line), ["# Heading"])

    def test_mixed_white_space(self):
        self.assertEqual(split_markdown_in_blocks(self.mixed_white_space), ["# Heading", "Second block"])

if __name__ == '__main__':
    unittest.main()