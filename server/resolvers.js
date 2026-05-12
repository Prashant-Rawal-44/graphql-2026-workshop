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
