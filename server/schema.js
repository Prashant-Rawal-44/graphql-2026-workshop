import { gql } from 'graphql-tag';

// ── STARTER BRANCH ─────────────────────────────────────────────────────────────
// The server is just a bare Express app with no GraphQL yet.
// You can compare this with the REST endpoints below.
// Goal: understand what REST gives you — and what it lacks.

export const typeDefs = gql`
  type Query {
    hello: String
  }
`;
