"""
元素
A=1
"""
from Element import Element


class VarAssignmentElement(Element):
    VAR_KEY = "VarAssVar"
    VALUE_KEY = "VarAssValue"

    def __init__(self, key: str, value: str):
        super(VarAssignmentElement, self).__init__("VarAssignmentE")
        self.key = key
        self.value = value

    def to_dict(self):
        result = super().to_dict()
        result[Element.DEFAULTMAP_KEY] = {VarAssignmentElement.VALUE_KEY: str(self.value),
                                          VarAssignmentElement.VAR_KEY: str(self.key)}
        return result
