# sample_project.py
from my_interface import ParentInterface

class ChildClass(ParentInterface):
    def _hidden_method(self):
        print("This is a hidden method")

    def public_method(self):
        print("This is a public method")

# Test the child class
child = ChildClass()
child.public_method()  # Accessible
# child._hidden_method()  # Accessible but discouraged
