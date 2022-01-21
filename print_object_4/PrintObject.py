class A:
    def __init__(self, value: int):
        self.value = value

    # def __str__(self):
    #     return str(self.value)


class B:
    def __init__(self, value: float):
        self.value = value


class ObjectException(Exception):
    pass


def func(obj) -> None:
    class_name = str(obj.__class__)
    if class_name.__contains__('B'):
        raise ObjectException("You entered class B object")
    elif class_name.__contains__('A'):
        print(str(obj.value))
    else:
        print(obj)


if __name__ == '__main__':
    func(A(10))
    func(B(1.5))
    func("hello!")

