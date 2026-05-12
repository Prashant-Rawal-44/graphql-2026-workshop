# Step 1 — SOLUTION: Complete GraphQL Schema

## What we built
A fully typed SDL that replaces the implicit contracts of 5 REST endpoints.

## Key takeaways
- `!` = non-null (server guarantees this field will always have a value)
- `[Type!]!` = non-null array of non-null items
- Nested types (`Category.skills`) are resolved lazily — zero over-fetching
- One schema = one source of truth for your entire API surface

## Next Step
```bash
git checkout 02-queries
```
