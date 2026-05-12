import { gql } from '@apollo/client';

// Reusable fragments — a GraphQL best practice for DRY operations
export const SKILL_FRAGMENT = gql`
  fragment SkillFields on Skill {
    id
    title
    category
    level
    maxLevel
    isMastered
    description
    tags
    xp
  }
`;

export const CATEGORY_STAT_FRAGMENT = gql`
  fragment CategoryStatFields on CategoryStat {
    category
    count
    avgLevel
    totalXP
    color
  }
`;
