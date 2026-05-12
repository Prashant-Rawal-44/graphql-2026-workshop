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
