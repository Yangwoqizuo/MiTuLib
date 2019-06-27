from .Element import Element


class MusicElement(Element):
    def __init__(self, music_type, type_type, is_delayed):
        """
        音乐
        :param music_type: 乐器
        :param type_type: 乐器子类
        :param is_delayed: 是否等待到播放完成再进行下一条
        """
        super(MusicElement, self).__init__("MusicE")
        self.music_type = music_type
        self.type_type = type_type
        self.is_delayed = is_delayed

    def to_dict(self):
        result = super().to_dict()
        result[Element.SELFMAP_KEY] = {
            "musicType": str(self.music_type),
            "musicTypeType": str(self.type_type),
            "isDelayed": "1" if self.is_delayed else "0"
        }
        return result
