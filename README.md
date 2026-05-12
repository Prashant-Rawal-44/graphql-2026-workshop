# Step 6 — Scaling GraphQL in Production

## Goal
Learn the critical patterns for taking GraphQL from demo to production.
These are the topics that separate a toy GraphQL setup from a scalable system.

## Topics Covered

### 6a–6d. The N+1 Problem & DataLoader
The most common GraphQL performance pitfall.

**The problem:**
```
getCategories {     ← 1 query
  skills {          ← 4 queries (one per category)
    categoryInfo {  ← 20 queries (one per skill) = N+1!
    }
  }
}
```

**The fix — DataLoader:**
```js
// server/dataloader.js
import DataLoader from 'dataloader';

export function createCategoryLoader() {
  return new DataLoader(async (categoryNames) => {
    // ONE batch call instead of N individual calls
    return categoryNames.map(name => categories.find(c => c.name === name) || null);
  });
}
```

**Add to context in server/index.js:**
```js
expressMiddleware(server, {
  context: async () => ({ categoryLoader: createCategoryLoader() })
})
```

**Use in resolver:**
```js
Skill: {
  categoryInfo: (skill, _, { categoryLoader }) => categoryLoader.load(skill.category),
}
```

### Query Complexity & Depth Limits
Protect your API from malicious deeply nested queries.
See `server/complexity.js` for implementation notes.

### 6e–6f. Fragments — DRY operations
```graphql
fragment SkillFields on Skill { id title level xp isMastered ... }

query GetSkills { getSkills { ...SkillFields } }
mutation LevelUp { levelUpSkill(id: $id) { ...SkillFields } }
```

### Federation — Scaling teams (2026 trend)
With Apollo Federation, different teams own different parts of the schema:
```
Team Frontend  → skills subgraph
Team Platform  → categories subgraph
Team AI        → recommendations subgraph
                   ↓
           Apollo Router (gateway)
                   ↓
           One unified supergraph
```

### Other 2026 Production Patterns
| Pattern | What it solves |
|---|---|
| Persisted Queries (APQ) | CDN caching + security (no arbitrary queries) |
| @defer / @stream | Stream large payloads incrementally |
| Response Cache plugin | TTL-based server-side caching |
| Cursor pagination | Efficient large list navigation |
| GraphQL Codegen | Auto-generate TypeScript types from schema |

## Run and verify DataLoader is working
```bash
# In server/index.js add this to see batching in action:
# context: async () => {
#   const loader = createCategoryLoader();
#   loader._batchScheduleFn = () => console.log('DataLoader batch fired!');
#   return { categoryLoader: loader };
# }
```

## Next Step
```bash
git checkout 06-scaling-solution   # See the answer
```
