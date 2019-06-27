from .Element import Element


class MidiChordElement(Element):
    def __init__(self, chord_tones, chord_chord, chord_time):
        """
        和弦
        :param chord_tones:
        :param chord_chord:
        :param chord_time: 节奏
        """
        super(MidiChordElement, self).__init__("MidiChordE")
        self.chord_tones = chord_tones
        self.chord_chord = chord_chord
        self.chord_time = chord_time

    def on_get_changable_variables(self):
        return {"MidiChordTime": self.chord_time}

    def to_dict(self):
        result = super().to_dict()
        result[Element.SELFMAP_KEY] = {
            "MidiChordChord": str(self.chord_chord),
            "MidiChordTones": str(self.chord_tones)
        }
