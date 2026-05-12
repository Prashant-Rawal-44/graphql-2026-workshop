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
