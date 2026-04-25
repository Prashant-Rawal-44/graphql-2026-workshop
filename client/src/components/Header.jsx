// ─── Header ───────────────────────────────────────────────────────────────────
// Reads skill stats from the cache (no extra network request) and renders
// the dashboard title + summary badges.

import { useQuery }     from '@apollo/client';
import { motion }       from 'framer-motion';
import { GET_SKILLS }   from '../graphql/queries';

export default function Header() {
  const { data } = useQuery(GET_SKILLS);
  const skills   = data?.getSkills ?? [];

  const total    = skills.length;
  const mastered = skills.filter((s) => s.isMastered).length;
  const avgLevel = total > 0
    ? (skills.reduce((sum, s) => sum + s.level, 0) / total).toFixed(1)
    : '—';

  return (
    <header className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-6">
      <motion.div
        initial={{ opacity: 0, y: -18 }}
        animate={{ opacity: 1, y:   0  }}
        transition={{ duration: 0.55, ease: 'easeOut' }}
      >
        {/* ── Logo row ─────────────────────────────────────────────────────── */}
        <div className="flex items-end gap-4 mb-1">
          <motion.span
            className="text-5xl select-none leading-none"
            animate={{ rotate: [0, -12, 12, -6, 0] }}
            transition={{ duration: 1.8, delay: 1.2, repeat: Infinity, repeatDelay: 6 }}
          >
            ⚡
          </motion.span>

          <div>
            <p className="font-mono text-[0.6rem] tracking-[0.35em] text-gray-600 uppercase mb-0.5">
              Apollo GraphQL · 2026
            </p>
            <h1 className="text-4xl md:text-5xl font-extrabold tracking-tight leading-none">
              <span className="neon-cyan font-mono">Skill</span>
              <span className="text-gray-100"> Tree</span>
            </h1>
          </div>
        </div>

        <p className="ml-[4.5rem] font-mono text-sm text-gray-500 mb-8">
          Your personal tech RPG — master the stack, one level at a time.
        </p>

        {/* ── Stat badges ───────────────────────────────────────────────────── */}
        {total > 0 && (
          <motion.div
            className="ml-[4.5rem] flex flex-wrap gap-3"
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.35 }}
          >
            <StatBadge label="Skills"   value={total}    color="cyan"   />
            <StatBadge label="Mastered" value={mastered} color="green"  />
            <StatBadge label="Avg Lvl"  value={avgLevel} color="purple" />
          </motion.div>
        )}
      </motion.div>

      {/* Divider */}
      <div className="mt-8 h-px bg-gradient-to-r from-transparent via-white/10 to-transparent" />
    </header>
  );
}

// ── StatBadge sub-component ───────────────────────────────────────────────────
const BADGE_COLORS = {
  cyan:   { text: '#00f5ff', border: 'rgba(0,245,255,0.2)',   bg: 'rgba(0,245,255,0.06)'   },
  green:  { text: '#00ff88', border: 'rgba(0,255,136,0.2)',   bg: 'rgba(0,255,136,0.06)'   },
  purple: { text: '#bf00ff', border: 'rgba(191,0,255,0.2)',   bg: 'rgba(191,0,255,0.06)'   },
};

function StatBadge({ label, value, color }) {
  const c = BADGE_COLORS[color];
  return (
    <div
      className="glass-card px-4 py-2 flex flex-col items-center min-w-[76px]"
      style={{ borderColor: c.border, background: c.bg }}
    >
      <span
        className="text-2xl font-bold font-mono leading-tight"
        style={{ color: c.text, textShadow: `0 0 14px ${c.text}` }}
      >
        {value}
      </span>
      <span className="text-[0.6rem] font-mono tracking-widest text-gray-500 uppercase">
        {label}
      </span>
    </div>
  );
}
