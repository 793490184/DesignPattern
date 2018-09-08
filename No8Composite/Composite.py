class Component:
    def __init__(self, str_name):
        self.str_name = str_name

    def add(self, com):
        pass

    def display(self, n_depth):
        pass


class Leaf(Component):
    def __init__(self, com):
        print(com)

    def add(self, com):
        print('leaf can not add')

    def display(self, n_depth):
        str_temp = '+' * n_depth
        str_temp = str_temp + self.m_str_name
        print(str_temp)


class Composite(Component):
    def __init__(self, str_name):
        self.m_str_name = str_name
        self.c = []

    def add(self, com):
        self.c.append(com)

    def display(self, n_depth):
        str_temp = '-' * n_depth
        str_temp = str_temp + self.m_str_name
        print(str_temp)
        for com in self.c:
            com.display(n_depth + 2)


if __name__ == '__main__':
    p = Component('Wong')
    p.add(Leaf('Lee'))
    p.add(Leaf('zhao'))
    p1 = Component('Wu')
    p1.add(Leaf('San'))
    p.add(p1)
    p.display(1)
