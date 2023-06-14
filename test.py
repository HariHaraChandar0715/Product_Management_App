class A():
    def __init__(self, name):
        self.name = name


class B():
    def __init__(self) -> None:
        self.names = []

    def addname(self, a):
        self.names.append(a)

    def getname(self):
        return self.names


# driver code


b = B()
b.addname(A("Hari"))
b.addname(A("manoj"))
lst = b.getname()
for i in lst:
    print(i.name)
