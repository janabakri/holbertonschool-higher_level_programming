Python OOP Exercises – Advanced Concepts
A focused set of Python exercises that explore advanced Object-Oriented Programming (OOP) patterns and design techniques: Abstract Base Classes (ABC), Duck Typing, Subclassing built-ins, Method Overriding, Multiple Inheritance, and Mixins.

Learning Goals
By the end of this project, you should be comfortable with:

Abstract Classes (ABC)

Defining common contracts using ABC and @abstractmethod
Preventing instantiation of incomplete base classes
Enforcing required behavior in subclasses
Duck Typing

Designing code around capabilities rather than explicit types
Writing polymorphic functions that work with any compatible object
Subclassing Standard Types

Extending core types like list, dict, and iterators
Overriding methods while preserving original behavior
Method Overriding

Customizing inherited behavior safely
Using super() when parent behavior should remain part of the flow
Multiple Inheritance

Building classes from more than one parent
Understanding Python’s Method Resolution Order (MRO)
Avoiding and resolving conflicts between parent implementations
Mixins

Creating small, reusable behavior units
Composing features across unrelated classes
Keeping inheritance hierarchies shallow and maintainable
Project Structure
python-abc/ ├── task_00_abc.py # Abstract Base Classes – example hierarchy ├── task_01_duck_typing.py # Duck Typing – behavior-based polymorphism ├── task_02_verboselist.py # Subclassing – list with extra notifications ├── task_03_countediterator.py # Iterator subclassing – iteration counter ├── task_04_flyingfish.py # Multiple Inheritance – FlyingFish + MRO ├── task_05_dragon.py # Mixins – Dragon with multiple abilities └── README.md

Author
Jana AL/Bakri
Holberton School Project
