// ─── GraphQL Schema ──────────────────────────────────────────────────────────
// Defines the entire public API surface: types, queries, mutations, subscriptions.

export const typeDefs = `#graphql

  # ── Domain type ─────────────────────────────────────────────────────────────
  type Skill {
    id:         ID!
    title:      String!
    category:   String!   # Frontend | Backend | AI | DevOps
    level:      Int!      # 1 – ∞; isMastered flips at level > 5
    isMastered: Boolean!
  }

  # ── Queries ──────────────────────────────────────────────────────────────────
  type Query {
    getSkills:        [Skill!]!
    getSkillById(id: ID!): Skill
  }

  # ── Mutations ─────────────────────────────────────────────────────────────────
  type Mutation {
    """Increment a skill's level by 1 and mark it Mastered when level > 5."""
    levelUpSkill(id: ID!): Skill
  }

  # ── Subscriptions ─────────────────────────────────────────────────────────────
  type Subscription {
    """Fires whenever ANY client levels up a skill – enables real-time cross-tab sync."""
    skillLeveledUp: Skill!
  }
`;
