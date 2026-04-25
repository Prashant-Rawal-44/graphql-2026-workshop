// ─── SkillCard ────────────────────────────────────────────────────────────────
// The centrepiece component: glassmorphism card with neon category theming,
// animated level bar, mastered badge, and a Level-Up button.
//
// Animation notes:
//  • Card entrance  → staggered fade+slide via Framer Motion variants
//  • Level number   → scale-pop keyed to skill.level (re-animates on change)
//  • Progress bar   → width animates from 0 on mount + re-animates on level up
//  • Flash overlay  → radial glow burst on successful mutation

import { useState }              from 'react';
import { useMutation }           from '@apollo/client';
import { motion, AnimatePresence } from 'framer-motion';
import { LEVEL_UP_SKILL }        from '../graphql/mutations';

// ── Category visual config ─────────────────────────────────────────────────────
const CATEGORY_CONFIG = {
  Frontend: {
    icon:     '⚡',
    color:    '#00f5ff',
    glow:     'rgba(0, 245, 255, 0.28)',
    border:   'rgba(0, 245, 255, 0.22)',
    bg:       'rgba(0, 245, 255, 0.04)',
    barFrom:  '#00c0ee',
    barTo:    '#00f5ff',
  },
  Backend: {
    icon:     '🔧',
    color:    '#bf00ff',
    glow:     'rgba(191, 0, 255, 0.28)',
    border:   'rgba(191, 0, 255, 0.22)',
    bg:       'rgba(191, 0, 255, 0.04)',
    barFrom:  '#8800cc',
    barTo:    '#bf00ff',
  },
  AI: {
    icon:     '🧠',
    color:    '#00ff88',
    glow:     'rgba(0, 255, 136, 0.28)',
    border:   'rgba(0, 255, 136, 0.22)',
    bg:       'rgba(0, 255, 136, 0.04)',
    barFrom:  '#00cc60',
    barTo:    '#00ff88',
  },
  DevOps: {
    icon:     '🛡️',
    color:    '#ff6b00',
    glow:     'rgba(255, 107, 0, 0.28)',
    border:   'rgba(255, 107, 0, 0.22)',
    bg:       'rgba(255, 107, 0, 0.04)',
    barFrom:  '#cc5200',
    barTo:    '#ff6b00',
  },
};

const MAX_DISPLAY_LEVEL = 10;

// ── Framer Motion variants ─────────────────────────────────────────────────────
const cardVariants = {
  hidden:  { opacity: 0, y: 28,  scale: 0.96 },
  visible: (i) => ({
    opacity: 1, y: 0, scale: 1,
    transition: {
      duration: 0.4,
      delay:    i * 0.065,
      ease:     [0.25, 0.46, 0.45, 0.94],
    },
  }),
  exit: { opacity: 0, scale: 0.94, transition: { duration: 0.18 } },
};

