// ─── Apollo Client — Dual-transport Link ─────────────────────────────────────
// • HTTP link  → Queries + Mutations  (standard request/response)
// • WS link   → Subscriptions         (persistent WebSocket via graphql-ws)
// The `split` function routes each operation to the correct transport.

import { ApolloClient, InMemoryCache, HttpLink, split } from '@apollo/client';
import { GraphQLWsLink }                                  from '@apollo/client/link/subscriptions';
import { createClient }                                   from 'graphql-ws';
import { getMainDefinition }                              from '@apollo/client/utilities';

const HTTP_ENDPOINT = 'http://localhost:4000/graphql';
const WS_ENDPOINT   = 'ws://localhost:4000/graphql';

// ── HTTP transport (queries & mutations) ──────────────────────────────────────
const httpLink = new HttpLink({ uri: HTTP_ENDPOINT });

// ── WebSocket transport (subscriptions) ──────────────────────────────────────
const wsLink = new GraphQLWsLink(
  createClient({
    url:           WS_ENDPOINT,
    retryAttempts: 5,                      // auto-reconnect on disconnect
    shouldRetry:   () => true,
  }),
);

// ── Route to correct transport ────────────────────────────────────────────────
const splitLink = split(
  ({ query }) => {
    const def = getMainDefinition(query);
    return def.kind === 'OperationDefinition' && def.operation === 'subscription';
  },
  wsLink,   // ← subscriptions
  httpLink, // ← everything else
);

// ── Client ────────────────────────────────────────────────────────────────────
export const client = new ApolloClient({
  link:             splitLink,
  cache:            new InMemoryCache(),
  connectToDevTools: true,
});
