from .Element import Element
from .DelayableElement import DelayableElement


class MusicElement(DelayableElement):
    def __init__(self, music_type, type_type, is_delayed):
        """
        音乐
        :param music_type: 乐器
        :param type_type: 乐器子类
        :param is_delayed: 是否等待到播放完成再进行下一条
        """
        super(MusicElement, self).__init__("MusicE", is_delayed)
        self.music_type = music_type
        self.type_type = type_type

    def to_dict(self):
        result = super().to_dict()
        result[Element.SELFMAP_KEY]["musicType"] = str(self.music_type)
        result[Element.SELFMAP_KEY]["musicTypeType"] = str(self.type_type)
        return result
