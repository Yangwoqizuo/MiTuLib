from .Element import Element


class EMTimeElement(Element):
    def __init__(self, em_type, speed, time, is_delayed: bool):
        """
        电机按照时间
        :param em_type: 电机ABCD
        :param speed: -100-100
        :param time: 时间
        :param is_delayed: 是否执行完本条再进行下一条
        """
        super(EMTimeElement, self).__init__("EMTimeE")
        self.em_type = em_type
        self.speed = speed
        self.time = time
        self.is_delayed = is_delayed

    def on_get_changable_variables(self):
        return {
            "speed": self.speed,
            "time": self.time
        }

    def to_dict(self):
        result = super().to_dict()
        result[Element.DEFAULTMAP_KEY]["EMType"] = self.em_type
        result[Element.DEFAULTMAP_KEY]["isDelayed"] = "1" if self.is_delayed else "0"
        return result
