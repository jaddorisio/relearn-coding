# Classical Design Patterns (Gang of Four)

Design patterns are reusable solutions to commonly occurring problems in software design. They are not code snippets—they are templates for *how* to structure relationships between objects. Understanding them helps you recognize structural choices in existing codebases and communicate design decisions with other developers.

**Tutor's Note:** Do not force-fit patterns into simple code. Patterns add complexity. Apply them only when the problem they solve actually exists in your project (YAGNI). These are "unlocked" when you reach OOP and multi-class exercises.

## Creational Patterns
These patterns deal with object creation, abstracting the instantiation process.

### Factory / Abstract Factory
- **What:** Encapsulates object creation logic behind a method or class. The caller requests an object by *type* or *configuration* without knowing the exact class being instantiated.
- **When to use:** When a function needs to create different objects based on input, and you want to avoid a giant `if/elif/else` chain of constructors.
- **Python note:** Often implemented as a simple function returning different class instances.
- **Go note:** Use constructor functions like `NewValidator(config)` returning an interface type.

### Singleton
- **What:** Restricts a class to a single instance throughout the application.
- **⚠️ Considered an anti-pattern** in most modern contexts. Makes testing extremely difficult because global state cannot be easily swapped.
- **Python note:** Modules already act as singletons. Just use module-level variables.
- **Go note:** Use `sync.Once` if truly needed, but prefer dependency injection.

## Structural Patterns
These patterns deal with composing classes and objects to form larger structures.

### Adapter
- **What:** Bridges the gap between two incompatible interfaces. Translates requests from one system into the format expected by another.
- **When to use:** Integrating a third-party library whose API doesn't match your internal interfaces. Common in Clean Architecture at the "adapters" layer.

### Decorator
- **What:** Dynamically wraps an object to extend or modify its behavior without changing its interface. Each decorator adds one responsibility.
- **When to use:** Adding cross-cutting concerns (logging, caching, retries) without modifying the original code. Follows the Open/Closed Principle.
- **Python note:** Python's `@decorator` syntax is a language-level implementation of this pattern.

### Façade
- **What:** Provides a simplified, high-level interface that hides the complexity of a larger subsystem.
- **When to use:** When a client needs to interact with a complex system but only cares about a small subset of its capabilities. Reduces coupling.

### Composite
- **What:** Treats individual objects and hierarchical compositions of objects uniformly. Both "leaf" and "branch" nodes implement the same interface.
- **When to use:** Tree-like data structures (file systems, organizational hierarchies, UI component trees).

## Behavioral Patterns
These patterns deal with how objects communicate and distribute responsibility.

### Strategy
- **What:** Encapsulates different algorithms behind a common interface, allowing them to be swapped at runtime. The *context* object delegates to a *strategy* object.
- **When to use:** When you have multiple ways to perform the same operation (e.g., different sorting algorithms, different pricing rules, different authentication methods).
- **Python note:** Often implemented with functions/callables instead of full classes, since Python treats functions as first-class objects.

### Observer (Publisher-Subscriber)
- **What:** Defines a one-to-many relationship where state changes in a "publisher" automatically notify all "subscribers."
- **When to use:** Event systems, UI update notifications, decoupling modules that need to react to changes without tight coupling.
- **Connection to EDA:** This is the local, in-process version of Event-Driven Architecture.

### Command
- **What:** Encapsulates a request as an object, allowing you to parameterize operations, queue them, log them, or support undo.
- **When to use:** Implementing undo/redo, task queues, or macro recording systems.

### Template Method
- **What:** Defines the skeleton of an algorithm in a base class but lets subclasses override specific steps.
- **When to use:** When multiple classes share the same overall workflow but differ in specific details.
- **Go note:** Achieved through composition and interfaces rather than inheritance.

### State
- **What:** Allows an object to alter its behavior when its internal state changes. Each state is represented as a separate object implementing a shared interface.
- **When to use:** Objects with clearly defined states and transitions (e.g., order processing: Pending → Approved → Shipped → Delivered).
