from Element import Element


class DeltaTimeElement(Element):

    def __init__(self, time):
        """
        等待
        :param time: 时长
        """
        super(DeltaTimeElement, self).__init__("DeltaTimeE")
        self.time = time

    def to_dict(self):
        result = super().to_dict()
        if isinstance(self.time, str):
            result[Element.DEFAULTMAP_KEY] = {"time": "0"}
            result[Element.CHANGEMAP_KEY] = {"time": {"typeName": "VariableE", "defaultMap": {"Variable": self.time}}}
        else:
            result[Element.DEFAULTMAP_KEY] = {"time": str(self.time)}
        return result
