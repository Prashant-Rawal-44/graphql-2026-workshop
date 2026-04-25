// ─── Resolvers ────────────────────────────────────────────────────────────────
// Pure functions — no framework coupling, easy to unit test.

import { PubSub } from 'graphql-subscriptions';
import { skills } from './data/skills.js';

const pubsub = new PubSub();
const SKILL_LEVELED_UP = 'SKILL_LEVELED_UP';

export const resolvers = {
  // ── Queries ──────────────────────────────────────────────────────────────────
  Query: {
    getSkills: () => skills,

    getSkillById: (_, { id }) =>
      skills.find((s) => s.id === id) ?? null,
  },

  // ── Mutations ─────────────────────────────────────────────────────────────────
  Mutation: {
    levelUpSkill: (_, { id }) => {
      const skill = skills.find((s) => s.id === id);

      if (!skill) {
        throw new Error(`Skill with id "${id}" not found.`);
      }

      // Mutate in-place (fine for a mock store)
      skill.level     += 1;
      skill.isMastered = skill.level > 5;

      // Broadcast to ALL connected WebSocket subscribers (cross-tab magic ✨)
      pubsub.publish(SKILL_LEVELED_UP, { skillLeveledUp: { ...skill } });

      return skill;
    },
  },

  // ── Subscriptions ─────────────────────────────────────────────────────────────
  Subscription: {
    skillLeveledUp: {
      subscribe: () => pubsub.asyncIterator([SKILL_LEVELED_UP]),
    },
  },
};
