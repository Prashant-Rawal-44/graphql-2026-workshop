import { useState } from 'react';
import { useMutation } from '@apollo/client';
import { motion } from 'framer-motion';
import { LEVEL_UP_SKILL, RESET_SKILL } from '../graphql/mutations';

const CATEGORY_COLORS = {
  Frontend: '#60a5fa',
  Backend:  '#34d399',
  DevOps:   '#f97316',
  'AI/ML':  '#a78bfa',
};

export default function SkillCard({ skill }) {
  const [flashing, setFlashing] = useState(false);
  const color = CATEGORY_COLORS[skill.category] || '#60a5fa';
  const pct = Math.round((skill.level / skill.maxLevel) * 100);

  const [levelUp, { loading }] = useMutation(LEVEL_UP_SKILL, {
    variables: { id: skill.id },
    onCompleted: () => {
      setFlashing(true);
      setTimeout(() => setFlashing(false), 600);
    },
  });

  const [reset] = useMutation(RESET_SKILL, { variables: { id: skill.id } });

  return (
    <motion.div
      layout
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, scale: 0.9 }}
      className={`skill-card${flashing ? ' flash' : ''}`}
      style={{ '--card-accent': color }}
    >
      {skill.isMastered && <div className="mastered-badge">✓ Mastered</div>}

      <div className="card-header">
        <h3 className="card-title">{skill.title}</h3>
        <span className="card-cat" style={{ color }}>{skill.category}</span>
      </div>

      <p className="card-desc">{skill.description}</p>

      <div className="card-tags">
        {skill.tags.map(t => <span key={t} className="tag">#{t}</span>)}
      </div>

      <div className="level-row">
        <span className="level-label">Level {skill.level} / {skill.maxLevel}</span>
        <span className="xp-label">{skill.xp} XP</span>
      </div>

      <div className="progress-track">
        <motion.div
          className="progress-bar"
          style={{ backgroundColor: color }}
          animate={{ width: `${pct}%` }}
          transition={{ type: 'spring', stiffness: 120 }}
        />
      </div>

      <div className="card-actions">
        <button
          className="btn-level-up"
          style={{ '--btn-color': color }}
          onClick={() => levelUp()}
          disabled={loading || skill.isMastered}
        >
          {loading ? '...' : skill.isMastered ? 'MAX' : '⬆ Level Up'}
        </button>
        <button className="btn-reset" onClick={() => reset()} title="Reset skill">↺</button>
      </div>
    </motion.div>
  );
}
