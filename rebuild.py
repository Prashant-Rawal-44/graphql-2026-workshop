import os

B = '/Users/prashant/Desktop/Project-graphQL'

def w(path, content):
    full = os.path.join(B, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w') as f:
        f.write(content)
    print(f'  wrote {path}')

# ── server/data/skills.js ─────────────────────────────────────────────────────
w('server/data/skills.js', """\
export const skills = [
  // Frontend
  { id: 'sk-1',  title: 'React 19',            category: 'Frontend', level: 8, maxLevel: 10, isMastered: false, description: 'Server Components, Actions, use() hook and concurrent features.', tags: ['react','components','hooks'], xp: 800 },
  { id: 'sk-2',  title: 'TypeScript 5',        category: 'Frontend', level: 7, maxLevel: 10, isMastered: false, description: 'Strict mode, decorators, template literal types, satisfies operator.', tags: ['typescript','types','tooling'], xp: 700 },
  { id: 'sk-3',  title: 'Tailwind CSS',        category: 'Frontend', level: 9, maxLevel: 10, isMastered: false, description: 'Utility-first styling, JIT engine, dark mode, and custom plugins.', tags: ['css','tailwind','design'], xp: 900 },
  { id: 'sk-4',  title: 'Web Performance',     category: 'Frontend', level: 6, maxLevel: 10, isMastered: false, description: 'Core Web Vitals, LCP optimization, code splitting, prefetching.', tags: ['performance','vitals','optimization'], xp: 600 },
  { id: 'sk-5',  title: 'Framer Motion',       category: 'Frontend', level: 5, maxLevel: 10, isMastered: false, description: 'Layout animations, shared element transitions, gesture handling.', tags: ['animation','motion','ux'], xp: 500 },
  // Backend
  { id: 'sk-6',  title: 'GraphQL',             category: 'Backend',  level: 3, maxLevel: 10, isMastered: false, description: 'Schema-first design, resolvers, DataLoader, subscriptions.', tags: ['graphql','api','apollo'], xp: 300 },
  { id: 'sk-7',  title: 'Node.js',             category: 'Backend',  level: 7, maxLevel: 10, isMastered: false, description: 'Event loop, streams, worker threads, performance tuning.', tags: ['node','javascript','backend'], xp: 700 },
  { id: 'sk-8',  title: 'PostgreSQL',          category: 'Backend',  level: 6, maxLevel: 10, isMastered: false, description: 'Query optimization, indexing, CTEs, window functions, JSONB.', tags: ['database','sql','postgres'], xp: 600 },
  { id: 'sk-9',  title: 'Redis',               category: 'Backend',  level: 5, maxLevel: 10, isMastered: false, description: 'Caching strategies, pub/sub, streams, sorted sets.', tags: ['cache','redis','performance'], xp: 500 },
  { id: 'sk-10', title: 'REST API Design',     category: 'Backend',  level: 8, maxLevel: 10, isMastered: false, description: 'OpenAPI spec, versioning, HATEOAS, idempotency, rate limiting.', tags: ['rest','api','http'], xp: 800 },
  // DevOps
  { id: 'sk-11', title: 'Docker',              category: 'DevOps',   level: 7, maxLevel: 10, isMastered: false, description: 'Multi-stage builds, compose orchestration, security hardening.', tags: ['docker','containers','devops'], xp: 700 },
  { id: 'sk-12', title: 'Kubernetes',          category: 'DevOps',   level: 4, maxLevel: 10, isMastered: false, description: 'Pod scheduling, services, ingress, HPA, RBAC policies.', tags: ['k8s','orchestration','cloud'], xp: 400 },
  { id: 'sk-13', title: 'GitHub Actions',      category: 'DevOps',   level: 8, maxLevel: 10, isMastered: false, description: 'CI/CD workflows, matrix builds, reusable actions, OIDC.', tags: ['ci-cd','automation','github'], xp: 800 },
  { id: 'sk-14', title: 'Terraform',           category: 'DevOps',   level: 5, maxLevel: 10, isMastered: false, description: 'Infrastructure as code, modules, state management, workspaces.', tags: ['iac','terraform','cloud'], xp: 500 },
  { id: 'sk-15', title: 'Observability',       category: 'DevOps',   level: 4, maxLevel: 10, isMastered: false, description: 'OpenTelemetry, distributed tracing, metrics dashboards, alerting.', tags: ['monitoring','tracing','logs'], xp: 400 },
  // AI/ML
  { id: 'sk-16', title: 'Prompt Engineering',  category: 'AI/ML',    level: 6, maxLevel: 10, isMastered: false, description: 'Chain-of-thought, few-shot prompting, RAG pipelines.', tags: ['llm','prompting','ai'], xp: 600 },
  { id: 'sk-17', title: 'LangChain/LangGraph', category: 'AI/ML',    level: 4, maxLevel: 10, isMastered: false, description: 'Agentic workflows, tool use, memory, graph-based orchestration.', tags: ['langchain','agents','rag'], xp: 400 },
  { id: 'sk-18', title: 'Vector Databases',    category: 'AI/ML',    level: 3, maxLevel: 10, isMastered: false, description: 'Embeddings, similarity search, pgvector, ANN indexes.', tags: ['vectors','embeddings','search'], xp: 300 },
  { id: 'sk-19', title: 'Fine-Tuning LLMs',    category: 'AI/ML',    level: 2, maxLevel: 10, isMastered: false, description: 'LoRA, PEFT, RLHF, dataset curation, model evaluation.', tags: ['fine-tuning','llm','training'], xp: 200 },
  { id: 'sk-20', title: 'AI Agents & MCP',     category: 'AI/ML',    level: 5, maxLevel: 10, isMastered: false, description: 'Model Context Protocol, tool-calling agents, multi-agent systems.', tags: ['agents','mcp','ai'], xp: 500 },
];
""")

# ── server/data/categories.js ─────────────────────────────────────────────────
w('server/data/categories.js', """\
export const categories = [
  { id: 'cat-1', name: 'Frontend', description: 'UI/UX, React, browser APIs, modern CSS', color: '#60a5fa', icon: '🎨' },
  { id: 'cat-2', name: 'Backend',  description: 'Node.js, databases, REST, GraphQL, microservices', color: '#34d399', icon: '⚙️' },
  { id: 'cat-3', name: 'DevOps',   description: 'CI/CD pipelines, containers, cloud infrastructure', color: '#f97316', icon: '🚀' },
  { id: 'cat-4', name: 'AI/ML',    description: 'Machine learning, LLM integration, model fine-tuning', color: '#a78bfa', icon: '🤖' },
];
""")

# ── server/schema.js ──────────────────────────────────────────────────────────
w('server/schema.js', """\
import { gql } from 'graphql-tag';

// WHY GRAPHQL OVER REST?
// REST needs: GET /skills, GET /skills/:id, GET /categories, GET /stats, PATCH /skills/:id
// GraphQL: ONE endpoint, client asks EXACTLY what it needs — no over-fetching, no under-fetching.

export const typeDefs = gql`
  # Core domain types — strongly typed, self-documenting
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
    # Nested type — resolved only when client requests it
    categoryInfo: Category
  }

  type Category {
    id: ID!
    name: String!
    description: String!
    color: String!
    icon: String!
    # These fields are ONLY resolved when requested (no over-fetching)
    skills: [Skill!]!
    skillCount: Int!
    avgLevel: Float!
  }

  # Aggregated stats — one GraphQL query replaces 3+ REST round trips
  type DashboardStats {
    totalSkills: Int!
    masteredSkills: Int!
    totalXP: Int!
    avgLevel: Float!
    categoryBreakdown: [CategoryStat!]!
  }

  type CategoryStat {
    category: String!
    count: Int!
    avgLevel: Float!
    totalXP: Int!
    color: String!
  }

  # Demo comparison type — rendered in the REST vs GraphQL panel
  type RestVsGraphQL {
    feature: String!
    rest: String!
    graphql: String!
    winner: String!
  }

  # ONE endpoint handles all these queries (REST needs 5+ routes)
  type Query {
    getSkills(category: String, minLevel: Int, tags: [String]): [Skill!]!
    getSkillById(id: ID!): Skill
    getCategories: [Category!]!
    getCategoryByName(name: String!): Category
    getDashboardStats: DashboardStats!
    getRestVsGraphQLComparison: [RestVsGraphQL!]!
  }

  type Mutation {
    levelUpSkill(id: ID!): Skill!
    addTagToSkill(id: ID!, tag: String!): Skill!
    resetSkill(id: ID!): Skill!
  }

  # REAL-TIME — impossible with plain REST without polling hacks
  type Subscription {
    skillLeveledUp: Skill!
    categoryUpdated(categoryName: String!): Category!
  }
`;
""")

# ── server/resolvers.js ───────────────────────────────────────────────────────
w('server/resolvers.js', """\
import { PubSub } from 'graphql-subscriptions';
import { skills } from './data/skills.js';
import { categories } from './data/categories.js';

const pubsub = new PubSub();
const SKILL_LEVELED_UP = 'SKILL_LEVELED_UP';
const CATEGORY_UPDATED = 'CATEGORY_UPDATED';

// Comparison data rendered in the front-end panel
const restVsGraphQLData = [
  { feature: 'Data Fetching', rest: 'Multiple endpoints, over-fetching common', graphql: 'One endpoint — ask exactly what you need', winner: 'GraphQL' },
  { feature: 'Type Safety', rest: 'Manual OpenAPI docs, often stale', graphql: 'Schema IS the contract — always in sync', winner: 'GraphQL' },
  { feature: 'Real-time', rest: 'Polling or SSE workarounds', graphql: 'Built-in Subscriptions over WebSocket', winner: 'GraphQL' },
  { feature: 'Versioning', rest: '/v1, /v2 — breaking changes are painful', graphql: 'Evolve schema with deprecations, no versions', winner: 'GraphQL' },
  { feature: 'Caching', rest: 'HTTP cache headers, CDN-friendly by default', graphql: 'Normalized client cache (Apollo InMemoryCache)', winner: 'REST' },
  { feature: 'File Uploads', rest: 'Multipart form data — straightforward', graphql: 'Requires extra setup (graphql-upload)', winner: 'REST' },
  { feature: 'Tooling', rest: 'Postman, Swagger — mature ecosystem', graphql: 'GraphiQL, Apollo Studio, codegen — great DX', winner: 'GraphQL' },
  { feature: 'Learning Curve', rest: 'Familiar to every developer', graphql: 'Schema, resolvers, N+1 — takes time to master', winner: 'REST' },
];

export const resolvers = {
  Query: {
    // Filtering args in ONE query replaces multiple REST routes
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

    // One round trip replaces GET /stats + GET /categories + aggregation
    getDashboardStats: () => {
      const mastered = skills.filter(s => s.isMastered).length;
      const totalXP = skills.reduce((sum, s) => sum + s.xp, 0);
      const avgLevel = skills.reduce((sum, s) => sum + s.level, 0) / skills.length;
      const breakdown = categories.map(cat => {
        const cs = skills.filter(s => s.category === cat.name);
        return {
          category: cat.name,
          count: cs.length,
          avgLevel: cs.reduce((sum, s) => sum + s.level, 0) / cs.length,
          totalXP: cs.reduce((sum, s) => sum + s.xp, 0),
          color: cat.color,
        };
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
      // Publish to ALL subscribers (cross-tab real-time!)
      pubsub.publish(SKILL_LEVELED_UP, { skillLeveledUp: skill });
      const cat = categories.find(c => c.name === skill.category);
      if (cat) pubsub.publish(CATEGORY_UPDATED, { categoryUpdated: cat, categoryName: skill.category });
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
      skill.level = 1;
      skill.xp = 100;
      skill.isMastered = false;
      return skill;
    },
  },

  Subscription: {
    skillLeveledUp: {
      subscribe: () => pubsub.asyncIterator([SKILL_LEVELED_UP]),
    },
    categoryUpdated: {
      subscribe: () => pubsub.asyncIterator([CATEGORY_UPDATED]),
      resolve: (payload, { categoryName }) => {
        if (payload.categoryName !== categoryName) return null;
        return payload.categoryUpdated;
      },
    },
  },

  // Field-level resolvers — GraphQL's superpower: resolve nested data lazily
  Skill: {
    categoryInfo: (skill) => categories.find(c => c.name === skill.category),
  },
  Category: {
    skills: (cat) => skills.filter(s => s.category === cat.name),
    skillCount: (cat) => skills.filter(s => s.category === cat.name).length,
    avgLevel: (cat) => {
      const cs = skills.filter(s => s.category === cat.name);
      return cs.reduce((sum, s) => sum + s.level, 0) / cs.length;
    },
  },
};
""")

# ── server/index.js ───────────────────────────────────────────────────────────
w('server/index.js', """\
import express from 'express';
import http from 'http';
import cors from 'cors';
import { ApolloServer } from '@apollo/server';
import { expressMiddleware } from '@apollo/server/express4';
import { ApolloServerPluginDrainHttpServer } from '@apollo/server/plugin/drainHttpServer';
import { makeExecutableSchema } from '@graphql-tools/schema';
import { WebSocketServer } from 'ws';
import { useServer } from 'graphql-ws/lib/use/ws';
import { typeDefs } from './schema.js';
import { resolvers } from './resolvers.js';

async function bootstrap() {
  const app = express();
  const httpServer = http.createServer(app);

  // Single schema shared by HTTP (queries/mutations) + WebSocket (subscriptions)
  const schema = makeExecutableSchema({ typeDefs, resolvers });

  // WebSocket server for real-time subscriptions
  const wsServer = new WebSocketServer({ server: httpServer, path: '/graphql' });
  const wsCleanup = useServer({ schema }, wsServer);

  const server = new ApolloServer({
    schema,
    plugins: [
      ApolloServerPluginDrainHttpServer({ httpServer }),
      { async serverWillStart() { return { async drainServer() { await wsCleanup.dispose(); } }; } },
    ],
  });

  await server.start();
  app.use('/graphql', cors({ origin: '*' }), express.json(), expressMiddleware(server));

  // REST comparison routes — these show WHY GraphQL is better
  // REST needs 5 separate endpoints; GraphQL handles all with one /graphql
  app.get('/rest/skills', (_, res) => res.json({ note: 'REST: needs separate endpoints for everything', endpoints: ['/rest/skills', '/rest/skills/:id', '/rest/categories', '/rest/stats'] }));
  app.get('/rest/skills/:id', (req, res) => res.json({ note: 'REST: GET /skills/:id — separate round trip', id: req.params.id }));
  app.get('/rest/categories', (_, res) => res.json({ note: 'REST: GET /categories — yet another round trip' }));
  app.get('/rest/stats', (_, res) => res.json({ note: 'REST: GET /stats — 3rd round trip just for aggregates' }));
  app.patch('/rest/skills/:id/level', (req, res) => res.json({ note: 'REST: PATCH — no real-time push to other clients' }));

  const PORT = 4000;
  httpServer.listen(PORT, () => {
    console.log('');
    console.log('  GraphQL in 2026 — Skill-Tree Dashboard');
    console.log('  =======================================');
    console.log(`  GraphQL : http://localhost:${PORT}/graphql`);
    console.log(`  WS Subs : ws://localhost:${PORT}/graphql`);
    console.log(`  REST cmp: http://localhost:${PORT}/rest/skills`);
    console.log('');
  });
}

bootstrap();
""")

print('\\nAll server files written cleanly.')
