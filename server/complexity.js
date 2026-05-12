// ── Query Complexity — Protecting Your GraphQL API ───────────────────────────
// Without complexity limits, a malicious client could send:
//   { getCategories { skills { categoryInfo { skills { categoryInfo { ... } } } } } }
// This creates exponential DB calls (N+1 on steroids).
//
// PRODUCTION BEST PRACTICES:
//
// 1. Query Depth Limiting
//    Use: graphql-depth-limit
//    npm install graphql-depth-limit
//
// 2. Query Complexity Analysis
//    Use: graphql-query-complexity
//    npm install graphql-query-complexity
//
// 3. Persisted Queries (APQ)
//    Only allow pre-registered query hashes — blocks arbitrary queries
//    Apollo Client supports this out of the box with:
//    import { createPersistedQueryLink } from '@apollo/client/link/persisted-queries';
//
// 4. Rate Limiting
//    Limit by IP or auth token at the HTTP layer
//
// Example depth limit setup (for index.js):
// import depthLimit from 'graphql-depth-limit';
// const server = new ApolloServer({
//   schema,
//   validationRules: [depthLimit(5)], // Max 5 levels deep
// });
//
// Example complexity setup (for index.js):
// import { createComplexityRule, simpleEstimator } from 'graphql-query-complexity';
// validationRules: [
//   createComplexityRule({
//     estimators: [simpleEstimator({ defaultComplexity: 1 })],
//     maximumComplexity: 100,
//     onComplete: (complexity) => console.log('Query complexity:', complexity),
//   }),
// ],

export const scalingNotes = {
  dataLoader: 'Batch N+1 DB calls into 1 per request cycle',
  depthLimit: 'Prevent deeply nested query attacks',
  complexity: 'Assign cost to fields, reject expensive queries',
  apq: 'Persisted queries — CDN-cacheable, faster, more secure',
  pagination: 'Use cursor-based pagination for large lists (Relay spec)',
  caching: 'Apollo Server Response Cache plugin for field-level TTL',
  federation: 'Apollo Federation — split schema across microservice teams',
};
