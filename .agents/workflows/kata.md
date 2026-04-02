---
description: Starts a new TDD (Test-Driven Development) Kata exercise to practice the Red-Green-Refactor sequence.
---
# /kata Learning Workflow

**What is this?**
A "Kata" is a short, highly constrained programming exercise designed solely for practicing technique. When you trigger `/kata`, we will temporarily stop building real-world features and instead drill down on the exact mechanics of Test-Driven Development (TDD) and the Red-Green-Refactor loop.

**Why use it?**
To build muscle memory for testing *before* you code. When working on large applications, writing tests after you write the logic often leads to tightly coupled, hard-to-test code. This workflow forces an inherently testable design.

**How it works:**
1. We pick a small problem (like a calculator or string converter).
2. I strictly enforce that you write **only** a single failing test first (Red).
3. You write the ugliest possible code just to make it pass (Green).
4. We critique and refine the code according to our architecture principles (Refactor).

## Step 1: Assign the Kata
1. Acknowledge the `/kata` command.
2. If the user didn't specify a topic or language, ask them which programming language (e.g., Python, PowerShell, Go) they want to use, and if they have a specific Kata in mind.
3. If they don't have a Kata in mind, suggest three classic Katas (e.g., Roman Numeral converter, FizzBuzz, String Calculator).
4. Do NOT proceed until the user selects a Kata and language.

## Step 2: Set the Rules (The Red Phase)
1. Instruct the user to create a new directory for the Kata inside their workspace (e.g., `/python/katas/roman_numerals/`).
2. Instruct the user to definitively **NOT write any logic code yet**.
3. Instruct the user to write exactly **ONE failing test case** for the simplest possible scenario in their test file (e.g., `test_kata.py`), and to show it to you.
4. Do not provide the code yourself. Wait for their input.

## Step 3: Green Phase
1. After the user provides the failing test, verify it is truly minimal.
2. Instruct them to write merely enough logic code to make the test pass. The code can be 'ugly' or hard-coded at this stage. (KISS principle).
3. Do not proceed until they confirm the test is passing.

## Step 4: Refactor Phase
1. Critique the passing code against the TDD and design principles in `docs/architecture/04-TESTING_STRATEGIES.md` and `docs/architecture/01-CORE_PRINCIPLES.md`. Does it violate DRY? Can the names be improved? Is there unnecessary complexity?
2. Ask the user to refactor it.
3. Loop back to Step 2 for the next test case, progressively adding complexity.

## Step 5: Completion and Reflection
The kata is complete when the user has written **at least 5 test cases** covering the happy path *and* meaningful edge cases, and the final refactored code passes all tests.
1. Run the full test suite one final time to confirm all tests pass.
2. Ask the user to answer in their own words: **"What design principle did you learn or reinforce during this kata?"**
3. Optionally suggest a follow-up: a harder kata, or re-doing the same kata in a different language to compare idioms.