// ─────────────────────────────────────────────────────────────────────────────
export default function SkillCard({ skill, index }) {
  const cfg = CATEGORY_CONFIG[skill.category] ?? CATEGORY_CONFIG.Backend;
  const [flashing, setFlashing] = useState(false);

  const [levelUp, { loading }] = useMutation(LEVEL_UP_SKILL, {
    variables:   { id: skill.id },
    onCompleted: () => {
      setFlashing(true);
      setTimeout(() => setFlashing(false), 900);
    },
  });

  const progress = Math.min((skill.level / MAX_DISPLAY_LEVEL) * 100, 100);

  return (
    <motion.div
      layout
      custom={index}
      variants={cardVariants}
      initial="hidden"
      animate="visible"
      exit="exit"
      whileHover={{ y: -6, transition: { duration: 0.2 } }}
      className="glass-card p-5 flex flex-col gap-4 relative overflow-hidden"
      style={{
        borderColor: cfg.border,
        background:  `linear-gradient(145deg, ${cfg.bg}, rgba(0,0,0,0))`,
      }}
    >
      {/* ── Ambient corner glow (always present, very subtle) ── */}
      <div
        aria-hidden
        className="absolute -top-12 -right-12 w-36 h-36 rounded-full pointer-events-none blur-3xl opacity-20"
        style={{ background: cfg.color }}
      />

      {/* ── Category badge + Mastered pill ── */}
      <div className="relative flex items-center justify-between gap-2">
        <span
          className="inline-flex items-center gap-1.5 text-xs font-mono font-semibold px-2.5 py-1 rounded-lg border shrink-0"
          style={{ color: cfg.color, borderColor: cfg.border, background: cfg.bg }}
        >
          {cfg.icon}&nbsp;{skill.category}
        </span>

        {skill.isMastered && (
          <motion.span
            animate={{ scale: [1, 1.12, 1], opacity: [1, 0.7, 1] }}
            transition={{ duration: 2.4, repeat: Infinity }}
            className="text-xs font-mono font-bold px-2 py-0.5 rounded-lg shrink-0"
            style={{
              color:      '#ffbe00',
              background: 'rgba(255,190,0,0.08)',
              border:     '1px solid rgba(255,190,0,0.22)',
              textShadow: '0 0 10px rgba(255,190,0,0.55)',
            }}
          >
            ✦ MASTERED
          </motion.span>
        )}
      </div>

      {/* ── Skill title ── */}
      <h3 className="font-mono text-base font-semibold text-gray-100 leading-snug">
        {skill.title}
      </h3>

      {/* ── Level display + progress bar ── */}
      <div className="space-y-2">
        <div className="flex justify-between items-baseline">
          <span className="text-[0.6rem] font-mono tracking-[0.25em] text-gray-600 uppercase">
            Level
          </span>

          {/* Pops whenever level changes */}
          <motion.span
            key={`lvl-${skill.level}`}
            initial={{ scale: 1.6, opacity: 0 }}
            animate={{ scale: 1.0, opacity: 1 }}
            transition={{ type: 'spring', stiffness: 380, damping: 20 }}
            className="text-2xl font-bold font-mono leading-none"
            style={{ color: cfg.color, textShadow: `0 0 22px ${cfg.color}90` }}
          >
            {skill.level}
            <span className="text-sm font-normal text-gray-700 ml-0.5">
              /{MAX_DISPLAY_LEVEL}
            </span>
          </motion.span>
        </div>

        {/* Progress track */}
        <div
          className="h-1.5 rounded-full overflow-hidden"
          style={{ background: 'rgba(255,255,255,0.06)' }}
        >
          <motion.div
            key={`bar-${skill.level}`}
            initial={{ width: 0 }}
            animate={{ width: `${progress}%` }}
            transition={{ duration: 0.75, ease: 'easeOut' }}
            className="h-full rounded-full"
            style={{
              background: `linear-gradient(90deg, ${cfg.barFrom}, ${cfg.barTo})`,
              boxShadow:  `0 0 10px ${cfg.color}70`,
            }}
          />
        </div>
      </div>

      {/* ── Level Up button ── */}
      <motion.button
        onClick={() => levelUp()}
        disabled={loading}
        whileTap={{ scale: 0.95 }}
        className="btn-level-up relative z-10 mt-auto"
      >
        <AnimatePresence mode="wait">
          {loading ? (
            <motion.span
              key="loading"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="flex items-center justify-center gap-2"
            >
              <motion.span
                animate={{ rotate: 360 }}
                transition={{ duration: 0.9, repeat: Infinity, ease: 'linear' }}
                style={{ display: 'inline-block' }}
              >
                ⚙
              </motion.span>
              Leveling…
            </motion.span>
          ) : (
            <motion.span
              key="idle"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
            >
              ▲&nbsp;LEVEL UP
            </motion.span>
          )}
        </AnimatePresence>
      </motion.button>

      {/* ── Flash overlay on successful level-up ── */}
      <AnimatePresence>
        {flashing && (
          <motion.div
            aria-hidden
            initial={{ opacity: 0.7 }}
            animate={{ opacity: 0 }}
            exit={{}}
            transition={{ duration: 0.85, ease: 'easeOut' }}
            className="absolute inset-0 rounded-[inherit] pointer-events-none"
            style={{
              background: `radial-gradient(ellipse at center, ${cfg.glow} 0%, transparent 70%)`,
            }}
          />
        )}
      </AnimatePresence>
    </motion.div>
  );
}
