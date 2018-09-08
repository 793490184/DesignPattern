import copy


class Prototype:

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


def main():
    class A:
        def __str__(self):
            return 'I am A'

    a = A()
    prototype = Prototype()
    prototype.register_object('b', a)
    b = prototype.clone('b', a=1, b=2, c=3)

    print(a)
    print(b.a, b.b, b.c)
    print(b)
    print(a)


if __name__ == '__main__':
    main()
