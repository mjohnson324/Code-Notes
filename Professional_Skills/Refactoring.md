When to:
    Testing, DRY, brittleness
    
How to:
    Rename, split, move (functions, method calls, classes)
    Simplify
    Redraw boundaries (in classes)

Python:
    Reference Effective Python?
    Variables and functions improve readability
    Classes improve testability

    Classes:
        Split classes using optional arguments to __init__
        Reference methods/fields between classes with @property (inheritance!)
        Recommend as closure in place of functional closures

Refactoring: DRY, YAGNI, Single Responsibility
-Refactor if you're copying code
-Refactor complex methods by breaking complex methods into separate ones
-Effective application of single responsibility requires deciding what to exclude in code