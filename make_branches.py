"""
Creates all 13 workshop branches with README.md step guides for each.
Branch map:
  starter
  01-schema           / 01-schema-solution
  02-queries          / 02-queries-solution
  03-mutations        / 03-mutations-solution
  04-subscriptions    / 04-subscriptions-solution
  05-rest-vs-graphql  / 05-rest-vs-graphql-solution
  06-scaling          / 06-scaling-solution
"""

import subprocess, os, shutil, textwrap

ROOT = '/Users/prashant/Desktop/Project-graphQL'
os.chdir(ROOT)

def git(*args):
    r = subprocess.run(['git'] + list(args), capture_output=True, text=True)
    print(f'  git {" ".join(args[:3])} -> {r.returncode}')
    return r

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w') as f:
        f.write(textwrap.dedent(content).lstrip())

# ── Ensure we are on main and everything is committed ─────────────────────────
git('checkout', 'main')
git('add', '-A')
git('commit', '-m', 'chore: clean up rebuild scripts', '--allow-empty')

# ── Delete old branches ────────────────────────────────────────────────────────
old = ['starter','01-schema','01-schema-solution','02-query','02-query-solution',
       '03-mutation','03-mutation-solution','04-subscription','04-subscription-solution',
       '01-schema-task','02-queries','02-queries-solution','03-mutations',
       '03-mutations-solution','04-subscriptions','04-subscriptions-solution',
       '05-rest-vs-graphql','05-rest-vs-graphql-solution','06-scaling','06-scaling-solution']
for b in old:
    git('branch', '-D', b)

# ════════════════════════════════════════════════════════════════════════════════
# BRANCH 1: starter
# ════════════════════════════════════════════════════════════════════════════════
git('checkout', '-b', 'starter')

write('server/schema.js', """\
import { gql } from 'graphql-tag';

// ── STARTER BRANCH ─────────────────────────────────────────────────────────────
// The server is just a bare Express app with no GraphQL yet.
// You can compare this with the REST endpoints below.
// Goal: understand what REST gives you — and what it lacks.

export const typeDefs = gql`
  type Query {
    hello: String
  }
`;
""")

write('server/resolvers.js', """\
// Bare starter resolvers — just a hello world
export const resolvers = {
  Query: {
    hello: () => 'Hello from GraphQL! Now lets build something real.',
  },
};
""")

write('README.md', """\
# 🚀 GraphQL in 2026 — Workshop

## Starter Branch

This is where we begin. The server runs Express with the barest GraphQL setup.

### Run the project
```bash
# Terminal 1 — Server
cd server && npm install && npm run dev
# → http://localhost:4000/graphql

# Terminal 2 — Client
cd client && npm install && npm run dev
# → http://localhost:5173
```

### What's here
- Express server on port 4000
- Apollo Server 4 with a single `hello` query
- Static skill data in `server/data/skills.js`
- REST comparison endpoints at `/rest/skills`, `/rest/categories`, `/rest/stats`

### Try these REST calls (open in browser)
```
http://localhost:4000/rest/skills        ← needs 1 round trip
http://localhost:4000/rest/categories    ← needs another round trip
http://localhost:4000/rest/stats         ← needs a 3rd round trip!
```

### Discussion: What's wrong with REST here?
1. **Over-fetching** — `/rest/skills` returns ALL fields even if you only need `title` and `level`
2. **Multiple round trips** — you need 3 separate HTTP calls just for the dashboard
3. **No real-time** — you'd have to poll every few seconds
4. **No type safety** — nothing stops you returning wrong data shapes

### Next Step
```bash
git checkout 01-schema
```
""")

git('add', '-A')
git('commit', '-m', 'starter: bare Express + hello GraphQL + REST comparison routes')

# ════════════════════════════════════════════════════════════════════════════════
# BRANCH 2: 01-schema (TASK)
# ════════════════════════════════════════════════════════════════════════════════
git('checkout', 'main')
git('checkout', '-b', '01-schema')

write('server/schema.js', """\
import { gql } from 'graphql-tag';

// ── STEP 1: Define your GraphQL Schema ─────────────────────────────────────────
// The schema is the CONTRACT between client and server.
// Unlike REST where the shape is implicit, here it is EXPLICIT and self-documenting.
//
// YOUR TASKS:
//   1a. Define a Skill type with fields: id, title, category, level, maxLevel,
//       isMastered, description, tags (array), xp
//
//   1b. Define a Category type with: id, name, description, color, icon
//       Add nested fields: skills (array of Skill), skillCount, avgLevel
//
//   1c. Define a DashboardStats type with: totalSkills, masteredSkills, totalXP, avgLevel
//
//   1d. Define a RestVsGraphQL type with: feature, rest, graphql, winner
//
//   1e. Define Query type with these operations:
//       - getSkills(category, minLevel, tags) -> [Skill!]!
//       - getSkillById(id) -> Skill
//       - getCategories -> [Category!]!
//       - getDashboardStats -> DashboardStats!
//       - getRestVsGraphQLComparison -> [RestVsGraphQL!]!
//
// HINT: Use ! for non-null, [Type!]! for non-null array of non-null items
// WHY: A strongly typed schema means the server and client always agree on shape.
//      Zero runtime surprises. Compare this to REST where you discover mismatches
//      in production.
// ──────────────────────────────────────────────────────────────────────────────

export const typeDefs = gql`
  # TODO 1a: Define Skill type
  # type Skill { ... }

  # TODO 1b: Define Category type with nested skills
  # type Category { ... }

  # TODO 1c: Define DashboardStats and CategoryStat types
  # type DashboardStats { ... }
  # type CategoryStat { ... }

  # TODO 1d: Define RestVsGraphQL comparison type
  # type RestVsGraphQL { ... }

  # TODO 1e: Define Query type
  type Query {
    hello: String
    # Add your queries here...
  }
`;
""")

