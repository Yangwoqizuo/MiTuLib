from Element import Element


class DeltaTimeElement(Element):

    def __init__(self, time: float):
        """
        等待
        :param time: 时长
        """
        super(DeltaTimeElement, self).__init__("DeltaTimeE")
        self.time = time

    def to_dict(self):
        result = super().to_dict()
        result[Element.DEFAULTMAP_KEY] = {"time": str(self.time)}
        return result
