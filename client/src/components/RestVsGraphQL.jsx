import { useQuery } from '@apollo/client';
import { motion } from 'framer-motion';
import { GET_REST_VS_GRAPHQL } from '../graphql/queries';

// TODO 5a: This component fetches comparison data FROM GraphQL and renders a table.
// The entire comparison table is data-driven — the server controls the content.
// This demonstrates that GraphQL is flexible enough to serve ANY shape of data.
//
// TASK: Complete the query below, then render the comparison rows.
// The data comes from getRestVsGraphQLComparison query which returns:
//   { feature, rest, graphql, winner }
//
// BONUS: Notice how this component fetches data WITHOUT prop drilling.
// Any component can call useQuery() and get exactly what it needs.
// With REST you'd have to pass the comparison data down from a parent, or make
// a separate fetch call with its own loading/error state.

export default function RestVsGraphQL() {
  // TODO 5b: Uncomment and complete this query
  // const { data, loading } = useQuery(GET_REST_VS_GRAPHQL);

  // DEMO DATA — replace with real query result
  const loading = false;
  const data = {
    getRestVsGraphQLComparison: [
      { feature: 'Data Fetching', rest: 'Multiple endpoints', graphql: 'One endpoint', winner: 'GraphQL' },
      { feature: 'Type Safety', rest: 'Manual docs', graphql: 'Schema contract', winner: 'GraphQL' },
      { feature: 'Real-time', rest: 'Polling / SSE', graphql: 'Built-in Subscriptions', winner: 'GraphQL' },
    ],
  };

  return (
    <section className="comparison-panel">
      <h2 className="panel-title">
        <span className="panel-icon">⚔</span>
        REST vs GraphQL — Why Switch in 2026?
      </h2>
      <p className="panel-sub">
        This data is fetched from a single GraphQL query (<code>getRestVsGraphQLComparison</code>).
        {/* TODO 5c: Add a note about how many REST calls this would replace */}
      </p>

      {loading ? (
        <p>Loading...</p>
      ) : (
        <div className="comparison-grid">
          <div className="comparison-header">
            <span>Feature</span><span>REST</span><span>GraphQL</span><span>Winner</span>
          </div>
          {/* TODO 5d: Map over data?.getRestVsGraphQLComparison and render comparison rows */}
          {data?.getRestVsGraphQLComparison.map((row, i) => (
            <motion.div key={row.feature} className="comparison-row" initial={{ opacity:0, x:-20 }} animate={{ opacity:1, x:0 }} transition={{ delay: i * 0.07 }}>
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
