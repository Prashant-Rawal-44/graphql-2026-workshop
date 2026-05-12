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
