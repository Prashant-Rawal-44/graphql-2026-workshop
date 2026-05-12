import os

B = '/Users/prashant/Desktop/Project-graphQL'

def w(path, content):
    full = os.path.join(B, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w') as f:
        f.write(content)
    print(f'  wrote {path}')

# ── client/src/apollo/client.js ───────────────────────────────────────────────
w('client/src/apollo/client.js', """\
import { ApolloClient, InMemoryCache, HttpLink, split } from '@apollo/client';
import { GraphQLWsLink } from '@apollo/client/link/subscriptions';
import { createClient } from 'graphql-ws';
import { getMainDefinition } from '@apollo/client/utilities';

// HTTP link — handles Queries and Mutations
const httpLink = new HttpLink({ uri: 'http://localhost:4000/graphql' });

// WebSocket link — handles Subscriptions (real-time)
const wsLink = new GraphQLWsLink(
  createClient({ url: 'ws://localhost:4000/graphql', retryAttempts: 5 })
);

// Route: Subscriptions -> WS, everything else -> HTTP
const splitLink = split(
  ({ query }) => {
    const def = getMainDefinition(query);
    return def.kind === 'OperationDefinition' && def.operation === 'subscription';
  },
  wsLink,
  httpLink
);

export const client = new ApolloClient({
  link: splitLink,
  cache: new InMemoryCache({
    typePolicies: {
      Skill: { keyFields: ['id'] },
      Category: { keyFields: ['id'] },
    },
  }),
});
""")

# ── client/src/graphql/queries.js ─────────────────────────────────────────────
w('client/src/graphql/queries.js', """\
import { gql } from '@apollo/client';

export const GET_SKILLS = gql`
  query GetSkills($category: String, $minLevel: Int, $tags: [String]) {
    getSkills(category: $category, minLevel: $minLevel, tags: $tags) {
      id
      title
      category
      level
      maxLevel
      isMastered
      description
      tags
      xp
    }
  }
`;

export const GET_SKILL_BY_ID = gql`
  query GetSkillById($id: ID!) {
    getSkillById(id: $id) {
      id
      title
      category
      level
      maxLevel
      isMastered
      description
      tags
      xp
      categoryInfo {
        id
        name
        color
        icon
        skillCount
        avgLevel
      }
    }
  }
`;

export const GET_CATEGORIES = gql`
  query GetCategories {
    getCategories {
      id
      name
      description
      color
      icon
      skillCount
      avgLevel
    }
  }
`;

export const GET_DASHBOARD_STATS = gql`
  query GetDashboardStats {
    getDashboardStats {
      totalSkills
      masteredSkills
      totalXP
      avgLevel
      categoryBreakdown {
        category
        count
        avgLevel
        totalXP
        color
      }
    }
  }
`;

export const GET_REST_VS_GRAPHQL = gql`
  query GetRestVsGraphQL {
    getRestVsGraphQLComparison {
      feature
      rest
      graphql
      winner
    }
  }
`;
""")

# ── client/src/graphql/mutations.js ───────────────────────────────────────────
w('client/src/graphql/mutations.js', """\
import { gql } from '@apollo/client';

export const LEVEL_UP_SKILL = gql`
  mutation LevelUpSkill($id: ID!) {
    levelUpSkill(id: $id) {
      id
      title
      level
      maxLevel
      isMastered
      xp
      category
      tags
    }
  }
`;

export const ADD_TAG = gql`
  mutation AddTagToSkill($id: ID!, $tag: String!) {
    addTagToSkill(id: $id, tag: $tag) {
      id
      tags
    }
  }
`;

export const RESET_SKILL = gql`
  mutation ResetSkill($id: ID!) {
    resetSkill(id: $id) {
      id
      level
      xp
      isMastered
    }
  }
`;
""")

# ── client/src/graphql/subscriptions.js ───────────────────────────────────────
w('client/src/graphql/subscriptions.js', """\
import { gql } from '@apollo/client';

export const SKILL_LEVELED_UP = gql`
  subscription OnSkillLeveledUp {
    skillLeveledUp {
      id
      title
      level
      maxLevel
      isMastered
      xp
      category
      tags
    }
  }
`;

export const CATEGORY_UPDATED = gql`
  subscription OnCategoryUpdated($categoryName: String!) {
    categoryUpdated(categoryName: $categoryName) {
      id
      name
      skillCount
      avgLevel
    }
  }
`;
""")

# ── client/src/graphql/fragments.js ───────────────────────────────────────────
w('client/src/graphql/fragments.js', """\
import { gql } from '@apollo/client';

// Reusable fragments — a GraphQL best practice for DRY operations
export const SKILL_FRAGMENT = gql`
  fragment SkillFields on Skill {
    id
    title
    category
    level
    maxLevel
    isMastered
    description
    tags
    xp
  }
`;

export const CATEGORY_STAT_FRAGMENT = gql`
  fragment CategoryStatFields on CategoryStat {
    category
    count
    avgLevel
    totalXP
    color
  }
`;
""")

# ── client/src/components/Header.jsx ──────────────────────────────────────────
w('client/src/components/Header.jsx', """\
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
""")

# ── client/src/components/SkillCard.jsx ───────────────────────────────────────
w('client/src/components/SkillCard.jsx', """\
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
""")

# ── client/src/components/SkillGrid.jsx ───────────────────────────────────────
w('client/src/components/SkillGrid.jsx', """\
import { useQuery } from '@apollo/client';
import { AnimatePresence } from 'framer-motion';
import { GET_SKILLS } from '../graphql/queries';
import SkillCard from './SkillCard';
import SkillSkeleton from './SkillSkeleton';

export default function SkillGrid({ selectedCategory }) {
  const { data, loading, error } = useQuery(GET_SKILLS, {
    variables: selectedCategory ? { category: selectedCategory } : {},
  });

  if (error) return (
    <div className="error-msg">
      <p>GraphQL Error: {error.message}</p>
      <p style={{fontSize:'0.8rem',opacity:0.6}}>Is the server running? cd server && npm run dev</p>
    </div>
  );

  if (loading) return (
    <div className="skill-grid">
      {Array.from({ length: 8 }).map((_, i) => <SkillSkeleton key={i} />)}
    </div>
  );

  return (
    <div className="skill-grid">
      <AnimatePresence mode="popLayout">
        {data?.getSkills.map(skill => (
          <SkillCard key={skill.id} skill={skill} />
        ))}
      </AnimatePresence>
    </div>
  );
}
""")

# ── client/src/components/SkillSkeleton.jsx ───────────────────────────────────
w('client/src/components/SkillSkeleton.jsx', """\
export default function SkillSkeleton() {
  return (
    <div className="skill-card skeleton-card">
      <div className="skeleton-shimmer" style={{width:'60%',height:'18px',borderRadius:'4px',marginBottom:'8px'}} />
      <div className="skeleton-shimmer" style={{width:'35%',height:'12px',borderRadius:'4px',marginBottom:'12px'}} />
      <div className="skeleton-shimmer" style={{width:'100%',height:'10px',borderRadius:'4px',marginBottom:'6px'}} />
      <div className="skeleton-shimmer" style={{width:'80%',height:'10px',borderRadius:'4px',marginBottom:'16px'}} />
      <div className="skeleton-shimmer" style={{width:'100%',height:'6px',borderRadius:'3px',marginBottom:'12px'}} />
      <div className="skeleton-shimmer" style={{width:'100%',height:'34px',borderRadius:'6px'}} />
    </div>
  );
}
""")

# ── client/src/components/CategoryFilter.jsx ──────────────────────────────────
w('client/src/components/CategoryFilter.jsx', """\
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
""")

# ── client/src/components/LiveIndicator.jsx ───────────────────────────────────
w('client/src/components/LiveIndicator.jsx', """\
export default function LiveIndicator({ connected = true }) {
  return (
    <div className={`live-indicator ${connected ? 'live' : 'disconnected'}`}>
      <span className="live-dot" />
      <span>{connected ? 'Live' : 'Offline'}</span>
    </div>
  );
}
""")

# ── client/src/components/Toast.jsx ───────────────────────────────────────────
w('client/src/components/Toast.jsx', """\
import { motion } from 'framer-motion';

export default function Toast({ message, onDone }) {
  return (
    <motion.div
      className="toast"
      initial={{ x: 120, opacity: 0 }}
      animate={{ x: 0, opacity: 1 }}
      exit={{ x: 120, opacity: 0 }}
      transition={{ type: 'spring', stiffness: 200, damping: 20 }}
      onAnimationComplete={(_def) => {
        if (_def.opacity === 0) onDone();
      }}
    >
      {message}
    </motion.div>
  );
}
""")

# ── client/src/components/RestVsGraphQL.jsx ───────────────────────────────────
w('client/src/components/RestVsGraphQL.jsx', """\
import { useQuery } from '@apollo/client';
import { motion } from 'framer-motion';
import { GET_REST_VS_GRAPHQL } from '../graphql/queries';

export default function RestVsGraphQL() {
  const { data, loading } = useQuery(GET_REST_VS_GRAPHQL);

  return (
    <section className="comparison-panel">
      <h2 className="panel-title">
        <span className="panel-icon">⚔</span>
        REST vs GraphQL — Why Switch in 2026?
      </h2>
      <p className="panel-sub">
        This data is fetched from a single GraphQL query (<code>getRestVsGraphQLComparison</code>).
        With REST you'd need a separate endpoint for this, plus one for skills, categories, and stats — 4 round trips vs 1.
      </p>

      {loading ? (
        <div className="comparison-grid">
          {Array.from({length:6}).map((_,i) => (
            <div key={i} className="comparison-row skeleton-shimmer" style={{height:'64px',borderRadius:'8px'}} />
          ))}
        </div>
      ) : (
        <div className="comparison-grid">
          <div className="comparison-header">
            <span>Feature</span>
            <span>REST</span>
            <span>GraphQL</span>
            <span>Winner</span>
          </div>
          {data?.getRestVsGraphQLComparison.map((row, i) => (
            <motion.div
              key={row.feature}
              className="comparison-row"
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: i * 0.07 }}
            >
              <span className="cmp-feature">{row.feature}</span>
              <span className="cmp-rest">{row.rest}</span>
              <span className="cmp-gql">{row.graphql}</span>
              <span className={`cmp-winner ${row.winner.toLowerCase()}`}>{row.winner}</span>
            </motion.div>
          ))}
        </div>
      )}
    </section>
  );
}
""")

# ── client/src/components/StatsPanel.jsx ──────────────────────────────────────
w('client/src/components/StatsPanel.jsx', """\
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
""")

# ── client/src/App.jsx ────────────────────────────────────────────────────────
w('client/src/App.jsx', """\
import { useState, useEffect, useRef } from 'react';
import { useSubscription } from '@apollo/client';
import { AnimatePresence } from 'framer-motion';
import { SKILL_LEVELED_UP } from './graphql/subscriptions';
import { GET_SKILLS } from './graphql/queries';
import { useApolloClient } from '@apollo/client';
import Header from './components/Header';
import CategoryFilter from './components/CategoryFilter';
import SkillGrid from './components/SkillGrid';
import StatsPanel from './components/StatsPanel';
import RestVsGraphQL from './components/RestVsGraphQL';
import LiveIndicator from './components/LiveIndicator';
import Toast from './components/Toast';

function App() {
  const [selectedCategory, setSelectedCategory] = useState(null);
  const [toasts, setToasts] = useState([]);
  const [wsConnected, setWsConnected] = useState(false);
  const toastId = useRef(0);
  const client = useApolloClient();

  const addToast = (msg) => {
    const id = ++toastId.current;
    setToasts(prev => [...prev, { id, msg }]);
    setTimeout(() => setToasts(prev => prev.filter(t => t.id !== id)), 4000);
  };

  // Real-time subscription — updates Apollo cache + shows toast
  useSubscription(SKILL_LEVELED_UP, {
    onData: ({ data }) => {
      if (!data?.data?.skillLeveledUp) return;
      setWsConnected(true);
      const skill = data.data.skillLeveledUp;
      addToast(`⬆ ${skill.title} leveled up to ${skill.level}!`);

      // Write directly to normalized cache — all queries using this skill auto-update
      client.cache.modify({
        id: client.cache.identify({ __typename: 'Skill', id: skill.id }),
        fields: {
          level: () => skill.level,
          xp: () => skill.xp,
          isMastered: () => skill.isMastered,
        },
      });
    },
    onError: () => setWsConnected(false),
  });

  useEffect(() => {
    const t = setTimeout(() => setWsConnected(true), 1000);
    return () => clearTimeout(t);
  }, []);

  return (
    <div className="app">
      <LiveIndicator connected={wsConnected} />
      <Header />

      <main className="main-content">
        <RestVsGraphQL />
        <StatsPanel />

        <section className="skills-section">
          <div className="skills-header">
            <h2 className="panel-title">
              <span className="panel-icon">🎯</span>
              Skill Tree
            </h2>
            <CategoryFilter selected={selectedCategory} onChange={setSelectedCategory} />
          </div>
          <SkillGrid selectedCategory={selectedCategory} />
        </section>
      </main>

      <div className="toast-stack">
        <AnimatePresence>
          {toasts.map(t => (
            <Toast key={t.id} message={t.msg} onDone={() => setToasts(prev => prev.filter(x => x.id !== t.id))} />
          ))}
        </AnimatePresence>
      </div>
    </div>
  );
}

export default App;
""")

# ── client/src/main.jsx ───────────────────────────────────────────────────────
w('client/src/main.jsx', """\
import React from 'react';
import ReactDOM from 'react-dom/client';
import { ApolloProvider } from '@apollo/client';
import { client } from './apollo/client';
import App from './App';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <ApolloProvider client={client}>
      <App />
    </ApolloProvider>
  </React.StrictMode>
);
""")

# ── client/src/index.css ──────────────────────────────────────────────────────
w('client/src/index.css', """\
/* ── Reset & Variables ─────────────────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --bg:       #0a0a0f;
  --surface:  rgba(255,255,255,0.04);
  --border:   rgba(255,255,255,0.08);
  --text:     #e2e8f0;
  --muted:    #64748b;
  --accent:   #60a5fa;
  --green:    #34d399;
  --orange:   #f97316;
  --purple:   #a78bfa;
  --radius:   12px;
}

body {
  background: var(--bg);
  color: var(--text);
  font-family: 'Inter', system-ui, sans-serif;
  font-size: 14px;
  line-height: 1.6;
  min-height: 100vh;
  background-image:
    radial-gradient(ellipse 80% 50% at 20% 20%, rgba(96,165,250,0.06) 0%, transparent 60%),
    radial-gradient(ellipse 60% 40% at 80% 80%, rgba(167,139,250,0.05) 0%, transparent 60%);
}

/* ── Header ────────────────────────────────────────────────────────────────── */
.header-bar {
  position: sticky; top: 0; z-index: 50;
  background: rgba(10,10,15,0.85);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  padding: 0 24px;
}
.header-inner {
  max-width: 1280px; margin: 0 auto;
  display: flex; align-items: center; justify-content: space-between;
  height: 64px; gap: 16px;
}
.header-title { display: flex; align-items: center; gap: 12px; }
.header-logo { font-size: 1.6rem; }
.header-title h1 { font-size: 1.15rem; font-weight: 700; color: #fff; }
.header-sub { font-size: 0.72rem; color: var(--muted); }
.header-stats { display: flex; gap: 8px; flex-wrap: wrap; }
.stat-pill {
  display: flex; flex-direction: column; align-items: center;
  padding: 4px 14px; border-radius: 20px;
  background: var(--surface); border: 1px solid var(--border);
  min-width: 68px;
}
.stat-pill.xp { border-color: rgba(167,139,250,0.3); }
.stat-val { font-size: 1rem; font-weight: 700; color: #fff; }
.stat-label { font-size: 0.65rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.04em; }

/* ── Main layout ────────────────────────────────────────────────────────────── */
.app { display: flex; flex-direction: column; min-height: 100vh; }
.main-content { max-width: 1280px; margin: 0 auto; padding: 32px 24px; width: 100%; display: flex; flex-direction: column; gap: 40px; }

/* ── Panel titles ──────────────────────────────────────────────────────────── */
.panel-title {
  font-size: 1.05rem; font-weight: 700; color: #fff;
  display: flex; align-items: center; gap: 8px; margin-bottom: 16px;
}
.panel-icon { font-size: 1.1rem; }
.panel-hint { font-size: 0.72rem; color: var(--muted); font-weight: 400; }
.panel-sub { font-size: 0.8rem; color: var(--muted); margin-bottom: 20px; line-height: 1.5; }
.panel-sub code { background: rgba(255,255,255,0.08); padding: 2px 6px; border-radius: 4px; font-family: monospace; color: var(--accent); }

/* ── REST vs GraphQL comparison ─────────────────────────────────────────────── */
.comparison-panel { }
.comparison-grid { display: flex; flex-direction: column; gap: 6px; }
.comparison-header {
  display: grid; grid-template-columns: 1.4fr 2fr 2fr 1fr;
  padding: 8px 16px; font-size: 0.7rem; text-transform: uppercase;
  letter-spacing: 0.06em; color: var(--muted);
}
.comparison-row {
  display: grid; grid-template-columns: 1.4fr 2fr 2fr 1fr;
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 8px; padding: 12px 16px; align-items: start; gap: 12px;
  transition: background 0.2s;
}
.comparison-row:hover { background: rgba(255,255,255,0.06); }
.cmp-feature { font-weight: 600; color: #fff; font-size: 0.82rem; }
.cmp-rest  { font-size: 0.78rem; color: #f87171; }
.cmp-gql   { font-size: 0.78rem; color: var(--green); }
.cmp-winner { font-size: 0.75rem; font-weight: 700; padding: 2px 10px; border-radius: 20px; text-align: center; }
.cmp-winner.graphql { background: rgba(52,211,153,0.15); color: var(--green); border: 1px solid rgba(52,211,153,0.3); }
.cmp-winner.rest    { background: rgba(248,113,113,0.12); color: #f87171; border: 1px solid rgba(248,113,113,0.3); }

/* ── Stats panel ─────────────────────────────────────────────────────────────── */
.stats-panel { }
.stats-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px,1fr)); gap: 16px; }
.stat-card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 16px;
  border-top: 2px solid var(--cat-color, var(--accent));
}
.stat-cat-name { font-size: 0.95rem; font-weight: 700; margin-bottom: 10px; }
.stat-cat-row { display: flex; justify-content: space-between; margin-bottom: 12px; }
.stat-cat-val { font-size: 1.15rem; font-weight: 700; color: #fff; }
.stat-cat-label { font-size: 0.65rem; color: var(--muted); }
.stat-cat-bar-track { height: 4px; background: rgba(255,255,255,0.06); border-radius: 2px; overflow: hidden; }
.stat-cat-bar { height: 100%; border-radius: 2px; }

/* ── Skills section ───────────────────────────────────────────────────────────── */
.skills-section { }
.skills-header { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; margin-bottom: 20px; }

/* ── Category filter ─────────────────────────────────────────────────────────── */
.filter-bar { display: flex; gap: 8px; flex-wrap: wrap; }
.filter-pill {
  position: relative; display: flex; align-items: center; gap: 6px;
  padding: 5px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: 500;
  background: var(--surface); border: 1px solid var(--border); color: var(--muted);
  cursor: pointer; transition: all 0.2s;
}
.filter-pill:hover { color: #fff; border-color: rgba(255,255,255,0.2); }
.filter-pill.active { color: var(--pill-color, #fff); }
.filter-dot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }

/* ── Skill grid & cards ───────────────────────────────────────────────────────── */
.skill-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; }

.skill-card {
  position: relative;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 18px;
  transition: border-color 0.2s, box-shadow 0.2s;
  border-left: 3px solid var(--card-accent, var(--accent));
}
.skill-card:hover { border-color: rgba(255,255,255,0.14); box-shadow: 0 4px 24px rgba(0,0,0,0.3); }
.skill-card.flash { animation: flash-anim 0.55s ease; }
@keyframes flash-anim { 0%,100% { background: var(--surface); } 40% { background: rgba(96,165,250,0.12); } }

.mastered-badge {
  position: absolute; top: 12px; right: 12px;
  font-size: 0.65rem; font-weight: 700; color: var(--green);
  background: rgba(52,211,153,0.12); border: 1px solid rgba(52,211,153,0.3);
  padding: 2px 8px; border-radius: 12px;
}
.card-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 6px; }
.card-title { font-size: 0.95rem; font-weight: 700; color: #fff; flex: 1; padding-right: 8px; }
.card-cat { font-size: 0.7rem; font-weight: 600; }
.card-desc { font-size: 0.78rem; color: var(--muted); margin-bottom: 10px; line-height: 1.5; }

.card-tags { display: flex; gap: 4px; flex-wrap: wrap; margin-bottom: 12px; }
.tag { font-size: 0.65rem; color: var(--muted); background: rgba(255,255,255,0.05); padding: 2px 8px; border-radius: 10px; }

.level-row { display: flex; justify-content: space-between; font-size: 0.72rem; margin-bottom: 6px; }
.level-label { color: #fff; font-weight: 600; }
.xp-label { color: var(--muted); }

.progress-track { height: 5px; background: rgba(255,255,255,0.06); border-radius: 3px; overflow: hidden; margin-bottom: 14px; }
.progress-bar { height: 100%; border-radius: 3px; transition: width 0.5s ease; }

.card-actions { display: flex; gap: 8px; }
.btn-level-up {
  flex: 1; padding: 8px; border-radius: 8px; font-size: 0.8rem; font-weight: 600;
  background: transparent; color: var(--btn-color, var(--accent));
  border: 1px solid var(--btn-color, var(--accent));
  cursor: pointer; transition: all 0.2s;
}
.btn-level-up:hover:not(:disabled) { background: rgba(96,165,250,0.1); box-shadow: 0 0 12px rgba(96,165,250,0.2); }
.btn-level-up:disabled { opacity: 0.4; cursor: not-allowed; }
.btn-reset { padding: 8px 12px; border-radius: 8px; background: rgba(255,255,255,0.04); border: 1px solid var(--border); color: var(--muted); cursor: pointer; font-size: 0.85rem; transition: all 0.2s; }
.btn-reset:hover { color: #fff; background: rgba(255,255,255,0.08); }

/* ── Skeletons ────────────────────────────────────────────────────────────────── */
.skeleton-shimmer {
  background: linear-gradient(90deg, rgba(255,255,255,0.04) 25%, rgba(255,255,255,0.08) 50%, rgba(255,255,255,0.04) 75%);
  background-size: 200% 100%;
  animation: shimmer 1.6s infinite;
}
@keyframes shimmer { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }
.skeleton-card { pointer-events: none; }

/* ── Live indicator ───────────────────────────────────────────────────────────── */
.live-indicator {
  position: fixed; top: 16px; right: 16px; z-index: 100;
  display: flex; align-items: center; gap: 6px;
  padding: 4px 12px; border-radius: 20px; font-size: 0.72rem; font-weight: 600;
  background: rgba(10,10,15,0.9); border: 1px solid rgba(52,211,153,0.3);
  color: var(--green); backdrop-filter: blur(10px);
}
.live-indicator.disconnected { border-color: rgba(248,113,113,0.3); color: #f87171; }
.live-dot {
  width: 7px; height: 7px; border-radius: 50%; background: var(--green);
  animation: pulse 1.5s infinite;
}
.live-indicator.disconnected .live-dot { background: #f87171; animation: none; }
@keyframes pulse { 0%,100% { opacity:1; transform:scale(1); } 50% { opacity:0.4; transform:scale(0.8); } }

/* ── Toast stack ──────────────────────────────────────────────────────────────── */
.toast-stack { position: fixed; bottom: 24px; right: 24px; z-index: 200; display: flex; flex-direction: column; gap: 8px; }
.toast {
  background: rgba(20,20,30,0.95); border: 1px solid rgba(52,211,153,0.3);
  color: var(--green); padding: 10px 18px; border-radius: 10px; font-size: 0.82rem; font-weight: 600;
  backdrop-filter: blur(10px); box-shadow: 0 4px 20px rgba(0,0,0,0.4);
  white-space: nowrap;
}

/* ── Error ────────────────────────────────────────────────────────────────────── */
.error-msg { text-align: center; padding: 40px; color: #f87171; }

/* ── Responsive ───────────────────────────────────────────────────────────────── */
@media (max-width: 768px) {
  .main-content { padding: 16px; gap: 28px; }
  .header-stats { display: none; }
  .comparison-header, .comparison-row { grid-template-columns: 1fr 1fr; }
  .cmp-rest, .cmp-winner { display: none; }
}
""")

print('\\nAll client files written cleanly.')
