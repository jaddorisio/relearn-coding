# Go (Golang) Software Architecture Specifics

Go is both simple and opinionated. It does not have classes, inheritance, or traditional OOP. Instead, it uses composition, interfaces, and explicit error handling. Below are the core architectural and coding patterns to apply to Go projects.

## 1. Embrace Go's Design Philosophy
- **Do NOT force OOP paradigms into Go.** Go does not support traditional C++/Java-style inheritance. Do not try to recreate class hierarchies. Instead, use composition (embedding structs) and interfaces.
- **Simplicity is a feature.** Go's standard library is extensive and well-designed. Prefer it over third-party packages unless you have a clear, justified need.

## 2. Project Structure
- **`internal/` Directory:** Go enforces a strict visibility rule where code placed inside an `internal/` directory can only be imported by packages within that same directory tree. Use this heavily to protect domain logic from being accidentally exposed in the public API—a natural fit for DDD-style boundary enforcement.
- **`pkg/` Directory:** A community convention indicating code that is safe for external consumption. Use it for utilities and shared libraries you intend others to import.
- **`cmd/` Directory:** Place application entry points here (e.g., `cmd/myapp/main.go`). Each subdirectory represents a separate executable.

## 3. Interface Design
- **Define interfaces where they are used, not where they are implemented.** This is the opposite of Java. The *consumer* of a dependency defines the interface it needs, making mocking and testing trivial.
- **Prefer small, single-method interfaces.** Name them with an `-er` suffix (e.g., `Reader`, `Writer`, `Validator`). The smaller the interface, the easier it is to compose.
- **Do NOT define interfaces before they are actually needed.** Wait until you have a concrete use case (e.g., needing to swap implementations or mock in tests). This directly applies YAGNI.

## 4. Naming Conventions
- **Variable names should be short,** especially when used close to their declaration. Use `i` for an index, `r` for a reader, `ctx` for context. Longer names are reserved for exported identifiers.
- **Package names must be short, lowercase, and a single word.** Do not use underscores or camelCase in package names.
- **Do NOT prefix type names with the package name.** Inside the `xml` package, name the interface `Reader`, not `XMLReader`. Callers already write `xml.Reader`.
- **Getters should NOT be prefixed with `Get`.** A method returning `owner` should be called `Owner()`, not `GetOwner()`. Setters should use `SetOwner()`.

## 5. Context Propagation
- **Always pass `context.Context` as the very first argument** to functions, especially those doing I/O, network calls, or database queries. Name it `ctx`.
- **Never store `context.Context` as a field inside a struct.** This causes context leakage and unpredictable timeout behavior. Pass it explicitly through each function call in the chain.

## 6. Error Handling
- **Errors are values, not exceptions.** Go deliberately avoids `try/catch`. Functions return an `error` as the last return value, and the caller is expected to handle it immediately with `if err != nil`.
- **Only use `panic` in truly exceptional cases** where the application cannot safely continue (e.g., out of memory, impossible state violations during initialization). Never use `panic` for normal control flow.
- **Error strings should be lowercase** and should not end with punctuation. They are often wrapped by callers (e.g., `fmt.Errorf("reading config: %w", err)`).
- **Use `%w` for error wrapping** to preserve the error chain for `errors.Is()` and `errors.As()` inspection.

## 7. CQRS Adaptation in Go
When applying Command Query Responsibility Segregation:
- **Commands (state-modifying methods)** should return only an `error` or `nil`.
- **Queries (data-reading methods)** should NOT modify the database or the receiver struct. They return the requested data and an `error`.

## 8. Concurrency
- **Goroutines and channels are Go's concurrency primitives.** Do not reach for mutexes first—prefer communicating via channels.
- **"Don't communicate by sharing memory; share memory by communicating."** This is the Go proverb that underpins all concurrency design.
- **Always ensure goroutines can be stopped.** Use `context.Context` with cancellation to prevent goroutine leaks. A function that spawns a goroutine should provide a mechanism to shut it down gracefully.