write('README.md', """\
# Step 1 — Define the GraphQL Schema

## Goal
Build the SDL (Schema Definition Language) that describes ALL the data your app needs.
**One schema replaces the implicit contracts of 5+ REST endpoints.**

## Your Tasks

### 1a. Skill type
```graphql
type Skill {
  id: ID!
  title: String!
  category: String!
  level: Int!
  maxLevel: Int!
  isMastered: Boolean!
  description: String!
  tags: [String!]!
  xp: Int!
}
```

### 1b. Category type (notice nested Skill array — resolved lazily!)
```graphql
type Category {
  id: ID!
  name: String!
  description: String!
  color: String!
  icon: String!
  skills: [Skill!]!      # Only resolved when client asks for it
  skillCount: Int!
  avgLevel: Float!
}
```

### 1c. Aggregated Stats type
```graphql
type DashboardStats {
  totalSkills: Int!
  masteredSkills: Int!
  totalXP: Int!
  avgLevel: Float!
  categoryBreakdown: [CategoryStat!]!
}
type CategoryStat { category: String! count: Int! avgLevel: Float! totalXP: Int! color: String! }
```

### 1d. REST vs GraphQL comparison type
```graphql
type RestVsGraphQL { feature: String! rest: String! graphql: String! winner: String! }
```

### 1e. Query operations
```graphql
type Query {
  getSkills(category: String, minLevel: Int, tags: [String]): [Skill!]!
  getSkillById(id: ID!): Skill
  getCategories: [Category!]!
  getDashboardStats: DashboardStats!
  getRestVsGraphQLComparison: [RestVsGraphQL!]!
}
```

## Key Concept: Why schema-first?
- Self-documenting — GraphiQL introspection shows everything
- Strongly typed — client and server agree at compile time
- Evolve without versions — add fields, deprecate old ones, never break clients

## Run & Verify
```bash
cd server && npm run dev
# Open http://localhost:4000/graphql
# Click "Schema" in the left sidebar — you should see all your types!
```

## Next Step
```bash
git checkout 01-schema-solution   # See the answer
git checkout 02-queries           # Next task
```
""")

git('add', '-A')
git('commit', '-m', '01-schema: TASK — define Skill, Category, Stats, RestVsGraphQL types')

# ════════════════════════════════════════════════════════════════════════════════
# BRANCH 3: 01-schema-solution
# ════════════════════════════════════════════════════════════════════════════════
git('checkout', 'main')
git('checkout', '-b', '01-schema-solution')

write('README.md', """\
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
""")

git('add', '-A')
git('commit', '-m', '01-schema-solution: complete SDL with all types')

# ════════════════════════════════════════════════════════════════════════════════
# BRANCH 4: 02-queries (TASK)
# ════════════════════════════════════════════════════════════════════════════════
git('checkout', 'main')
git('checkout', '-b', '02-queries')

write('server/resolvers.js', """\
import { skills } from './data/skills.js';
import { categories } from './data/categories.js';

// REST vs GraphQL comparison data
const restVsGraphQLData = [
  { feature: 'Data Fetching', rest: 'Multiple endpoints, over-fetching common', graphql: 'One endpoint — ask exactly what you need', winner: 'GraphQL' },
  { feature: 'Type Safety', rest: 'Manual OpenAPI docs, often stale', graphql: 'Schema IS the contract — always in sync', winner: 'GraphQL' },
  { feature: 'Real-time', rest: 'Polling or SSE workarounds', graphql: 'Built-in Subscriptions over WebSocket', winner: 'GraphQL' },
  { feature: 'Versioning', rest: '/v1, /v2 — breaking changes are painful', graphql: 'Evolve schema with deprecations, no versions', winner: 'GraphQL' },
  { feature: 'Caching', rest: 'HTTP cache headers, CDN-friendly', graphql: 'Normalized client cache (Apollo InMemoryCache)', winner: 'REST' },
  { feature: 'File Uploads', rest: 'Multipart form data — straightforward', graphql: 'Requires extra setup (graphql-upload)', winner: 'REST' },
  { feature: 'Tooling', rest: 'Postman, Swagger — mature ecosystem', graphql: 'GraphiQL, Apollo Studio, codegen — great DX', winner: 'GraphQL' },
  { feature: 'Learning Curve', rest: 'Familiar to every developer', graphql: 'Schema, resolvers, N+1 — takes time to master', winner: 'REST' },
];

export const resolvers = {
  Query: {
    // TODO 2a: Implement getSkills
    // It should support optional filtering by: category (String), minLevel (Int), tags ([String])
    // HINT: Use args.category, args.minLevel, args.tags
    // WHY: One resolver with args replaces GET /skills, GET /skills?category=Backend, etc.
    getSkills: (_, args = {}) => {
      // YOUR CODE HERE
      return [];
    },

    // TODO 2b: Implement getSkillById
    // Return the skill matching id, or null/undefined if not found
    getSkillById: (_, { id }) => {
      // YOUR CODE HERE
    },

    // TODO 2c: Implement getCategories
    // Return all categories from the categories data file
    getCategories: () => {
      // YOUR CODE HERE
      return [];
    },

    // TODO 2d: Implement getDashboardStats
    // Returns: { totalSkills, masteredSkills, totalXP, avgLevel, categoryBreakdown }
    // HIGHLIGHT: This ONE resolver replaces GET /stats + GET /categories + client aggregation
    getDashboardStats: () => {
      // YOUR CODE HERE
      return { totalSkills: 0, masteredSkills: 0, totalXP: 0, avgLevel: 0, categoryBreakdown: [] };
    },

    getRestVsGraphQLComparison: () => restVsGraphQLData,
  },

  // TODO 2e: Implement field-level resolvers (GraphQL superpower!)
  // These resolve nested fields only when the client requests them.
  // With REST you'd always fetch everything or make a second request.
  Skill: {
    // categoryInfo: (skill) => ???
  },
  Category: {
    // skills: (cat) => ???
    // skillCount: (cat) => ???
    // avgLevel: (cat) => ???
  },
};
""")

