import datetime
from feature import Feature


class MainClass:
    """
    Definition
    """

    def __init__(self):
        FeatureInstance = Feature()
        FeatureInstance.print_line()

    @staticmethod
    def print_message():
        Feature.print_hello()


# nagybetűvel szokták a példányok neveit is írni
if __name__ == "__main__":
    MainInstance = MainClass()
    print(datetime.datetime.now())
    MainClass.print_hello()
    MainInstance.print_line()
    MainInstance.print_hello()
