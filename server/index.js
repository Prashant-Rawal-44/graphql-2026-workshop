import express from 'express';
import http from 'http';
import cors from 'cors';
import { ApolloServer } from '@apollo/server';
import { expressMiddleware } from '@apollo/server/express4';
import { ApolloServerPluginDrainHttpServer } from '@apollo/server/plugin/drainHttpServer';
import { makeExecutableSchema } from '@graphql-tools/schema';
import { WebSocketServer } from 'ws';
import { useServer } from 'graphql-ws/lib/use/ws';
import { typeDefs } from './schema.js';
import { resolvers } from './resolvers.js';

async function bootstrap() {
  const app = express();
  const httpServer = http.createServer(app);

  // Single schema shared by HTTP (queries/mutations) + WebSocket (subscriptions)
  const schema = makeExecutableSchema({ typeDefs, resolvers });

  // WebSocket server for real-time subscriptions
  const wsServer = new WebSocketServer({ server: httpServer, path: '/graphql' });
  const wsCleanup = useServer({ schema }, wsServer);

  const server = new ApolloServer({
    schema,
    plugins: [
      ApolloServerPluginDrainHttpServer({ httpServer }),
      { async serverWillStart() { return { async drainServer() { await wsCleanup.dispose(); } }; } },
    ],
  });

  await server.start();
  app.use('/graphql', cors({ origin: '*' }), express.json(), expressMiddleware(server));

  // REST comparison routes — these show WHY GraphQL is better
  // REST needs 5 separate endpoints; GraphQL handles all with one /graphql
  app.get('/rest/skills', (_, res) => res.json({ note: 'REST: needs separate endpoints for everything', endpoints: ['/rest/skills', '/rest/skills/:id', '/rest/categories', '/rest/stats'] }));
  app.get('/rest/skills/:id', (req, res) => res.json({ note: 'REST: GET /skills/:id — separate round trip', id: req.params.id }));
  app.get('/rest/categories', (_, res) => res.json({ note: 'REST: GET /categories — yet another round trip' }));
  app.get('/rest/stats', (_, res) => res.json({ note: 'REST: GET /stats — 3rd round trip just for aggregates' }));
  app.patch('/rest/skills/:id/level', (req, res) => res.json({ note: 'REST: PATCH — no real-time push to other clients' }));

  const PORT = 4000;
  httpServer.listen(PORT, () => {
    console.log('');
    console.log('  GraphQL in 2026 — Skill-Tree Dashboard');
    console.log('  =======================================');
    console.log(`  GraphQL : http://localhost:${PORT}/graphql`);
    console.log(`  WS Subs : ws://localhost:${PORT}/graphql`);
    console.log(`  REST cmp: http://localhost:${PORT}/rest/skills`);
    console.log('');
  });
}

bootstrap();
