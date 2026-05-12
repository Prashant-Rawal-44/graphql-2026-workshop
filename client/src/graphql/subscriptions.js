import { gql } from '@apollo/client';

export const SKILL_LEVELED_UP = gql`
  subscription OnSkillLeveledUp {
    skillLeveledUp {
      id
      title
      level
      maxLevel
      isMastered
      xp
      category
      tags
    }
  }
`;

export const CATEGORY_UPDATED = gql`
  subscription OnCategoryUpdated($categoryName: String!) {
    categoryUpdated(categoryName: $categoryName) {
      id
      name
      skillCount
      avgLevel
    }
  }
`;
