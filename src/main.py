from textnode import TextNode, TextType
from copystatic import delete_and_replace
from markdown_blocks import generate_page, generate_pages_recursive


def main():
    delete_and_replace("static", "public")
    generate_pages_recursive("content/", "template.html", "public/")


if __name__ == '__main__':
    main()

