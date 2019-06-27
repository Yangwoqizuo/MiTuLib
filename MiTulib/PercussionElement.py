from .Element import Element


class PercussionElement(Element):
    def __init__(self, percussion_type: int):
        """
        打击乐
        :param percussion_type: 编号
        """
        super(PercussionElement, self).__init__("PercussionE")
        self.percussion_type = percussion_type

    def to_dict(self):
        result = super().to_dict()
        result[Element.SELFMAP_KEY] = {"PercussionType": str(self.percussion_type)}
        return result