write('client/src/App.jsx', """\
import { useState } from 'react';
import { ApolloProvider } from '@apollo/client';
import { client } from './apollo/client';
import Header from './components/Header';
import CategoryFilter from './components/CategoryFilter';
import SkillGrid from './components/SkillGrid';
import StatsPanel from './components/StatsPanel';
import RestVsGraphQL from './components/RestVsGraphQL';

// TODO 2f: Wrap your app in ApolloProvider so all components can use useQuery/useMutation
// ApolloProvider makes the Apollo client available throughout the component tree.
// HINT: <ApolloProvider client={client}> ... </ApolloProvider>

function App() {
  const [selectedCategory, setSelectedCategory] = useState(null);

  return (
    <div className="app">
      <Header />
      <main className="main-content">
        <RestVsGraphQL />
        <StatsPanel />
        <section className="skills-section">
          <div className="skills-header">
            <h2 className="panel-title"><span className="panel-icon">🎯</span>Skill Tree</h2>
            <CategoryFilter selected={selectedCategory} onChange={setSelectedCategory} />
          </div>
          <SkillGrid selectedCategory={selectedCategory} />
        </section>
      </main>
    </div>
  );
}

// YOUR CODE HERE — export with ApolloProvider wrapper
export default App;
""")

write('README.md', """\
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
""")

git('add', '-A')
git('commit', '-m', '02-queries: TASK — implement getSkills, getCategories, getDashboardStats resolvers')

# ════════════════════════════════════════════════════════════════════════════════
# BRANCH 5: 02-queries-solution
# ════════════════════════════════════════════════════════════════════════════════
git('checkout', 'main')
git('checkout', '-b', '02-queries-solution')

write('README.md', """\
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
""")

git('add', '-A')
git('commit', '-m', '02-queries-solution: all queries working, ApolloProvider wired up')

# ════════════════════════════════════════════════════════════════════════════════
# BRANCH 6: 03-mutations (TASK)
# ════════════════════════════════════════════════════════════════════════════════
git('checkout', 'main')
git('checkout', '-b', '03-mutations')

write('server/resolvers.js', """\
import { skills } from './data/skills.js';
import { categories } from './data/categories.js';

const restVsGraphQLData = [
  { feature: 'Data Fetching', rest: 'Multiple endpoints, over-fetching common', graphql: 'One endpoint — ask exactly what you need', winner: 'GraphQL' },
  { feature: 'Type Safety', rest: 'Manual OpenAPI docs, often stale', graphql: 'Schema IS the contract — always in sync', winner: 'GraphQL' },
  { feature: 'Real-time', rest: 'Polling or SSE workarounds', graphql: 'Built-in Subscriptions over WebSocket', winner: 'GraphQL' },
  { feature: 'Versioning', rest: '/v1, /v2 — breaking changes are painful', graphql: 'Evolve schema with deprecations, no versions', winner: 'GraphQL' },
  { feature: 'Caching', rest: 'HTTP cache headers, CDN-friendly', graphql: 'Normalized client cache (Apollo InMemoryCache)', winner: 'REST' },
  { feature: 'File Uploads', rest: 'Multipart form data — straightforward', graphql: 'Requires extra setup (graphql-upload)', winner: 'REST' },
  { feature: 'Tooling', rest: 'Postman, Swagger — mature ecosystem', graphql: 'GraphiQL, Apollo Studio, codegen — great DX', winner: 'GraphQL' },
  { feature: 'Learning Curve', rest: 'Familiar to every developer', graphql: 'Schema, resolvers, N+1 — takes time to master', winner: 'REST' },
];

export const resolvers = {
  Query: {
    getSkills: (_, args = {}) => {
      let result = [...skills];
      if (args.category) result = result.filter(s => s.category === args.category);
      if (args.minLevel) result = result.filter(s => s.level >= args.minLevel);
      if (args.tags && args.tags.length) result = result.filter(s => args.tags.some(t => s.tags.includes(t)));
      return result;
    },
    getSkillById: (_, { id }) => skills.find(s => s.id === id),
    getCategories: () => categories,
    getCategoryByName: (_, { name }) => categories.find(c => c.name === name),
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
    getRestVsGraphQLComparison: () => restVsGraphQLData,
  },

  Mutation: {
    // TODO 3a: Implement levelUpSkill
    // - Find the skill by id (throw Error if not found)
    // - Throw if already at maxLevel
    // - Increment level by 1, add 100 xp
    // - If level === maxLevel, set isMastered = true
    // - Return the updated skill
    // WHY IT MATTERS: Unlike REST PATCH which returns nothing useful,
    //   GraphQL mutations return the updated object so Apollo cache auto-updates!
    levelUpSkill: (_, { id }) => {
      // YOUR CODE HERE
      throw new Error('Not implemented yet');
    },

    // TODO 3b: Implement addTagToSkill
    // - Find skill, push tag if not already present, return skill
    addTagToSkill: (_, { id, tag }) => {
      // YOUR CODE HERE
      throw new Error('Not implemented yet');
    },

    // TODO 3c: Implement resetSkill
    // - Find skill, set level=1, xp=100, isMastered=false, return skill
    resetSkill: (_, { id }) => {
      // YOUR CODE HERE
      throw new Error('Not implemented yet');
    },
  },

  Skill: {
    categoryInfo: (skill) => categories.find(c => c.name === skill.category),
  },
  Category: {
    skills: (cat) => skills.filter(s => s.category === cat.name),
    skillCount: (cat) => skills.filter(s => s.category === cat.name).length,
    avgLevel: (cat) => { const cs = skills.filter(s => s.category === cat.name); return cs.reduce((a,s)=>a+s.level,0)/cs.length; },
  },
};
""")

