# Testing Strategies

Automated tests are the bedrock of confidence when rebuilding an architecture. When tests are fast, isolation is pristine, and developers push code without fear.

## The Testing Pyramid
Software must not rely heavily on full end-to-end integration manual tests. Structure your test suite according to the pyramid:
- **Base (Unit Tests):** The vast majority of tests. Fast, strictly isolated, focused on pure logic execution.
- **Middle (Integration Tests):** Connecting code components to ensure boundaries hold. Tests API routes hitting databases.
- **Top (E2E Tests):** Very few. Slow and brittle UI/Browser automation validating the absolute final end-user experience on critical paths.

## Test-Driven Development (TDD)
The act of writing the verification before the logic. TDD enforces an inherently testable design, because "testability" is prioritized immediately.
- **Red:** Write a test that fails (since there is no code yet) testing a small slice of business logic.
- **Green:** Implement purely the absolute minimum code required to make the test pass. (EAFP, KISS)
- **Refactor:** Now you have the safety net of a passing test, adjust your solution for readability, structure, and abstraction (DRY).

## Behavior-Driven Development (BDD)
A superset of TDD. Drive tests not purely logically ("test function returns 5"), but by expected business requirement behavior ("when user is inactive, account is locked"). This helps shape testing variables into Ubiquitous language.

## Test Boundaries and Doubles
When working in a truly decoupled Clean Architecture, business logic shouldn't inherently know about an external Database, SMTP server, or REST API. That implies it shouldn't be tested against one. 
**Test Doubles** allow isolation:
- **Dummy:** Objects passed around but never utilized (filler arguments).
- **Fake:** An object that has a working implementation, but takes shortcuts prohibiting production use (in-memory databases).
- **Stub:** An object providing canned answers rigidly defined for the testing scenario.
- **Spy:** A stub that records information about how it was called (e.g., tallying the number of times `log()` was invoked).
- **Mock:** Objects pre-programmed with expectations acting as strict verifiers to whether interacting calls arrived properly.
