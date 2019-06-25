from Element import Element
from ElementList import ElementList


class ElementWithChild(Element):
    def __init__(self, name: str, child1: list = None, child2: list = None):
        """
        拥有子元素的元素，例如循环、分支
        :param name: 名称
        :param child1: 子列表1
        :param child2: 子列表2
        """
        super(ElementWithChild, self).__init__(name)
        if child1:
            self.child1 = ElementList(child1)
        if child2:
            self.child2 = ElementList(child2)

    def add_into_list(self, target: list):
        index = super().add_into_list(target)
        self_index = index[0]
        if hasattr(self, "child1"):
            child1_index = len(target)
            self.child1.add_into_list(target, proce1=self_index)
            target[self_index]["centerE1"] = child1_index
        if hasattr(self, "child2"):
            child2_index = len(target)
            self.child2.add_into_list(target, proce2=self_index)
            target[self_index]["centerE2"] = child2_index
        return index
