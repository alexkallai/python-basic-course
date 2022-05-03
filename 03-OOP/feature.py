class Feature:
    """

    """

    line_char: str = "#"

    def print_line(self):
        print(self.line_char*50)

    @staticmethod
    def print_hello():
        print("Hello World")


if __name__ == "__main__":
    Feature.print_hello()
