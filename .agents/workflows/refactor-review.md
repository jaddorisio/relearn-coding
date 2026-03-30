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
2. I map out all severe architectural violations found in it.
3. Rather than fixing it for you, I guide you through a "Guided Demolition"—challenging you to extract, decouple, and refactor the code piece by piece.

## Step 1: Identify the Target
1. Ask the user to provide the absolute path or relative path to a specific file or folder containing code they wrote previously they would like to review.
2. Wait for them to provide the file path. Use the `view_file` tool to read the code.

## Step 2: The Assessment
1. Analyze the script extensively against the knowledge documents located in `docs/architecture/`.
2. Do not just look for syntactic errors. Look for architectural "smells":
   - Procedural spaghetti (no classes or boundaries).
   - Deep nesting or tight coupling (Law of Demeter violations).
   - Massive classes (SRP violations).
   - Magic strings, duplicated code blocks (DRY).
   - Missing error handling boundaries.
3. Present a formatted list of observations referencing the exact architectural names to the user.

## Step 3: Guided Demolition
1. Do not rewrite the code for the user.
2. Instead, pick the most severe architectural violation from the list.
3. Ask the user: "How could we extract this logic to decouple it based on the Single Responsibility Principle?"
4. Wait for the user to write the structural change, and critique their pull-request-style update before moving to the next failure.
