import { useMutation } from '@apollo/client';
import { motion } from 'framer-motion';
import { LEVEL_UP_SKILL } from '../graphql/mutations';

const CATEGORY_COLORS = {
  Frontend: '#60a5fa', Backend: '#34d399', DevOps: '#f97316', 'AI/ML': '#a78bfa',
};

export default function SkillCard({ skill }) {
  const color = CATEGORY_COLORS[skill.category] || '#60a5fa';
  const pct = Math.round((skill.level / skill.maxLevel) * 100);

  // TODO 3d: Implement useMutation for LEVEL_UP_SKILL
  // HINT: const [levelUp, { loading }] = useMutation(LEVEL_UP_SKILL, {
  //   variables: { id: skill.id },
  // });
  // WHY: When the mutation returns the updated Skill, Apollo Client automatically
  // updates the normalized cache — ALL components showing this skill re-render!
  // With REST PATCH you'd have to manually refetch or update state.
  const levelUp = () => alert('TODO: wire up useMutation');
  const loading = false;

  return (
    <motion.div
      layout
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, scale: 0.9 }}
      className="skill-card"
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
        <motion.div className="progress-bar" style={{ backgroundColor: color }} animate={{ width: pct + '%' }} transition={{ type: 'spring', stiffness: 120 }} />
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
      </div>
    </motion.div>
  );
}
