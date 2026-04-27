from textnode import TextNode, TextType 

def main():
    print("hello world")
    dummy = TextNode("Some shit here", TextType.LINK, "https://www.boot.dev")
    print(dummy)


if __name__ == '__main__':
    main()

