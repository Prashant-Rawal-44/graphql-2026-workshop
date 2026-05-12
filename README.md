# Step 2 — Implement GraphQL Queries

## Goal
Wire up resolvers on the server and `useQuery` hooks on the client.
**This is where GraphQL's "ask for exactly what you need" comes alive.**

## Your Tasks

### Server (server/resolvers.js)

#### 2a. getSkills with filtering
```js
getSkills: (_, args = {}) => {
  let result = [...skills];
  if (args.category) result = result.filter(s => s.category === args.category);
  if (args.minLevel) result = result.filter(s => s.level >= args.minLevel);
  if (args.tags?.length) result = result.filter(s => args.tags.some(t => s.tags.includes(t)));
  return result;
},
```
**Why this is better than REST:** One query with args replaces:
`GET /skills`, `GET /skills?category=Backend`, `GET /skills?minLevel=5&tags=react` etc.

#### 2b. getSkillById
```js
getSkillById: (_, { id }) => skills.find(s => s.id === id),
```

#### 2c. getCategories
```js
getCategories: () => categories,
```

#### 2d. getDashboardStats — one query, aggregated server-side
```js
getDashboardStats: () => {
  const mastered = skills.filter(s => s.isMastered).length;
  const totalXP = skills.reduce((sum, s) => sum + s.xp, 0);
  const avgLevel = skills.reduce((sum, s) => sum + s.level, 0) / skills.length;
  const breakdown = categories.map(cat => {
    const cs = skills.filter(s => s.category === cat.name);
    return { category: cat.name, count: cs.length, avgLevel: cs.reduce((a,s)=>a+s.level,0)/cs.length, totalXP: cs.reduce((a,s)=>a+s.xp,0), color: cat.color };
  });
  return { totalSkills: skills.length, masteredSkills: mastered, totalXP, avgLevel, categoryBreakdown: breakdown };
},
```
**Why this matters:** REST would need you to hit 3 endpoints and aggregate on the client.

#### 2e. Field-level resolvers (GraphQL superpower!)
```js
Skill: {
  categoryInfo: (skill) => categories.find(c => c.name === skill.category),
},
Category: {
  skills: (cat) => skills.filter(s => s.category === cat.name),
  skillCount: (cat) => skills.filter(s => s.category === cat.name).length,
  avgLevel: (cat) => { const cs = skills.filter(s => s.category === cat.name); return cs.reduce((a,s)=>a+s.level,0)/cs.length; },
},
```
**Why this matters:** These only run if the client requests those fields. Zero wasted computation.

### Client (client/src/App.jsx)

#### 2f. Wrap with ApolloProvider
```jsx
export default function AppWithProvider() {
  return (
    <ApolloProvider client={client}>
      <App />
    </ApolloProvider>
  );
}
```

## Verify in GraphiQL
Open http://localhost:4000/graphql and run:
```graphql
query {
  getSkills(category: "Backend") {
    title level xp tags
  }
  getDashboardStats {
    totalSkills totalXP avgLevel
    categoryBreakdown { category count avgLevel }
  }
}
```
Notice: **One request, two operations, exactly the fields you asked for.** With REST you'd need 2-3 requests.

## Next Step
```bash
git checkout 02-queries-solution   # See the answer
git checkout 03-mutations          # Next task
```
