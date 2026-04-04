# Core Architectural and Design Principles

This document acts as an explicit reference guide for the structural principles expected when developing code in this workspace.

## SOLID Principles
A standard framework for object-oriented design intended to make software structures more understandable, flexible, and maintainable.
- **Single Responsibility Principle (SRP):** A class or module should have one, and only one, reason to change. Meaning, it should only have one job.
- **Open/Closed Principle (OCP):** Objects or entities should be open for extension but closed for modification. You should be able to add new functionality without altering existing code.
- **Liskov Substitution Principle (LSP):** Let `q(x)` be a property provable about objects of `x` of type `T`. Then `q(y)` should be provable for objects `y` of type `S` where `S` is a subtype of `T`. In simpler terms, subclasses should be substitutable for their base classes.
- **Interface Segregation Principle (ISP):** A client should never be forced to implement an interface that it doesn't use, or clients shouldn't be forced to depend on methods they do not use.
- **Dependency Inversion Principle (DIP):** Entities must depend on abstractions, not on concretions. High-level modules should not depend on low-level modules; both should depend on abstractions.

## DRY (Don't Repeat Yourself)
Every piece of knowledge must have a single, unambiguous, authoritative representation within a system. 
**Tutor's Note:** When you find yourself copy-pasting code, extract it into a function, module, or common utility. This prevents bugs where you fix an error in one place but forget to update the copy.

## KISS (Keep It Simple, Stupid)
Systems work best when they are kept simple rather than made complex. Simplicity guarantees clarity and significantly reduces maintenance overhead. Don't add clever hacks or hyper-compact code if it damages readability.

## YAGNI (You Aren't Gonna Need It)
Always implement things when you *actually* need them, never when you just foresee that you *might* need them.
**Tutor's Note:** Over-engineering is a common trap. Wait until the business requirement explicitly asks for a feature before building the infrastructure for it.

## Cohesion and Coupling
- **Maximize Cohesion:** Ensure that the code within a module or class is highly related and focused on a single task.
- **Minimize Coupling:** Ensure that the dependencies *between* different modules are as loose and isolated as possible. Change in one module should rarely force a change in another.

## Context and Boundaries 
- **Law of Demeter (LoD):** The principle of least knowledge. An object should only interact with its immediate friends, not strangers. Do not write "train wreck" code (`object.getChild().getService().doAction()`).
- **Separation of Concerns (SoC):** Divide the system into distinct sections, such that each section addresses a separate concern. Layered architectures (like MVC or Clean Architecture) naturally enforce SoC.
