// ─── CategoryFilter ───────────────────────────────────────────────────────────
// Animated filter pill row. The shared `layoutId="filter-indicator"` creates
// a smooth sliding underline/border effect as the active category changes.

import { motion } from 'framer-motion';

const PILL_COLORS = {
  All:      { active: '#ffffff',  activeBg: 'rgba(255,255,255,0.08)' },
  Frontend: { active: '#00f5ff',  activeBg: 'rgba(0,245,255,0.09)'   },
  Backend:  { active: '#bf00ff',  activeBg: 'rgba(191,0,255,0.09)'   },
  AI:       { active: '#00ff88',  activeBg: 'rgba(0,255,136,0.09)'   },
  DevOps:   { active: '#ff6b00',  activeBg: 'rgba(255,107,0,0.09)'   },
};

export default function CategoryFilter({ categories, active, onChange }) {
  return (
    <div className="flex flex-wrap gap-2 mb-8">
      {categories.map((cat) => {
        const isActive = cat === active;
        const c = PILL_COLORS[cat] ?? { active: '#ffffff', activeBg: 'rgba(255,255,255,0.08)' };

        return (
          <motion.button
            key={cat}
            onClick={() => onChange(cat)}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            className="relative px-4 py-1.5 rounded-xl font-mono text-xs font-semibold tracking-wider
                       transition-colors duration-200 border"
            style={{
              color:      isActive ? c.active : 'rgba(156,163,175,0.8)',
              background: isActive ? c.activeBg : 'rgba(255,255,255,0.02)',
              borderColor: isActive ? `${c.active}45` : 'rgba(255,255,255,0.06)',
              textShadow: isActive ? `0 0 12px ${c.active}` : 'none',
              boxShadow:  isActive ? `0 0 18px ${c.active}18` : 'none',
            }}
          >
            {cat.toUpperCase()}

            {/* Shared layout animation — slides the active glow ring between pills */}
            {isActive && (
              <motion.span
                layoutId="filter-indicator"
                className="absolute inset-0 rounded-xl pointer-events-none"
                style={{ boxShadow: `inset 0 0 0 1px ${c.active}30` }}
                transition={{ type: 'spring', bounce: 0.18, duration: 0.38 }}
              />
            )}
          </motion.button>
        );
      })}
    </div>
  );
}
