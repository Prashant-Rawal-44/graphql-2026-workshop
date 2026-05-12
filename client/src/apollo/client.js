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
