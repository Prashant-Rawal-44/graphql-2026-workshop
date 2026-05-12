import { useQuery } from '@apollo/client';
import { motion, AnimatePresence } from 'framer-motion';
import { GET_CATEGORIES } from '../graphql/queries';

const ALL_COLORS = { All: '#ffffff' };
const CATEGORY_COLORS = { Frontend: '#60a5fa', Backend: '#34d399', DevOps: '#f97316', 'AI/ML': '#a78bfa' };

export default function CategoryFilter({ selected, onChange }) {
  const { data } = useQuery(GET_CATEGORIES);
  const cats = ['All', ...(data?.getCategories.map(c => c.name) || [])];

  return (
    <div className="filter-bar">
      {cats.map(cat => {
        const active = cat === (selected || 'All');
        const color = CATEGORY_COLORS[cat] || '#ffffff';
        return (
          <button
            key={cat}
            className={`filter-pill${active ? ' active' : ''}`}
            style={active ? { '--pill-color': color, borderColor: color, color } : {}}
            onClick={() => onChange(cat === 'All' ? null : cat)}
          >
            {active && (
              <motion.span
                layoutId="filter-indicator"
                className="filter-dot"
                style={{ backgroundColor: color }}
              />
            )}
            {cat}
          </button>
        );
      })}
    </div>
  );
}
