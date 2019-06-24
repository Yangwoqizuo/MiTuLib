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
        elements = []
        for i in range(len(self.elements)):
            index = len(target)
            indexes.append(index)
            self.elements[i].add_into_list(target)
            elements.append(target[index])
        for i in range(len(elements)):
            element = elements[i]
            if i < len(elements) - 1:
                element["nextE"] = indexes[i + 1]
            if i > 0:
                element["proE"] = indexes[i - 1]
