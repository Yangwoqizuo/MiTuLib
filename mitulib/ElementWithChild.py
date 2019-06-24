"""
拥有子元素的元素，例如循环、分支
"""
from Element import Element
from ElementList import ElementList


class ElementWithChild(Element):
    def __init__(self, name: str, child1: list = None, child2: list = None):
        super(ElementWithChild, self).__init__(name)
        if child1:
            self.child1 = ElementList(child1)
        if child2:
            self.child2 = ElementList(child2)

    def add_into_list(self, target: list):
        self_index = len(target)
        super().add_into_list(target)
        if self.child1:
            child1_index = len(target)
            self.child1.add_into_list(target)
            target[self_index]["centerE1"] = child1_index
            target[child1_index]["proCE1"] = self_index
        if self.child2:
            child2_index = len(target)
            self.child2.add_into_list(target)
            target[self_index]["centerE2"] = child2_index
            target[child2_index]["proCE2"] = self_index
