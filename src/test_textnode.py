import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode, ParentNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD,  "https://www.boot.dev") 
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node",TextType.BOLD, "https://www.boot.dev") 
        node2 = TextNode("This is not text node", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node.url, None)

    def test_no_text(self):
        node = TextNode(None, TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node.text, None)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()