write('client/src/components/SkillCard.jsx', """\
import { useMutation } from '@apollo/client';
import { motion } from 'framer-motion';
import { LEVEL_UP_SKILL } from '../graphql/mutations';

const CATEGORY_COLORS = {
  Frontend: '#60a5fa', Backend: '#34d399', DevOps: '#f97316', 'AI/ML': '#a78bfa',
};

export default function SkillCard({ skill }) {
  const color = CATEGORY_COLORS[skill.category] || '#60a5fa';
  const pct = Math.round((skill.level / skill.maxLevel) * 100);

  // TODO 3d: Implement useMutation for LEVEL_UP_SKILL
  // HINT: const [levelUp, { loading }] = useMutation(LEVEL_UP_SKILL, {
  //   variables: { id: skill.id },
  // });
  // WHY: When the mutation returns the updated Skill, Apollo Client automatically
  // updates the normalized cache — ALL components showing this skill re-render!
  // With REST PATCH you'd have to manually refetch or update state.
  const levelUp = () => alert('TODO: wire up useMutation');
  const loading = false;

  return (
    <motion.div
      layout
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, scale: 0.9 }}
      className="skill-card"
      style={{ '--card-accent': color }}
    >
      {skill.isMastered && <div className="mastered-badge">✓ Mastered</div>}
      <div className="card-header">
        <h3 className="card-title">{skill.title}</h3>
        <span className="card-cat" style={{ color }}>{skill.category}</span>
      </div>
      <p className="card-desc">{skill.description}</p>
      <div className="card-tags">
        {skill.tags.map(t => <span key={t} className="tag">#{t}</span>)}
      </div>
      <div className="level-row">
        <span className="level-label">Level {skill.level} / {skill.maxLevel}</span>
        <span className="xp-label">{skill.xp} XP</span>
      </div>
      <div className="progress-track">
        <motion.div className="progress-bar" style={{ backgroundColor: color }} animate={{ width: pct + '%' }} transition={{ type: 'spring', stiffness: 120 }} />
      </div>
      <div className="card-actions">
        <button
          className="btn-level-up"
          style={{ '--btn-color': color }}
          onClick={() => levelUp()}
          disabled={loading || skill.isMastered}
        >
          {loading ? '...' : skill.isMastered ? 'MAX' : '⬆ Level Up'}
        </button>
      </div>
    </motion.div>
  );
}
""")

write('README.md', """\
# Step 3 — Implement GraphQL Mutations

## Goal
Add write operations. See how returning the updated object makes Apollo cache updates automatic.

## Your Tasks

### Server (server/resolvers.js)

#### 3a. levelUpSkill mutation
```js
levelUpSkill: (_, { id }) => {
  const skill = skills.find(s => s.id === id);
  if (!skill) throw new Error('Skill not found');
  if (skill.level >= skill.maxLevel) throw new Error('Already at max level');
  skill.level += 1;
  skill.xp += 100;
  if (skill.level === skill.maxLevel) skill.isMastered = true;
  return skill; // Return updated skill — Apollo cache auto-updates!
},
```

#### 3b. addTagToSkill
```js
addTagToSkill: (_, { id, tag }) => {
  const skill = skills.find(s => s.id === id);
  if (!skill) throw new Error('Skill not found');
  if (!skill.tags.includes(tag)) skill.tags.push(tag);
  return skill;
},
```

#### 3c. resetSkill
```js
resetSkill: (_, { id }) => {
  const skill = skills.find(s => s.id === id);
  if (!skill) throw new Error('Skill not found');
  skill.level = 1; skill.xp = 100; skill.isMastered = false;
  return skill;
},
```

### Client (client/src/components/SkillCard.jsx)

#### 3d. Wire up useMutation
```jsx
const [levelUp, { loading }] = useMutation(LEVEL_UP_SKILL, {
  variables: { id: skill.id },
  onCompleted: () => { setFlashing(true); setTimeout(() => setFlashing(false), 600); },
});
```
**Key insight:** The mutation returns the updated Skill object. Apollo Client uses the `id`
field to find it in the normalized cache and updates it — **every component showing that skill
instantly re-renders with the new level**. No manual state updates needed!

## Verify in GraphiQL
```graphql
mutation {
  levelUpSkill(id: "sk-6") {
    id title level xp isMastered
  }
}
```

## REST vs GraphQL: Write operations
- REST PATCH: returns 204 No Content — you have to refetch or manually update state
- GraphQL Mutation: returns the updated object — cache updates automatically

## Next Step
```bash
git checkout 03-mutations-solution   # See the answer
git checkout 04-subscriptions        # Next task — Real-time!
```
""")

git('add', '-A')
git('commit', '-m', '03-mutations: TASK — implement levelUpSkill, addTagToSkill, resetSkill')

# ════════════════════════════════════════════════════════════════════════════════
# BRANCH 7: 03-mutations-solution
# ════════════════════════════════════════════════════════════════════════════════
git('checkout', 'main')
git('checkout', '-b', '03-mutations-solution')

write('README.md', """\
# Step 3 — SOLUTION: Mutations Working

## What we proved
- Mutations return the updated object — Apollo cache updates automatically
- No manual state management, no refetch calls needed
- SkillCard level bar animates immediately — zero extra code

## Next Step
```bash
git checkout 04-subscriptions
```
""")

git('add', '-A')
git('commit', '-m', '03-mutations-solution: levelUpSkill + useMutation fully working')

# ════════════════════════════════════════════════════════════════════════════════
# BRANCH 8: 04-subscriptions (TASK)
# ════════════════════════════════════════════════════════════════════════════════
git('checkout', 'main')
git('checkout', '-b', '04-subscriptions')

