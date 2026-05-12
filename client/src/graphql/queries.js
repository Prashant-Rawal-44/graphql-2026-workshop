import { gql } from '@apollo/client';

export const GET_SKILLS = gql`
  query GetSkills($category: String, $minLevel: Int, $tags: [String]) {
    getSkills(category: $category, minLevel: $minLevel, tags: $tags) {
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
  }
`;

export const GET_SKILL_BY_ID = gql`
  query GetSkillById($id: ID!) {
    getSkillById(id: $id) {
      id
      title
      category
      level
      maxLevel
      isMastered
      description
      tags
      xp
      categoryInfo {
        id
        name
        color
        icon
        skillCount
        avgLevel
      }
    }
  }
`;

export const GET_CATEGORIES = gql`
  query GetCategories {
    getCategories {
      id
      name
      description
      color
      icon
      skillCount
      avgLevel
    }
  }
`;

export const GET_DASHBOARD_STATS = gql`
  query GetDashboardStats {
    getDashboardStats {
      totalSkills
      masteredSkills
      totalXP
      avgLevel
      categoryBreakdown {
        category
        count
        avgLevel
        totalXP
        color
      }
    }
  }
`;

export const GET_REST_VS_GRAPHQL = gql`
  query GetRestVsGraphQL {
    getRestVsGraphQLComparison {
      feature
      rest
      graphql
      winner
    }
  }
`;
