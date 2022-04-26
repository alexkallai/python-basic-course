"""
Module is not for import
"""

class MainClass:
    """
    This class is for practice.
    ez egy docstring
    """

    class_variable: str = "default value"

    def __init__(self, class_variable: str = "Default Argument"):
        self.class_variable = class_variable

    def just_a_method(self):
        print(self.class_variable)

    @staticmethod
    def static_thing():
        """
        this method type will try to reach a class variable without success
        :return:
        """

        try:
            print(self.class_variable)
        except Exception as err:
