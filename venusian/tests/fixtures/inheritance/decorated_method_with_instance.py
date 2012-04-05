from venusian.tests.fixtures.inheritance.decorated_method import Parent, Child
from venusian.tests.fixtures.inheritance.decorated_method_with_second_decorator import Child as Child2

class module(object):
    parent = Parent()
    child1 = Child()
    child2 = Child2()
