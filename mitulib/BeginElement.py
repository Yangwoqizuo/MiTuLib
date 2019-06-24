"""
开始节点
"""
from Element import Element


class BeginElement(Element):
    MODE_BALANCE = 0
    MODE_FREE = 1

    def __init__(self, mode):
        super(BeginElement, self).__init__("BeginE")
        self.mode = mode

    def to_dict(self):
        result = super().to_dict()
        result[Element.SELFMAP_KEY] = {"mode": str(self.mode)}
        return result
