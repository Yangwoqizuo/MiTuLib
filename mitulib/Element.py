"""
所有元素的父类
"""


class Element:
    DEFAULTMAP_KEY = "defaultMap"
    SELFMAP_KEY = "selfMap"
    UUID = "uuid"

    def __init__(self, type_name: str):
        self.type_name = type_name
        self._index = -1

    def to_dict(self):
        """
        转换成dict
        :return:
        """
        result = {'typeName': self.type_name}
        return result

    def add_into_list(self, target):
        """
        把自己和下属元素加入target
        :param target: 目标数组
        """
        target.append(self.to_dict())