write('server/resolvers.js', """\
// TODO 4a: Import PubSub from graphql-subscriptions
// import { PubSub } from 'graphql-subscriptions';
import { skills } from './data/skills.js';
import { categories } from './data/categories.js';

// TODO 4b: Create a pubsub instance and define event name constants
// const pubsub = new PubSub();
// const SKILL_LEVELED_UP = 'SKILL_LEVELED_UP';

const restVsGraphQLData = [
  { feature: 'Data Fetching', rest: 'Multiple endpoints, over-fetching common', graphql: 'One endpoint — ask exactly what you need', winner: 'GraphQL' },
  { feature: 'Type Safety', rest: 'Manual OpenAPI docs, often stale', graphql: 'Schema IS the contract — always in sync', winner: 'GraphQL' },
  { feature: 'Real-time', rest: 'Polling or SSE workarounds', graphql: 'Built-in Subscriptions over WebSocket', winner: 'GraphQL' },
  { feature: 'Versioning', rest: '/v1, /v2 — breaking changes are painful', graphql: 'Evolve schema with deprecations, no versions', winner: 'GraphQL' },
  { feature: 'Caching', rest: 'HTTP cache headers, CDN-friendly', graphql: 'Normalized client cache (Apollo InMemoryCache)', winner: 'REST' },
  { feature: 'File Uploads', rest: 'Multipart form data — straightforward', graphql: 'Requires extra setup (graphql-upload)', winner: 'REST' },
  { feature: 'Tooling', rest: 'Postman, Swagger — mature ecosystem', graphql: 'GraphiQL, Apollo Studio, codegen — great DX', winner: 'GraphQL' },
  { feature: 'Learning Curve', rest: 'Familiar to every developer', graphql: 'Schema, resolvers, N+1 — takes time to master', winner: 'REST' },
];

export const resolvers = {
  Query: {
    getSkills: (_, args = {}) => {
      let result = [...skills];
      if (args.category) result = result.filter(s => s.category === args.category);
      if (args.minLevel) result = result.filter(s => s.level >= args.minLevel);
      if (args.tags && args.tags.length) result = result.filter(s => args.tags.some(t => s.tags.includes(t)));
      return result;
    },
    getSkillById: (_, { id }) => skills.find(s => s.id === id),
    getCategories: () => categories,
    getCategoryByName: (_, { name }) => categories.find(c => c.name === name),
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
    getRestVsGraphQLComparison: () => restVsGraphQLData,
  },

  Mutation: {
    levelUpSkill: (_, { id }) => {
      const skill = skills.find(s => s.id === id);
      if (!skill) throw new Error('Skill not found');
      if (skill.level >= skill.maxLevel) throw new Error('Already at max level');
      skill.level += 1;
      skill.xp += 100;
      if (skill.level === skill.maxLevel) skill.isMastered = true;
      // TODO 4c: Publish the updated skill to SKILL_LEVELED_UP
      // pubsub.publish(SKILL_LEVELED_UP, { skillLeveledUp: skill });
      // WHY: This pushes the update to ALL connected WebSocket clients in real time!
      // Open two browser tabs — level up in one, see it update in the other instantly.
      return skill;
    },
    addTagToSkill: (_, { id, tag }) => {
      const skill = skills.find(s => s.id === id);
      if (!skill) throw new Error('Skill not found');
      if (!skill.tags.includes(tag)) skill.tags.push(tag);
      return skill;
    },
    resetSkill: (_, { id }) => {
      const skill = skills.find(s => s.id === id);
      if (!skill) throw new Error('Skill not found');
      skill.level = 1; skill.xp = 100; skill.isMastered = false;
      return skill;
    },
  },

  // TODO 4d: Add the Subscription resolver
  // Subscription: {
  //   skillLeveledUp: {
  //     subscribe: () => pubsub.asyncIterator([SKILL_LEVELED_UP]),
  //   },
  // },

  Skill: { categoryInfo: (skill) => categories.find(c => c.name === skill.category) },
  Category: {
    skills: (cat) => skills.filter(s => s.category === cat.name),
    skillCount: (cat) => skills.filter(s => s.category === cat.name).length,
    avgLevel: (cat) => { const cs = skills.filter(s => s.category === cat.name); return cs.reduce((a,s)=>a+s.level,0)/cs.length; },
  },
};
""")

write('client/src/App.jsx', """\
import { useState, useEffect, useRef } from 'react';
// TODO 4e: Import useSubscription from @apollo/client
// import { useSubscription } from '@apollo/client';
import { AnimatePresence } from 'framer-motion';
// TODO 4f: Import the SKILL_LEVELED_UP subscription document
// import { SKILL_LEVELED_UP } from './graphql/subscriptions';
import { useApolloClient, ApolloProvider } from '@apollo/client';
import { client } from './apollo/client';
import Header from './components/Header';
import CategoryFilter from './components/CategoryFilter';
import SkillGrid from './components/SkillGrid';
import StatsPanel from './components/StatsPanel';
import RestVsGraphQL from './components/RestVsGraphQL';
import LiveIndicator from './components/LiveIndicator';
import Toast from './components/Toast';

function App() {
  const [selectedCategory, setSelectedCategory] = useState(null);
  const [toasts, setToasts] = useState([]);
  const [wsConnected, setWsConnected] = useState(false);
  const toastId = useRef(0);
  const apolloClient = useApolloClient();

  const addToast = (msg) => {
    const id = ++toastId.current;
    setToasts(prev => [...prev, { id, msg }]);
    setTimeout(() => setToasts(prev => prev.filter(t => t.id !== id)), 4000);
  };

  // TODO 4g: Add useSubscription hook here
  // useSubscription(SKILL_LEVELED_UP, {
  //   onData: ({ data }) => {
  //     const skill = data?.data?.skillLeveledUp;
  //     if (!skill) return;
  //     setWsConnected(true);
  //     addToast(`⬆ ${skill.title} leveled up to ${skill.level}!`);
  //     // TODO 4h: Update Apollo cache so all components re-render
  //     // apolloClient.cache.modify({
  //     //   id: apolloClient.cache.identify({ __typename: 'Skill', id: skill.id }),
  //     //   fields: {
  //     //     level: () => skill.level,
  //     //     xp: () => skill.xp,
  //     //     isMastered: () => skill.isMastered,
  //     //   },
  //     // });
  //   },
  //   onError: () => setWsConnected(false),
  // });
  //
  // NOTE: Also update client/src/apollo/client.js to use the split link
  // that routes subscriptions to WebSocket and queries/mutations to HTTP.

  useEffect(() => { const t = setTimeout(() => setWsConnected(true), 1000); return () => clearTimeout(t); }, []);

  return (
    <div className="app">
      <LiveIndicator connected={wsConnected} />
      <Header />
      <main className="main-content">
        <RestVsGraphQL />
        <StatsPanel />
        <section className="skills-section">
          <div className="skills-header">
            <h2 className="panel-title"><span className="panel-icon">🎯</span>Skill Tree</h2>
            <CategoryFilter selected={selectedCategory} onChange={setSelectedCategory} />
          </div>
          <SkillGrid selectedCategory={selectedCategory} />
        </section>
      </main>
      <div className="toast-stack">
        <AnimatePresence>
          {toasts.map(t => <Toast key={t.id} message={t.msg} onDone={() => setToasts(prev => prev.filter(x => x.id !== t.id))} />)}
        </AnimatePresence>
      </div>
    </div>
  );
}

export default function AppWithProvider() {
  return <ApolloProvider client={client}><App /></ApolloProvider>;
}
""")

