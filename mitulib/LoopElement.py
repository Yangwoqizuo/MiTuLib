"""
if
"""
from ElementWithChild import ElementWithChild
from Element import Element


class LoopElement(ElementWithChild):
    def __init__(self, loop_body: list = None):
        """
        循环元素
        :param loop_body:
        """
        super(LoopElement, self).__init__("LoopE", loop_body, None)

    def to_dict(self):
        result = super().to_dict()
        result[Element.SELFMAP_KEY] = {"looptype": "LoopInfinite_"}
        return result

    def add_into_list(self, target: list):
        indexes = super().add_into_list(target)
        end_index = LoopEndEelemt().add_into_list(target)
        indexes.extend(end_index)
        return indexes


class LoopEndEelemt(Element):
    def __init__(self):
        super(LoopEndEelemt, self).__init__("LoopEndE")
