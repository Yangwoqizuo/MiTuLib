"""
容纳元素的数组
"""


class ElementList:

    def __init__(self, initial_elements: list = None):
        self.elements = []
        if initial_elements:
            self.elements.extend(initial_elements)

    def add_into_list(self, target: list):
        indexes = []
        for i in range(len(self.elements)):
            element_indexes = self.elements[i].add_into_list(target)
            indexes.extend(element_indexes)
        for i in range(len(indexes)):
            element = target[indexes[i]]
            if i < len(indexes) - 1:
                element["nextE"] = indexes[i + 1]
            if i > 0:
                element["proE"] = indexes[i - 1]
