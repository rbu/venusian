from venusian.tests.fixtures import decorator
from venusian.tests.fixtures.inheritance.decorated_method import Parent

class Child(Parent):
    @decorator()
    def child(self):
        pass
