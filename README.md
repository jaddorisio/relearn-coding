# Relearning Coding with PowerShell and Python

This repository is my hands-on workspace for rebuilding programming skill through practical exercises, small projects, and notes.

The main focus is:

- PowerShell for real-world automation and operational scripting
- Python for transferable programming fundamentals and general-purpose tooling
- Learning by building, testing, debugging, and reviewing code

## Why this repo exists

I mainly use PowerShell at work, but I want stronger programming fundamentals that transfer across languages and environments.

This repo is meant to help me:

- relearn core coding concepts
- practice writing clean, maintainable scripts
- turn course material into real exercises
- build habits for verifying AI-generated code instead of trusting it blindly
- create a body of examples I can reuse for automation work

## Learning approach

The goal is not just to finish exercises. The goal is to understand patterns that keep showing up in real work.

That means this repo will emphasize:

- variables, control flow, functions, and data structures
- file handling, parsing, APIs, and automation workflows
- input validation and error handling
- debugging and testing
- comparing how the same idea looks in PowerShell and Python

## Planned structure

As the repo grows, it will likely use a structure like this:

```text
/
  README.md
  AGENTS.md         # AI Tutor configuration
  .agents/          # Interactive pedagogical AI workflows
  docs/             # Architectural reference manuals
  powershell/
    [Book Name]/
      [Exercise Name]/
  python/
    [Book Name]/
      [Exercise Name]/
```

This structure is intentionally simple, organized by `Language > Book > Exercise`. For example, `python/sample-book/sample-exercise/hello.py`.

## Architecture and Learning Framework

To ensure all code strictly adheres to professional standards from the beginning, this workspace is equipped with an integrated pedagogical framework:

- **Architecture Knowledge Base (`docs/architecture/`)**: A detailed encyclopedia covering core principles (SOLID, DRY), Python/PowerShell idioms, system design (failure handling), and testing strategies (TDD).
- **Interactive AI Workflows (`.agents/workflows/`)**: Powered by an integrated AI tutor mapping directly to the architecture docs. These include slash-commands designed to force good habits:
  - `/kata`: Practice Test-Driven Development (Red-Green-Refactor).
  - `/design-stub`: Practice Top-Down Object-Oriented Design without writing logic first.
  - `/refactor-review`: Identify weaknesses in old scripts and successfully repair architectural "smells".

The agent's personality and contextual rules are explicitly defined in `AGENTS.md`.

## How this repo will be used

This repo will contain a mix of:

- short exercises focused on one concept
- worked examples with explanation
- small scripts that solve practical problems
- notes about what was learned and what was confusing
- solutions derived from online course work, adapted into personal practice

When adding new work, the default approach should be:

1. Define the problem in practical terms.
2. Break it into small steps.
3. Write the smallest clean solution.
4. Test that it actually works.
5. Review what concept the exercise was really teaching.

## Initial topic roadmap

Good starting topics for this repo could include typical learning paths:

1. Fundamentals (Variables, Conditionals, Loops, Functions)
2. Data Structures (Collections, Hashmaps, Dictionaries)
3. Input/Output (File reading, API interactions)
4. Application/Scripting Structure (Reusable modules, Parsing)
5. Practical Projects (Building tools, Scripting workflows)

## Working rules

To keep this repo useful over time:

- prefer readable code over clever code
- avoid unnecessary dependencies
- include comments only when they explain non-obvious logic
- validate inputs when scripts interact with files, users, or external systems
- treat verification as part of the exercise, not an optional extra

## Next steps

The next useful additions would be:

1. Create the top-level `powershell/` and `python/` folders.
2. Add one beginner-friendly PowerShell exercise and one equivalent Python exercise.
3. Create a simple template for future exercises so each one has the same shape.

---

This repo starts small on purpose. The value will come from steady accumulation of clear examples, corrected mistakes, and reusable patterns.
