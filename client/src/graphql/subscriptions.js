// ─── GraphQL Subscriptions ────────────────────────────────────────────────────
// These are routed to the WebSocket link automatically by the split function
// in apollo/client.js — no extra config needed at the call site.
import { gql } from '@apollo/client';

export const SKILL_LEVELED_UP_SUBSCRIPTION = gql`
  subscription OnSkillLeveledUp {
    skillLeveledUp {
      id
      title
      category
      level
      isMastered
    }
  }
`;