write('README.md', """\
# Step 4 — Real-time Subscriptions

## Goal
Make the app real-time with WebSocket subscriptions.
**Open two browser tabs — level up a skill in one, watch it update in the other instantly.**
This is impossible with plain REST without polling hacks.

## Your Tasks

### Server (server/resolvers.js)

#### 4a. Import PubSub
```js
import { PubSub } from 'graphql-subscriptions';
```

#### 4b. Create pubsub instance
```js
const pubsub = new PubSub();
const SKILL_LEVELED_UP = 'SKILL_LEVELED_UP';
```

#### 4c. Publish in levelUpSkill mutation
```js
// After updating the skill:
pubsub.publish(SKILL_LEVELED_UP, { skillLeveledUp: skill });
```

#### 4d. Add Subscription resolver
```js
Subscription: {
  skillLeveledUp: {
    subscribe: () => pubsub.asyncIterator([SKILL_LEVELED_UP]),
  },
},
```

### Client

#### 4e–4f. Import useSubscription + subscription document
```js
import { useSubscription } from '@apollo/client';
import { SKILL_LEVELED_UP } from './graphql/subscriptions';
```

#### 4g. Add the subscription hook in App.jsx
```jsx
useSubscription(SKILL_LEVELED_UP, {
  onData: ({ data }) => {
    const skill = data?.data?.skillLeveledUp;
    if (!skill) return;
    setWsConnected(true);
    addToast(`⬆ ${skill.title} leveled up to ${skill.level}!`);
    // 4h: Update cache
    apolloClient.cache.modify({
      id: apolloClient.cache.identify({ __typename: 'Skill', id: skill.id }),
      fields: { level: () => skill.level, xp: () => skill.xp, isMastered: () => skill.isMastered },
    });
  },
});
```

#### Note: client/src/apollo/client.js already has the split link configured.
The `split()` function routes subscription operations to WebSocket and everything else to HTTP.

## Demo moment
1. Start server + client
2. Open http://localhost:5173 in **two tabs**
3. Level up a skill in Tab 1
4. Watch Tab 2 update in real-time — no refresh, no polling!

## REST comparison
With REST you'd need:
- Server-Sent Events (SSE) + custom event handling
- WebSocket from scratch + message protocol
- Manual reconnection logic
GraphQL Subscriptions give you all of this with a 5-line resolver.

## Next Step
```bash
git checkout 04-subscriptions-solution   # See the answer
git checkout 05-rest-vs-graphql          # Next: deepen the comparison
```
""")

git('add', '-A')
git('commit', '-m', '04-subscriptions: TASK — add PubSub, publish event, useSubscription hook')

# ════════════════════════════════════════════════════════════════════════════════
# BRANCH 9: 04-subscriptions-solution
# ════════════════════════════════════════════════════════════════════════════════
git('checkout', 'main')
git('checkout', '-b', '04-subscriptions-solution')

write('README.md', """\
# Step 4 — SOLUTION: Real-time Subscriptions Working

## What we proved
- PubSub broadcasts events over WebSocket to all connected clients
- Two tabs open, level up in one → updates instantly in the other
- Apollo cache.modify() propagates changes to every component using that skill
- The green "Live" indicator shows active WebSocket connection

## Architecture
```
Browser Tab 1          Server                  Browser Tab 2
    │                    │                          │
    ├── levelUpSkill ──► │                          │
    │                    ├── pubsub.publish() ──────►│
    │                    │                          │
    │                    │   ◄── skillLeveledUp ────┤
    │                    │        (WS push)         │
    │                    │                   cache.modify()
    │                    │                   → UI re-renders
```

## Next Step
```bash
git checkout 05-rest-vs-graphql
```
""")

git('add', '-A')
git('commit', '-m', '04-subscriptions-solution: full real-time working, cross-tab sync demo')

# ════════════════════════════════════════════════════════════════════════════════
# BRANCH 10: 05-rest-vs-graphql (TASK — show comparison panel)
# ════════════════════════════════════════════════════════════════════════════════
git('checkout', 'main')
git('checkout', '-b', '05-rest-vs-graphql')

