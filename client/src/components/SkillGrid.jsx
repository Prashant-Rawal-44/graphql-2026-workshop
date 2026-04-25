// ─── SkillGrid ────────────────────────────────────────────────────────────────
// Fetches all skills, exposes category filtering, and orchestrates the
// skeleton → card transition. Uses AnimatePresence so filter changes animate
// cards in/out with layout animations.

import { useState }                          from 'react';
import { useQuery }                          from '@apollo/client';
import { motion, AnimatePresence }           from 'framer-motion';
import { GET_SKILLS }                        from '../graphql/queries';
import SkillCard                             from './SkillCard';
import SkillSkeleton                         from './SkillSkeleton';
import CategoryFilter                        from './CategoryFilter';

export default function SkillGrid() {
  const { data, loading, error } = useQuery(GET_SKILLS);
  const [activeCategory, setActiveCategory] = useState('All');

  // ── Error state ────────────────────────────────────────────────────────────
  if (error) {
    return (
      <div className="flex flex-col items-center justify-center py-28 text-center gap-4">
        <span className="text-5xl">⚠️</span>
        <h3 className="text-xl font-mono text-red-400">Connection Error</h3>
        <p className="text-gray-500 font-mono text-sm max-w-sm">{error.message}</p>
        <p className="text-gray-700 font-mono text-xs">
          Make sure the server is running on{' '}
          <span className="text-gray-500">http://localhost:4000</span>
        </p>
      </div>
    );
  }

  // ── Derive display data ────────────────────────────────────────────────────
  const skills     = data?.getSkills ?? [];
  const categories = ['All', ...[...new Set(skills.map((s) => s.category))].sort()];
  const filtered   = activeCategory === 'All'
    ? skills
    : skills.filter((s) => s.category === activeCategory);

  return (
    <div>
      {/* Category filter (hidden during skeleton phase) */}
      {!loading && (
        <CategoryFilter
          categories={categories}
          active={activeCategory}
          onChange={setActiveCategory}
        />
      )}

      {/* ── Skeleton loading state ─────────────────────────────────────────── */}
      {loading && (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
          {Array.from({ length: 8 }).map((_, i) => (
            <SkillSkeleton key={i} />
          ))}
        </div>
      )}

      {/* ── Skill cards ───────────────────────────────────────────────────── */}
      {!loading && (
        <AnimatePresence mode="popLayout">
          <motion.div
            layout
            className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5"
          >
            {filtered.map((skill, i) => (
              <SkillCard key={skill.id} skill={skill} index={i} />
            ))}
          </motion.div>
        </AnimatePresence>
      )}

      {/* ── Empty state ───────────────────────────────────────────────────── */}
      {!loading && filtered.length === 0 && (
        <div className="flex flex-col items-center py-20 gap-3 text-center">
          <span className="text-4xl">🔍</span>
          <p className="text-gray-500 font-mono text-sm">
            No skills in <span className="text-gray-400">{activeCategory}</span> yet.
          </p>
        </div>
      )}
    </div>
  );
}
