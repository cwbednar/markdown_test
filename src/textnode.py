import re 
from enum import Enum

from htmlnode import LeafNode, ParentNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text 
        self.text_type = text_type
        self.url = url 

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("Invalid node type")
    else:
        match(text_node.text_type):
            case TextType.TEXT:
                return LeafNode(None, text_node.text, None)
            case TextType.BOLD:
                return LeafNode("b", text_node.text, None)
            case TextType.ITALIC:
                return LeafNode("i", text_node.text, None)
            case TextType.CODE:
                return LeafNode("code", text_node.text, None)
            case TextType.LINK:
                return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
            case TextType.IMAGE:
                return LeafNode("img", text_node.text, {"src": f"{text_node.url}", "alt": f"{text_node.text}"})

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            parts = node.text.split(delimiter)
            if len(parts) % 2 != 0:
                raise Exception("Invalid number of identifiers")
            else:
                for i, part in enumerate(parts):
                    if part == "":
                        continue
                    if i % 2 == 0:
                        new_node = TextNode(part, TextType.TEXT)
                        result.append(new_node)
                    else:
                        new_node = TextNode(part, text_type)
                        result.append(new_node)
    return result

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches 

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches