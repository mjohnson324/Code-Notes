-Goal: Simplify interfaces

Types:
1. Class- templates for objects nesting state and behavior
2. Prototype- Behavior defined for individual objects

Key Terms:
Serialization- Saving/transferring objects into storage
Inheritance- How classes apply code defined by other classes
Polymorphism- When subclasses override inherited methods in a shared interface
	Generic Code- Code written to be polymorphic. Allows writing code-as-a-concept to substantiate in subclasses
Encapsulation- Bundling of data with methods operating on that data
Duck Typing- Classes that use the same method names but are otherwise unrelated (if it seems like a duck you can treat it like one)
Mutex/Lock- Mutual Exclusion Object: object used when multiple threads share the same resource to prevent problems related to concurrent programming
Nonce- A number that may only be used once
Destructuring- When variables are assigned to object attributes, permitting multivariable assignment

Law of Demeter: minimize method-chaining to maintain readability via delegation

-Avoid hardcoding exceptions at the outset. Exceptions are difficult to predict

Object Relational Mapping- Applying OOP to database interactions
-Simplifies/codifies the process of accessing databases
-Classes get tables
-Instances get rows
-Attributes get columns
