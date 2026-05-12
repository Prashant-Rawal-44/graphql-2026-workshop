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
