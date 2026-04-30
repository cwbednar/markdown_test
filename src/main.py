from textnode import TextNode, TextType
from copystatic import delete_and_replace, copy_files_recursive
from markdown_blocks import generate_page, generate_pages_recursive

import sys
import os
import shutil

def main():

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    if os.path.exists("./docs"):
        shutil.rmtree("./docs")
    
    copy_files_recursive("./static", "./docs")
    # delete_and_replace("static", "public")
    generate_pages_recursive("content/", "template.html", "docs/", basepath)


if __name__ == '__main__':
    main()

