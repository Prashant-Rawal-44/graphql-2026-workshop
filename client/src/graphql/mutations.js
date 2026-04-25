// ─── GraphQL Mutations ────────────────────────────────────────────────────────
import { gql } from '@apollo/client';

// Apollo's InMemoryCache automatically merges the returned Skill object
// (matched by __typename + id) so the UI updates without a refetch.
export const LEVEL_UP_SKILL = gql`
  mutation LevelUpSkill($id: ID!) {
    levelUpSkill(id: $id) {
      id
      title
      category
      level
      isMastered
    }
  }
`;
