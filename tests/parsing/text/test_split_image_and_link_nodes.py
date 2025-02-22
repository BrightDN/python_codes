import unittest
from src.nodes.textnode import *
from src.parsing.text.split_textnodes import split_nodes_images, split_nodes_links

class TestSplitImageAndLinkNodes(unittest.TestCase):
    def setUp(self):
        self.no_links_no_images = TextNode("Regular text without any images or links", TextType.TEXT)
        self.image_in_middle = TextNode("Text with ![an image](image.jpg) in the middle", TextType.TEXT)
        self.link_in_middle = TextNode("Text with [a link](https://example.com) in the middle", TextType.TEXT)
        self.multiple_images = TextNode("Text with multiple ![images](img1.jpg) and ![photos](img2.jpg)", TextType.TEXT)
        self.multiple_links = TextNode("Text with multiple [links](link1.com) and [anchors](link2.com)", TextType.TEXT)
        self.mixed = TextNode("Text with mixed [links](link1.com) and ![images](img1.jpg)", TextType.TEXT)
        self.mixed_multiple = TextNode("Text with multiple mixed [links](link1.com) and [anchors](link2.com), but also ![images](img1.jpg) and ![photos](img2.jpg)", TextType.TEXT)

def test_empty_input(self):
    self.assertEqual(split_nodes_images([]), [])
    self.assertEqual(split_nodes_links([]), [])

def test_no_links_no_images(self):
    result_images = split_nodes_images([self.no_links_no_images])
    result_links = split_nodes_links([self.no_links_no_images])
    self.assertEqual(len(result_images), 1)
    self.assertEqual(len(result_links), 1)
    self.assertEqual(result_images[0].text, "Regular text without any images or links")
    self.assertEqual(result_links[0].text, "Regular text without any images or links")

def test_single_image(self):
    result = split_nodes_images([self.image_in_middle])
    self.assertEqual(len(result), 3)
    self.assertEqual(result[0].text, "Text with ")
    self.assertEqual(result[1].text, "an image")
    self.assertEqual(result[1].url, "image.jpg")
    self.assertEqual(result[2].text, " in the middle")

def test_single_link(self):
    result = split_nodes_links([self.link_in_middle])
    self.assertEqual(len(result), 3)
    self.assertEqual(result[0].text, "Text with ")
    self.assertEqual(result[1].text, "a link")
    self.assertEqual(result[1].url, "https://example.com")
    self.assertEqual(result[2].text, " in the middle")

def test_multiple_images(self):
    result = split_nodes_images([self.multiple_images])
    self.assertEqual(len(result), 4)
    self.assertEqual(result[0].text, "Text with multiple ")
    self.assertEqual(result[1].text, "images")
    self.assertEqual(result[1].url, "img1.jpg")
    self.assertEqual(result[2].text, " and ")
    self.assertEqual(result[3].text, "photos")
    self.assertEqual(result[3].url, "img2.jpg")

def test_multiple_links(self):
    result = split_nodes_links([self.multiple_links])
    self.assertEqual(len(result), 4)
    self.assertEqual(result[0].text, "Text with multiple ")
    self.assertEqual(result[1].text, "links")
    self.assertEqual(result[1].url, "link1.com")
    self.assertEqual(result[2].text, " and ")
    self.assertEqual(result[3].text, "anchors")
    self.assertEqual(result[3].url, "link2.com")

def test_mixed_content(self):
    result_images = split_nodes_images([self.mixed])
    result_links = split_nodes_links([self.mixed])
    
    # Test images
    self.assertEqual(len(result_images), 3)
    self.assertEqual(result_images[1].text, "images")
    self.assertEqual(result_images[1].url, "img1.jpg")
    
    # Test links
    self.assertEqual(len(result_links), 3)
    self.assertEqual(result_links[1].text, "links")
if __name__ == '__main__':
    unittest.main()