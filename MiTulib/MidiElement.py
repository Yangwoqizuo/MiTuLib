from .Element import Element


class MidiElement(Element):

    def __init__(self, instrument_type, tone, time):
        """
        音乐
        :param instrument_type: 乐器类型
        :param tone: 声调，0-20
        :param time: 通道
        """
        super(MidiElement, self).__init__("MidiE")
        self.type = instrument_type
        self.tone = tone
        self.time = time

    def on_get_changable_variables(self):
        return {"MidiTime": self.time}

    def to_dict(self):
        result = super().to_dict()
        result[Element.SELFMAP_KEY] = {
            "midiType": str(self.tone),
            "midiTypeType": str(self.type)
        }
        return result
