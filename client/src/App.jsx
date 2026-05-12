import { useState } from 'react';
import { ApolloProvider } from '@apollo/client';
import { client } from './apollo/client';
import Header from './components/Header';
import CategoryFilter from './components/CategoryFilter';
import SkillGrid from './components/SkillGrid';
import StatsPanel from './components/StatsPanel';
import RestVsGraphQL from './components/RestVsGraphQL';

// TODO 2f: Wrap your app in ApolloProvider so all components can use useQuery/useMutation
// ApolloProvider makes the Apollo client available throughout the component tree.
// HINT: <ApolloProvider client={client}> ... </ApolloProvider>

function App() {
  const [selectedCategory, setSelectedCategory] = useState(null);

  return (
    <div className="app">
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
    </div>
  );
}

// YOUR CODE HERE — export with ApolloProvider wrapper
export default App;
