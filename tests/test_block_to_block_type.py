import unittest
from src.block_to_block_type import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def setUp(self):
        self.paragraph = "I am a paragraph"
        self.heading = "# I am a heading"
        self.no_space_heading = "#i am a heading"
        self.codeblock = "``` I am a codeblock ```"
        self.invalid_backtick_count = "``` I am a codeblock ``"
        self.ordered_list = "1. 1\n2. 2"
        self.ordered_list_sequence_break = "1. 1\n3. 2"
        self.quote = "> This is\n> A quote"
        self.wrong_quote = "> This is not\n<A quote"
        self.unordered_list = "* 1\n* 2"
        self.mixed_unordered_list = "* 1\n- 2"
        self.seq_break_unordered_list = "* 1\n1. 2"

    def test_paragraph(self):
        self.assertEqual(block_to_block_type(self.paragraph), "paragraph")

    def test_heading(self):
        self.assertEqual(block_to_block_type(self.heading), "heading")

    def test_codeblock(self):
        self.assertEqual(block_to_block_type(self.codeblock), "code")

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type(self.ordered_list), "ordered list")

    def test_quote(self):
        self.assertEqual(block_to_block_type(self.quote), "quote block")

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type(self.unordered_list), "unordered list")

    def test_mixed_unordered_list(self):
        self.assertEqual(block_to_block_type(self.mixed_unordered_list), "unordered list")

    def test_no_space_heading(self):
        self.assertEqual(block_to_block_type(self.no_space_heading), "paragraph")

    def test_invalid_backtick_count(self):
        self.assertEqual(block_to_block_type(self.invalid_backtick_count), "paragraph")

    def test_ordered_list_sequence_break(self):
        self.assertEqual(block_to_block_type(self.ordered_list_sequence_break), "paragraph")

    def test_wrong_quote(self):
        self.assertEqual(block_to_block_type(self.wrong_quote), "paragraph")

    def test_seq_break_unordered_list(self):
        self.assertEqual(block_to_block_type(self.seq_break_unordered_list), "paragraph")

if __name__ == '__main__':
    unittest.main()