write('client/src/components/RestVsGraphQL.jsx', """\
import { useQuery } from '@apollo/client';
import { motion } from 'framer-motion';
import { GET_REST_VS_GRAPHQL } from '../graphql/queries';

// TODO 5a: This component fetches comparison data FROM GraphQL and renders a table.
// The entire comparison table is data-driven — the server controls the content.
// This demonstrates that GraphQL is flexible enough to serve ANY shape of data.
//
// TASK: Complete the query below, then render the comparison rows.
// The data comes from getRestVsGraphQLComparison query which returns:
//   { feature, rest, graphql, winner }
//
// BONUS: Notice how this component fetches data WITHOUT prop drilling.
// Any component can call useQuery() and get exactly what it needs.
// With REST you'd have to pass the comparison data down from a parent, or make
// a separate fetch call with its own loading/error state.

export default function RestVsGraphQL() {
  // TODO 5b: Uncomment and complete this query
  // const { data, loading } = useQuery(GET_REST_VS_GRAPHQL);

  // DEMO DATA — replace with real query result
  const loading = false;
  const data = {
    getRestVsGraphQLComparison: [
      { feature: 'Data Fetching', rest: 'Multiple endpoints', graphql: 'One endpoint', winner: 'GraphQL' },
      { feature: 'Type Safety', rest: 'Manual docs', graphql: 'Schema contract', winner: 'GraphQL' },
      { feature: 'Real-time', rest: 'Polling / SSE', graphql: 'Built-in Subscriptions', winner: 'GraphQL' },
    ],
  };

  return (
    <section className="comparison-panel">
      <h2 className="panel-title">
        <span className="panel-icon">⚔</span>
        REST vs GraphQL — Why Switch in 2026?
      </h2>
      <p className="panel-sub">
        This data is fetched from a single GraphQL query (<code>getRestVsGraphQLComparison</code>).
        {/* TODO 5c: Add a note about how many REST calls this would replace */}
      </p>

      {loading ? (
        <p>Loading...</p>
      ) : (
        <div className="comparison-grid">
          <div className="comparison-header">
            <span>Feature</span><span>REST</span><span>GraphQL</span><span>Winner</span>
          </div>
          {/* TODO 5d: Map over data?.getRestVsGraphQLComparison and render comparison rows */}
          {data?.getRestVsGraphQLComparison.map((row, i) => (
            <motion.div key={row.feature} className="comparison-row" initial={{ opacity:0, x:-20 }} animate={{ opacity:1, x:0 }} transition={{ delay: i * 0.07 }}>
              <span className="cmp-feature">{row.feature}</span>
              <span className="cmp-rest">{row.rest}</span>
              <span className="cmp-gql">{row.graphql}</span>
              <span className={`cmp-winner ${row.winner.toLowerCase()}`}>{row.winner}</span>
            </motion.div>
          ))}
        </div>
      )}
    </section>
  );
}
""")

write('README.md', """\
# Step 5 — REST vs GraphQL: The Full Picture

## Goal
Wire up the comparison panel to fetch live data from GraphQL.
Use this as a discussion point with the audience.

## Your Tasks

### 5a–5d. Connect RestVsGraphQL.jsx to real data
```jsx
const { data, loading } = useQuery(GET_REST_VS_GRAPHQL);
```
Remove the hardcoded demo data and use the live query result.

## Discussion Points for the Audience

### When GraphQL wins
| Scenario | Why GraphQL |
|---|---|
| Mobile apps with limited bandwidth | Request only needed fields |
| Complex dashboards | One request for all widget data |
| Public APIs with diverse clients | Each client shapes its own response |
| Rapidly evolving schemas | Add fields without versioning |

### When REST wins
| Scenario | Why REST |
|---|---|
| Simple CRUD services | REST is simpler to set up |
| File upload heavy apps | Multipart is painful in GraphQL |
| CDN-heavy public APIs | HTTP caching is effortless with REST |
| Teams unfamiliar with GraphQL | Learning curve is real |

### Latest Trends in GraphQL (2026)
1. **Federation & Supergraph** — Apollo Federation 2, Cosmo Router
   Multiple teams own separate subgraphs, unified into one API gateway
2. **GraphQL over HTTP 1.1** — The new spec standardizes transport
3. **@defer / @stream** — Stream large datasets incrementally
4. **Persisted Queries / APQ** — CDN-cacheable POST requests
5. **Code-first schemas** — Pothos, TypeGraphQL for type-safe schema building
6. **Edge GraphQL** — Running resolvers at the edge (Cloudflare Workers)

## Next Step
```bash
git checkout 05-rest-vs-graphql-solution
git checkout 06-scaling
```
""")

git('add', '-A')
git('commit', '-m', '05-rest-vs-graphql: TASK — wire up comparison panel + discussion notes')

# ════════════════════════════════════════════════════════════════════════════════
# BRANCH 11: 05-rest-vs-graphql-solution
# ════════════════════════════════════════════════════════════════════════════════
git('checkout', 'main')
git('checkout', '-b', '05-rest-vs-graphql-solution')

write('README.md', """\
# Step 5 — SOLUTION: REST vs GraphQL Panel

## What we showed
- Comparison data comes from a GraphQL query (meta!)
- useQuery works in any component — no prop drilling, no Redux
- The table shows both where GraphQL wins and where REST is still better

## Next Step
```bash
git checkout 06-scaling
```
""")

git('add', '-A')
git('commit', '-m', '05-rest-vs-graphql-solution: comparison panel fully data-driven')

# ════════════════════════════════════════════════════════════════════════════════
# BRANCH 12: 06-scaling (TASK — N+1 problem, fragments, patterns)
# ════════════════════════════════════════════════════════════════════════════════
git('checkout', 'main')
git('checkout', '-b', '06-scaling')

