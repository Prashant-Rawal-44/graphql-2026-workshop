// ─── App Root ────────────────────────────────────────────────────────────────
// Owns the real-time subscription listener + toast notifications.
// The subscription cache-write ensures cross-tab updates propagate to every
// SkillCard that reads from the Apollo InMemoryCache — zero prop drilling.

import { useState }                         from 'react';
import { useSubscription, gql }             from '@apollo/client';
import { AnimatePresence }                  from 'framer-motion';

import Header                               from './components/Header';
import SkillGrid                            from './components/SkillGrid';
import LiveIndicator                        from './components/LiveIndicator';
import Toast                                from './components/Toast';
import { SKILL_LEVELED_UP_SUBSCRIPTION }    from './graphql/subscriptions';

// Minimal fragment used only for the cache write — avoids re-importing the full query shape.
const LIVE_SKILL_FRAGMENT = gql`
  fragment LiveSkillUpdate on Skill {
    level
    isMastered
  }
`;

export default function App() {
  const [toasts, setToasts] = useState([]);

  // Push a transient toast that self-destructs after 4 s
  const pushToast = (msg) => {
    const id = Date.now();
    setToasts((prev) => [...prev, { id, msg }]);
    setTimeout(() => setToasts((prev) => prev.filter((t) => t.id !== id)), 4000);
  };

  // ── Live subscription ──────────────────────────────────────────────────────
  // When any client levels up a skill the server broadcasts via WS.
  // We write the updated fields directly into the normalized cache — Apollo
  // re-renders every component that reads those fields automatically.
  useSubscription(SKILL_LEVELED_UP_SUBSCRIPTION, {
    onData: ({ client, data }) => {
      const skill = data.data?.skillLeveledUp;
      if (!skill) return;

      client.cache.writeFragment({
        id:       client.cache.identify({ __typename: 'Skill', id: skill.id }),
        fragment: LIVE_SKILL_FRAGMENT,
        data:     { level: skill.level, isMastered: skill.isMastered },
      });

      pushToast(`⚡ ${skill.title} reached Level ${skill.level}!`);
    },
  });

  return (
    <div className="min-h-screen">
      {/* Fixed top-right LIVE badge */}
      <LiveIndicator />

      <Header />

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-20">
        <SkillGrid />
      </main>

      {/* Toast stack — bottom right */}
      <div className="fixed bottom-6 right-6 flex flex-col gap-3 z-50 pointer-events-none">
        <AnimatePresence>
          {toasts.map((t) => (
            <Toast key={t.id} message={t.msg} />
          ))}
        </AnimatePresence>
      </div>
    </div>
  );
}
