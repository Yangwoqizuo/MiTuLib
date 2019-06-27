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
        variables = self.on_get_changable_variables()
        for (k, v) in variables.items():
            try:
                float(v)
                # 如果是数字，使用defaultMap
                if Element.DEFAULTMAP_KEY not in result.keys():
                    result[Element.DEFAULTMAP_KEY] = {}
                result[Element.DEFAULTMAP_KEY][str(k)] = str(v)
            except ValueError:
                # 如果不是数字，是variable
                if Element.CHANGEMAP_KEY not in result.keys():
                    result[Element.CHANGEMAP_KEY] = {}
                # 修改changeMap字段
                result[Element.CHANGEMAP_KEY][str(k)] = VariableElement(str(v)).to_dict()
                # defaultMap相应字段置0
                if Element.DEFAULTMAP_KEY not in result.keys():
                    result[Element.DEFAULTMAP_KEY] = {}
                result[Element.DEFAULTMAP_KEY][str(k)] = str(0)

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

    def on_get_changable_variables(self):
        """
        子类有参数可以为变量时，重写此方法。判断value为数字，使用defaultMap，否则使用changeMap
        :return:
        """
        return {}


class VariableElement(Element):
    def __init__(self, variable: str):
        super(VariableElement, self).__init__("VariableE")
        self.variable = variable

    def to_dict(self):
        result = super().to_dict()
        result[Element.DEFAULTMAP_KEY] = {"Variable": self.variable}
        return result
