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
