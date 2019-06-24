"""
if
"""
from ElementWithChild import ElementWithChild


class IfElement(ElementWithChild):
    def __init__(self, var1, operator, var2, then_do: list = None, else_do: list = None):
        super(IfElement, self).__init__("ConditionE1", then_do, else_do)
        self.var1 = var1
        self.var2 = var2
        self.operator = operator

    def to_dict(self):
        result = super().to_dict()
        result["defaultC"] = {
            "typeName": "ConditionTrueE",
            "selfMap": {
                "con": "1"
            }
        }
        result["changeC"] = {
            "typeName": "ConContainE",
            "defaultMap": {
                "equal": str(self.operator),
                "variable1": str(self.var1),
                "variable2": str(self.var2)
            }
        }
        return result
