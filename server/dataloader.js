import DataLoader from 'dataloader';
import { categories } from './data/categories.js';

// DataLoader batches ALL categoryInfo resolver calls within a single tick
// into one batch function call — eliminating the N+1 problem.
export function createCategoryLoader() {
  return new DataLoader(async (categoryNames) => {
    console.log(`DataLoader batch: ${categoryNames.length} categories in one call`);
    return categoryNames.map(name => categories.find(c => c.name === name) || null);
  });
}
