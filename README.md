# Step 6 — SOLUTION: Scaling Patterns

## What we covered
- DataLoader eliminates N+1 problem — N DB calls become 1 per batch
- Query depth limits protect against attack queries
- Fragments make operations DRY and type-safe
- Apollo Federation enables team-level schema ownership
- APQ, @defer, response caching for production performance

## You now have a complete GraphQL 2026 picture
```
Schema Definition Language  →  Type safety, self-documentation
Queries with args           →  No over-fetching, no multiple round trips
Mutations returning data    →  Automatic cache updates
Subscriptions over WS       →  Real-time, replaces REST polling
DataLoader                  →  Eliminates N+1 performance problem
Federation                  →  Scale to multiple teams/services
```

## The complete app
```bash
git checkout main
# Full working app — all features enabled
cd server && npm run dev   # :4000
cd client && npm run dev   # :5173
```