write('server/dataloader.js', """\
// ── DataLoader — Solving the N+1 Problem ─────────────────────────────────────
// The N+1 problem: if you have 20 skills and each needs its categoryInfo,
// you'd make 20 database calls (one per skill). With DataLoader, you batch
// them into ONE call per request cycle.
//
// This is critical for scaling GraphQL in production.
//
// Without DataLoader (N+1):
//   getSkills returns 20 skills
//   → For each skill, categoryInfo resolver runs → 20 DB calls = N+1 problem!
//
// With DataLoader:
//   All 20 categoryInfo requests are batched → 1 DB call
//
// TODO 6a: Install DataLoader
//   cd server && npm install dataloader
//
// TODO 6b: Implement the batch function below
// import DataLoader from 'dataloader';
// import { categories } from './data/categories.js';
//
// The batch function receives an array of keys (category names)
// and must return an array of values IN THE SAME ORDER.
//
// export function createCategoryLoader() {
//   return new DataLoader(async (categoryNames) => {
//     // Batch load — instead of N queries, this runs ONCE per request
//     return categoryNames.map(name => categories.find(c => c.name === name) || null);
//   });
// }
//
// TODO 6c: In server/index.js, add the loader to Apollo context:
// expressMiddleware(server, {
//   context: async () => ({ categoryLoader: createCategoryLoader() })
// })
//
// TODO 6d: Use the loader in the Skill.categoryInfo resolver:
// Skill: {
//   categoryInfo: (skill, _, { categoryLoader }) => categoryLoader.load(skill.category),
// }

export function createCategoryLoader() {
  // Stub — implement above
  return { load: (name) => Promise.resolve(null) };
}
""")

write('server/complexity.js', """\
// ── Query Complexity — Protecting Your GraphQL API ───────────────────────────
// Without complexity limits, a malicious client could send:
//   { getCategories { skills { categoryInfo { skills { categoryInfo { ... } } } } } }
// This creates exponential DB calls (N+1 on steroids).
//
// PRODUCTION BEST PRACTICES:
//
// 1. Query Depth Limiting
//    Use: graphql-depth-limit
//    npm install graphql-depth-limit
//
// 2. Query Complexity Analysis
//    Use: graphql-query-complexity
//    npm install graphql-query-complexity
//
// 3. Persisted Queries (APQ)
//    Only allow pre-registered query hashes — blocks arbitrary queries
//    Apollo Client supports this out of the box with:
//    import { createPersistedQueryLink } from '@apollo/client/link/persisted-queries';
//
// 4. Rate Limiting
//    Limit by IP or auth token at the HTTP layer
//
// Example depth limit setup (for index.js):
// import depthLimit from 'graphql-depth-limit';
// const server = new ApolloServer({
//   schema,
//   validationRules: [depthLimit(5)], // Max 5 levels deep
// });
//
// Example complexity setup (for index.js):
// import { createComplexityRule, simpleEstimator } from 'graphql-query-complexity';
// validationRules: [
//   createComplexityRule({
//     estimators: [simpleEstimator({ defaultComplexity: 1 })],
//     maximumComplexity: 100,
//     onComplete: (complexity) => console.log('Query complexity:', complexity),
//   }),
// ],

export const scalingNotes = {
  dataLoader: 'Batch N+1 DB calls into 1 per request cycle',
  depthLimit: 'Prevent deeply nested query attacks',
  complexity: 'Assign cost to fields, reject expensive queries',
  apq: 'Persisted queries — CDN-cacheable, faster, more secure',
  pagination: 'Use cursor-based pagination for large lists (Relay spec)',
  caching: 'Apollo Server Response Cache plugin for field-level TTL',
  federation: 'Apollo Federation — split schema across microservice teams',
};
""")

write('client/src/graphql/fragments.js', """\
import { gql } from '@apollo/client';

// ── Fragments — DRY GraphQL operations ──────────────────────────────────────
// Instead of repeating field lists in every query/mutation,
// define reusable fragments. This is a key GraphQL best practice for scaling.
//
// Benefits:
// 1. DRY — change the fields in one place
// 2. Co-location — component knows exactly what data it needs
// 3. Type safety — fragment types can be generated by GraphQL codegen
//
// TODO 6e: Use these fragments in your queries/mutations
// HINT: In a query: ...SkillFields  (spread the fragment)

export const SKILL_FRAGMENT = gql`
  fragment SkillFields on Skill {
    id
    title
    category
    level
    maxLevel
    isMastered
    description
    tags
    xp
  }
`;

export const CATEGORY_STAT_FRAGMENT = gql`
  fragment CategoryStatFields on CategoryStat {
    category
    count
    avgLevel
    totalXP
    color
  }
`;

// TODO 6f: Update GET_SKILLS query in queries.js to use the fragment:
// import { SKILL_FRAGMENT } from './fragments';
// export const GET_SKILLS = gql`
//   ${SKILL_FRAGMENT}
//   query GetSkills($category: String) {
//     getSkills(category: $category) {
//       ...SkillFields
//     }
//   }
// `;
""")

write('README.md', """\
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
""")

git('add', '-A')
git('commit', '-m', '06-scaling: TASK — DataLoader N+1, complexity limits, fragments, Federation overview')

# ════════════════════════════════════════════════════════════════════════════════
# BRANCH 13: 06-scaling-solution
# ════════════════════════════════════════════════════════════════════════════════
git('checkout', 'main')
git('checkout', '-b', '06-scaling-solution')

write('server/dataloader.js', """\
import DataLoader from 'dataloader';
import { categories } from './data/categories.js';

// DataLoader batches ALL categoryInfo resolver calls within a single tick
// into one batch function call — eliminating the N+1 problem.
export function createCategoryLoader() {
  return new DataLoader(async (categoryNames) => {
    console.log(`DataLoader batch: ${categoryNames.length} categories in one call`);
    return categoryNames.map(name => categories.find(c => c.name === name) || null);
  });
}
""")

write('README.md', """\
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
""")

git('add', '-A')
git('commit', '-m', '06-scaling-solution: DataLoader implemented, all scaling patterns documented')

# ── Back to main ──────────────────────────────────────────────────────────────
git('checkout', 'main')

print('\nAll 13 branches created successfully!')
print('\nBranch map:')
branches = [
    'starter',
    '01-schema', '01-schema-solution',
    '02-queries', '02-queries-solution',
    '03-mutations', '03-mutations-solution',
    '04-subscriptions', '04-subscriptions-solution',
    '05-rest-vs-graphql', '05-rest-vs-graphql-solution',
    '06-scaling', '06-scaling-solution',
]
for b in branches:
    print(f'  {b}')
