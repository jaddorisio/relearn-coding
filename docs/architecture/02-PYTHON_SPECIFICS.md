# Python Software Architecture Specifics

Python is unique. It relies heavily on convention and idiom rather than strict compilation rules. Below are the core architectural and coding patterns you should apply to your Python projects.

## 1. Pythonic Code Idioms
- **EAFP > LBYL:** Favor "Easier to Ask Forgiveness than Permission" over "Look Before You Leap." Instead of wrapping code in multiple `if` statements to verify the state, just execute the code within a `try/except` block and handle the resulting error natively.
- **Context Managers:** Any operation that involves acquiring and releasing resources (like file I/O, database sessions, thread locks) MUST be wrapped in a `with` statement.
- **Comprehensions:** Use list, dictionary, and set comprehensions for mapping/filtering sequences rather than imperative `for` loops. They perform faster and reduce boilerplate.
- **Mutable Default Arguments:** **Never** define a function with a mutable object type like `list` or `dict` as a default. Since defaults are evaluated once at definition time, mutating it will persist across multiple function calls. Use `None`.

## 2. Object-Oriented Patterns
- **Access Control:** Python lacks `public/private/protected` keywords. 
  - Use a single underscore (`_variable`) to denote an internal, protected helper meant for internal API use. 
  - **Do not** use double-underscores (`__variable`) for privacy; this invokes name-mangling meant to prevent subclass namespace collisions.
- **Properties:** Avoid writing Java-style `get_value()` and `set_value()` methods. Expose the variable directly (`obj.value`). If later you decide you need a read-only variable or validation upon assignment, convert it to an `@property` decorator smoothly.
- **Dataclasses:** Define purely data-holding classes using the `@dataclass` decorator to vastly reduce `__init__`, `__repr__`, and `__eq__` boilerplate.
- **Extend Collections Built-ins:** Do not subclass the pure C-level types like `dict` or `list`, as their inner C methods completely ignore overriding. Subclass from the standard library: `collections.UserDict`, `collections.UserList`, `collections.UserString`.

## 3. Structural Patterns
- **Clean Architecture:** Use Python's folder structure (packages/modules) to separate your core application layer (`domain/`) from your external plugins (`adapters/`, `frameworks/`). 
- **Singleton Avoidance:** The Singleton class pattern is an anti-pattern in Python. Because Python modules inherently act as singletons (they are processed once at interpretation), global state can just be held at the module level.
- **Duck Typing & Protocols:** Do not implement large trees of `Abstract Base Classes` just to enforce typing. Use `typing.Protocol` (duck typing) so that `mypy` structural type checks can ensure objects have the correct methods without forcing them to inherit a rigid hierarchy.
- **Preventing Execution:** All script logic must be guarded within an `if __name__ == "__main__":` block to prevent arbitrary execution upon import elsewhere.
- **Wildcard Imports are Banned:** Never utilize `from module import *`. It destroys namespace clarity and prevents simple static analysis.
