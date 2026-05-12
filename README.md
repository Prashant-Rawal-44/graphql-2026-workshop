# Step 2 — SOLUTION: Queries Working

## What we proved
- `getSkills` with filter args replaces 4+ REST routes
- `getDashboardStats` aggregates server-side — 1 query vs 3 REST calls
- Field-level resolvers (`Category.skills`) only run when requested
- Apollo Client `useQuery` hook fetches + normalizes data automatically

## Test in GraphiQL
```graphql
# Single request — two operations, exactly what the client needs
query Dashboard {
  getDashboardStats { totalSkills masteredSkills totalXP avgLevel }
  getSkills(category: "AI/ML") { title level xp }
}
```

## Next Step
```bash
git checkout 03-mutations
```
