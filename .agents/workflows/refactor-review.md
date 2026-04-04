---
description: Triggers a comprehensive architectural critique of an existing piece of code, driving structural refactoring.
---
# /refactor-review Learning Workflow

**What is this?**
An aggressive, structural code review session. When you trigger `/refactor-review`, I will use our established textbook (`docs/architecture/`) as an ironclad rubric to mercilessly (but constructively) critique an old script you wrote.

**Why use it?**
To break old habits. Often, scripts start clean and slowly morph into structural spaghetti. This workflow teaches you how to identify specific "code smells" (like deep nesting, gigantic classes, or magic strings) and translates abstract principles (SOLID, DRY) into practical, line-by-line surgical repairs.

**How it works:**
1. You provide me a path to code you want evaluated.
2. I map out all architectural violations found in it, ranked by severity.
3. Rather than fixing it for you, I guide you through a "Guided Demolition"—challenging you to extract, decouple, and refactor the code piece by piece.

## Step 1: Identify the Target
1. Ask the user to provide the absolute path or relative path to a specific file or folder containing code they wrote previously they would like to review.
2. Wait for them to provide the file path. Use the `view_file` tool to read the code.

## Step 2: The Assessment
1. Analyze the script extensively against the knowledge documents located in `docs/architecture/`.
2. Do not just look for syntactic errors. Look for architectural "smells," categorized by severity:

**🔴 Critical — Structural failures that prevent maintainability:**
- Procedural spaghetti (no functions, classes, or boundaries)
- Massive classes or functions doing too much (SRP violations)
- Tight coupling / Law of Demeter violations (`object.getChild().getService().doAction()`)
- Missing error handling boundaries entirely

**🟡 Major — Significant design weaknesses:**
- Magic strings, magic numbers, or duplicated code blocks (DRY violations)
- Deep nesting (more than 3 levels of indentation)
- Missing input validation on external data
- Mutable default arguments in Python function definitions
- Missing `if __name__ == "__main__":` guard in Python scripts
- God objects that know about everything in the system

**🟢 Minor — Polish and idiom improvements:**
- Non-idiomatic naming (not PEP 8, etc.)
- Missing type hints or parameter validation attributes
- Overly clever or compact code that sacrifices readability (KISS)
- Missing docstrings

3. Present a formatted, severity-ranked list of observations to the user, referencing the exact architectural principle names and the relevant `docs/architecture/` file.

## Step 3: Guided Demolition
1. Do not rewrite the code for the user.
2. Start with the **most severe (🔴 Critical)** violation from the list.
3. Ask the user a targeted question: e.g., "How could we extract this logic to decouple it based on the Single Responsibility Principle?"
4. Wait for the user to write the structural change, and critique their pull-request-style update before moving to the next violation.
5. Repeat for each violation, working down from Critical → Major → Minor.

## Step 4: Before/After Reflection
1. After addressing at least the Critical and Major violations, ask the user to re-read both the original and refactored versions side by side.
2. Ask them: **"In your own words, why is the new version better? What specific principle made the biggest difference?"**
3. Optionally suggest running the refactored code through a linter or test suite to verify nothing was broken.
