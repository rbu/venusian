from venusian.tests.fixtures import decorator

class Parent(object):
    @decorator()
    def parent(self):
        pass

class Child(Parent):
    pass
