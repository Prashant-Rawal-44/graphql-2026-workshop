// ─── Mock Database ────────────────────────────────────────────────────────────
// Plain in-memory array — swap for a real DB (Postgres, Mongo, etc.) later.
// Skills start at a variety of levels to make the demo dashboard feel alive.

export const skills = [
  { id: '1',  title: 'React 19',           category: 'Frontend', level: 4, isMastered: false },
  { id: '2',  title: 'GraphQL',            category: 'Backend',  level: 3, isMastered: false },
  { id: '3',  title: 'TypeScript',         category: 'Frontend', level: 5, isMastered: false },
  { id: '4',  title: 'Node.js',            category: 'Backend',  level: 6, isMastered: true  },
  { id: '5',  title: 'Docker',             category: 'DevOps',   level: 2, isMastered: false },
  { id: '6',  title: 'LLM Fine-tuning',    category: 'AI',       level: 1, isMastered: false },
  { id: '7',  title: 'Prompt Engineering', category: 'AI',       level: 4, isMastered: false },
  { id: '8',  title: 'Kubernetes',         category: 'DevOps',   level: 2, isMastered: false },
  { id: '9',  title: 'PostgreSQL',         category: 'Backend',  level: 5, isMastered: false },
  { id: '10', title: 'Tailwind CSS',       category: 'Frontend', level: 6, isMastered: true  },
  { id: '11', title: 'Vector Databases',   category: 'AI',       level: 3, isMastered: false },
  { id: '12', title: 'Rust',               category: 'Backend',  level: 1, isMastered: false },
  { id: '13', title: 'Apollo GraphQL',     category: 'Backend',  level: 5, isMastered: false },
  { id: '14', title: 'RAG Pipelines',      category: 'AI',       level: 2, isMastered: false },
  { id: '15', title: 'CI/CD Pipelines',    category: 'DevOps',   level: 4, isMastered: false },
];
