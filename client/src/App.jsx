import { useState, useEffect, useRef } from 'react';
// TODO 4e: Import useSubscription from @apollo/client
// import { useSubscription } from '@apollo/client';
import { AnimatePresence } from 'framer-motion';
// TODO 4f: Import the SKILL_LEVELED_UP subscription document
// import { SKILL_LEVELED_UP } from './graphql/subscriptions';
import { useApolloClient, ApolloProvider } from '@apollo/client';
import { client } from './apollo/client';
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
  const apolloClient = useApolloClient();

  const addToast = (msg) => {
    const id = ++toastId.current;
    setToasts(prev => [...prev, { id, msg }]);
    setTimeout(() => setToasts(prev => prev.filter(t => t.id !== id)), 4000);
  };

  // TODO 4g: Add useSubscription hook here
  // useSubscription(SKILL_LEVELED_UP, {
  //   onData: ({ data }) => {
  //     const skill = data?.data?.skillLeveledUp;
  //     if (!skill) return;
  //     setWsConnected(true);
  //     addToast(`⬆ ${skill.title} leveled up to ${skill.level}!`);
  //     // TODO 4h: Update Apollo cache so all components re-render
  //     // apolloClient.cache.modify({
  //     //   id: apolloClient.cache.identify({ __typename: 'Skill', id: skill.id }),
  //     //   fields: {
  //     //     level: () => skill.level,
  //     //     xp: () => skill.xp,
  //     //     isMastered: () => skill.isMastered,
  //     //   },
  //     // });
  //   },
  //   onError: () => setWsConnected(false),
  // });
  //
  // NOTE: Also update client/src/apollo/client.js to use the split link
  // that routes subscriptions to WebSocket and queries/mutations to HTTP.

  useEffect(() => { const t = setTimeout(() => setWsConnected(true), 1000); return () => clearTimeout(t); }, []);

  return (
    <div className="app">
      <LiveIndicator connected={wsConnected} />
      <Header />
      <main className="main-content">
        <RestVsGraphQL />
        <StatsPanel />
        <section className="skills-section">
          <div className="skills-header">
            <h2 className="panel-title"><span className="panel-icon">🎯</span>Skill Tree</h2>
            <CategoryFilter selected={selectedCategory} onChange={setSelectedCategory} />
          </div>
          <SkillGrid selectedCategory={selectedCategory} />
        </section>
      </main>
      <div className="toast-stack">
        <AnimatePresence>
          {toasts.map(t => <Toast key={t.id} message={t.msg} onDone={() => setToasts(prev => prev.filter(x => x.id !== t.id))} />)}
        </AnimatePresence>
      </div>
    </div>
  );
}

export default function AppWithProvider() {
  return <ApolloProvider client={client}><App /></ApolloProvider>;
}
