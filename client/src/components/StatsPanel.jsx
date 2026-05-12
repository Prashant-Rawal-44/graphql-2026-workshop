import { useQuery } from '@apollo/client';
import { motion } from 'framer-motion';
import { GET_DASHBOARD_STATS } from '../graphql/queries';

export default function StatsPanel() {
  const { data, loading } = useQuery(GET_DASHBOARD_STATS);
  const breakdown = data?.getDashboardStats?.categoryBreakdown || [];

  return (
    <section className="stats-panel">
      <h2 className="panel-title">
        <span className="panel-icon">📊</span>
        Category Breakdown
        <span className="panel-hint">— one GraphQL query, nested data</span>
      </h2>

      {loading ? (
        <div className="stats-grid">
          {[1,2,3,4].map(i => <div key={i} className="stat-card skeleton-shimmer" style={{height:'100px'}} />)}
        </div>
      ) : (
        <div className="stats-grid">
          {breakdown.map((cat, i) => (
            <motion.div
              key={cat.category}
              className="stat-card"
              style={{ '--cat-color': cat.color }}
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: i * 0.1 }}
            >
              <div className="stat-cat-name" style={{ color: cat.color }}>{cat.category}</div>
              <div className="stat-cat-row">
                <div>
                  <div className="stat-cat-val">{cat.count}</div>
                  <div className="stat-cat-label">Skills</div>
                </div>
                <div>
                  <div className="stat-cat-val">{cat.avgLevel.toFixed(1)}</div>
                  <div className="stat-cat-label">Avg Level</div>
                </div>
                <div>
                  <div className="stat-cat-val">{cat.totalXP.toLocaleString()}</div>
                  <div className="stat-cat-label">XP</div>
                </div>
              </div>
              <div className="stat-cat-bar-track">
                <motion.div
                  className="stat-cat-bar"
                  style={{ backgroundColor: cat.color }}
                  initial={{ width: 0 }}
                  animate={{ width: `${(cat.avgLevel / 10) * 100}%` }}
                  transition={{ delay: i * 0.1 + 0.3, type: 'spring', stiffness: 80 }}
                />
              </div>
            </motion.div>
          ))}
        </div>
      )}
    </section>
  );
}
