from .Element import Element


class DelayableElement(Element):
    def __init__(self, type_name: str, is_delayed: bool):
        super(DelayableElement, self).__init__(type_name)
        self.is_delayed = is_delayed

    def to_dict(self):
        result = super().to_dict()
        result[Element.SELFMAP_KEY] = {
            "isDelayed": "1" if self.is_delayed else "0"
        }
