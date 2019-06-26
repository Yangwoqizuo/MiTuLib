class Element:
    DEFAULTMAP_KEY = "defaultMap"
    SELFMAP_KEY = "selfMap"
    CHANGEMAP_KEY = "changeMap"
    UUID = "uuid"

    def __init__(self, type_name: str):
        """
        所有元素的父类
        :param type_name: 类型名称
        """
        self.type_name = type_name
        self._index = -1

    def to_dict(self):
        """
        转换成dict
        :return:
        """
        result = {'typeName': self.type_name}
        return result

    def add_into_list(self, target: list):
        """
        把自己和下属元素加入target
        :param target: 目标数组
        :return: 当前元素所在下标（有的元素插入不只一次，比如Loop）
        """
        index = len(target)
        target.append(self.to_dict())
        return [index]
