class Type(object):

    def __init__(self, corn=None, name=None, type=object):
        self.corn = corn
        self.name = name
        self.type = type

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.corn == other.corn and\
                    self.name == other.name and\
                    self.type == other.type
        return False

    def common_type(self, other):
        if self == other:
            return self
        if self.type == other.type:
            return Type(type=self.type)
        return Type(type=object)

class Dict(Type):

    def __init__(self, corn=None, name=None, mapping=None):
        super(Dict, self).__init__(corn=corn, name=name, type=dict)
        self.mapping = mapping

    def __eq__(self, other):
        return super(Dict, self).__eq__(other) and\
                self.mapping == other.mapping


class List(Type):

    def __init__(self, corn=None, name=None, inner_type=Type(type=object)):
        super(List, self).__init__(corn=corn, name=name, type=list)
        self.inner_type = inner_type

    def __eq__(self, other):
        return super(List, self).__eq__(other) and\
                self.inner_type == other.inner_type

    def common_type(self, other):
        if self == other:
            return self
        elif isinstance(other, List):
            return List(inner_type=self.inner_type.common_type(other.inner_type))
        else:
            return Type(type=object)

