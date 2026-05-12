// ── DataLoader — Solving the N+1 Problem ─────────────────────────────────────
// The N+1 problem: if you have 20 skills and each needs its categoryInfo,
// you'd make 20 database calls (one per skill). With DataLoader, you batch
// them into ONE call per request cycle.
//
// This is critical for scaling GraphQL in production.
//
// Without DataLoader (N+1):
//   getSkills returns 20 skills
//   → For each skill, categoryInfo resolver runs → 20 DB calls = N+1 problem!
//
// With DataLoader:
//   All 20 categoryInfo requests are batched → 1 DB call
//
// TODO 6a: Install DataLoader
//   cd server && npm install dataloader
//
// TODO 6b: Implement the batch function below
// import DataLoader from 'dataloader';
// import { categories } from './data/categories.js';
//
// The batch function receives an array of keys (category names)
// and must return an array of values IN THE SAME ORDER.
//
// export function createCategoryLoader() {
//   return new DataLoader(async (categoryNames) => {
//     // Batch load — instead of N queries, this runs ONCE per request
//     return categoryNames.map(name => categories.find(c => c.name === name) || null);
//   });
// }
//
// TODO 6c: In server/index.js, add the loader to Apollo context:
// expressMiddleware(server, {
//   context: async () => ({ categoryLoader: createCategoryLoader() })
// })
//
// TODO 6d: Use the loader in the Skill.categoryInfo resolver:
// Skill: {
//   categoryInfo: (skill, _, { categoryLoader }) => categoryLoader.load(skill.category),
// }

export function createCategoryLoader() {
  // Stub — implement above
  return { load: (name) => Promise.resolve(null) };
}
