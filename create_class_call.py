class A(object):
    def __init__(self):
        pass
    def methoda(self):
        print("class A method")
        return "2"
    def methodac(self):
        data = self.methoda()
        print("class A method called and returned {}",format(data))
        data1 = B.methodb()
        print("class B{}",format(data1))

class B(object):
    def __init__(self):
        pass
    @staticmethod
    def methodb():
        print("class B method")
        return "3"
obj=A()
obj.methodac()