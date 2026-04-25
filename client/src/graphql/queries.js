// ─── GraphQL Queries ──────────────────────────────────────────────────────────
import { gql } from '@apollo/client';

export const GET_SKILLS = gql`
  query GetSkills {
    getSkills {
      id
      title
      category
      level
      isMastered
    }
  }
`;

export const GET_SKILL_BY_ID = gql`
  query GetSkillById($id: ID!) {
    getSkillById(id: $id) {
      id
      title
      category
      level
      isMastered
    }
  }
`;
