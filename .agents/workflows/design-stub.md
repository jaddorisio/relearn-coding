---
description: Triggers a top-down architectural design session where we stub out interfaces and classes before writing execution logic.
---
# /design-stub Learning Workflow

**What is this?**
This workflow acts as an architectural whiteboard session. When you trigger `/design-stub`, I will actively prevent you from writing any actual business logic, algorithms, or functional code. Instead, we perform "Top-Down Design," focusing entirely on defining system boundaries, models, and interfaces.

**Why use it?**
To cure the habit of jumping straight into coding without a plan. By only allowing classes, empty method signatures (stubs), and print statements, you are forced to think about the *relationships* between objects (Coupling, Single Responsibility, Law of Demeter) before getting distracted by the implementation details.

**How it works:**
1. You propose a system (like a shopping cart or an ATM).
2. You map out the objects and their methods (the "nouns" and "verbs").
3. We critique the structural design.
4. Finally, you write a `main()` runner that strings together empty print statements to prove the flow of data makes logical sense.

## Step 1: Feature Idea
1. Ask the user what kind of realistic system they want to model (e.g., an ATM machine, an e-commerce cart, a deck of cards).
2. Wait for their response.

## Step 2: Enforce the Stub Rule
1. State the golden rule: **"We will not write any functional logic. We will only write classes, function definitions (stubs), and print statements."**
2. Ask the user to think about the primary "Actors" or "Nouns" in the system. Which core objects need to exist?

## Step 3: Architecture Critiquing
1. As the user creates the files and stubs out the initial classes, evaluate their design strictly against the principles found in `docs/architecture/01-CORE_PRINCIPLES.md`.
2. Check for Separation of Concerns: Is one class doing too much (violating SRP)? Are they passing the whole system object down the chain (violating the Law of Demeter)?
3. If issues are found, gently prompt the user to rethink which object should own the responsibility.

## Step 4: Flow Simulation
1. Once the stubs are refined, ask the user to write a `main()` function that instantiates the objects and calls their dummy methods.
2. Have the user run the script and verify that the `print()` statement output reflects a clean, logical sequence of events.
