import { gql } from '@apollo/client';

export const LEVEL_UP_SKILL = gql`
  mutation LevelUpSkill($id: ID!) {
    levelUpSkill(id: $id) {
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

export const ADD_TAG = gql`
  mutation AddTagToSkill($id: ID!, $tag: String!) {
    addTagToSkill(id: $id, tag: $tag) {
      id
      tags
    }
  }
`;

export const RESET_SKILL = gql`
  mutation ResetSkill($id: ID!) {
    resetSkill(id: $id) {
      id
      level
      xp
      isMastered
    }
  }
`;
