import { useQuery } from '@apollo/client';
import { GET_DASHBOARD_STATS } from '../graphql/queries';

export default function Header() {
  const { data, loading } = useQuery(GET_DASHBOARD_STATS);
  const stats = data?.getDashboardStats;

  return (
    <header className="header-bar">
      <div className="header-inner">
        <div className="header-title">
          <span className="header-logo">⚡</span>
          <div>
            <h1>Skill-Tree Dashboard</h1>
            <p className="header-sub">GraphQL in 2026 · Apollo Server 4 · Real-time Subscriptions</p>
          </div>
        </div>

        {loading ? (
          <div className="header-stats">
            {[1,2,3,4].map(i => <div key={i} className="stat-pill skeleton-shimmer" style={{width:'80px',height:'36px'}} />)}
          </div>
        ) : stats && (
          <div className="header-stats">
            <div className="stat-pill">
              <span className="stat-val">{stats.totalSkills}</span>
              <span className="stat-label">Skills</span>
            </div>
            <div className="stat-pill">
              <span className="stat-val">{stats.masteredSkills}</span>
              <span className="stat-label">Mastered</span>
            </div>
            <div className="stat-pill">
              <span className="stat-val">{stats.avgLevel.toFixed(1)}</span>
              <span className="stat-label">Avg Level</span>
            </div>
            <div className="stat-pill xp">
              <span className="stat-val">{stats.totalXP.toLocaleString()}</span>
              <span className="stat-label">Total XP</span>
            </div>
          </div>
        )}
      </div>
    </header>
  );
}
