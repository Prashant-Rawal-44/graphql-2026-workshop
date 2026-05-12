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
