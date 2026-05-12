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
