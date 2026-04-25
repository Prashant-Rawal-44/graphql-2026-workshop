// ─── Apollo Server 4 — Entry Point ───────────────────────────────────────────
// Dual-transport setup:
//   • HTTP  → express + expressMiddleware  (Queries & Mutations)
//   • WS    → ws + graphql-ws              (Subscriptions)

import { ApolloServer }                          from '@apollo/server';
import { expressMiddleware }                      from '@apollo/server/express4';
import { ApolloServerPluginDrainHttpServer }      from '@apollo/server/plugin/drainHttpServer';
import { makeExecutableSchema }                   from '@graphql-tools/schema';
import { WebSocketServer }                        from 'ws';
import { useServer }                              from 'graphql-ws/lib/use/ws';
import express                                    from 'express';
import http                                       from 'http';
import cors                                       from 'cors';
import { json }                                   from 'express';

import { typeDefs }   from './schema.js';
import { resolvers }  from './resolvers.js';

// ── Bootstrap ────────────────────────────────────────────────────────────────
async function bootstrap() {
  const app        = express();
  const httpServer = http.createServer(app);

  // Build a single executable schema shared by HTTP and WS transports
  const schema = makeExecutableSchema({ typeDefs, resolvers });

  // ── WebSocket server (subscriptions) ──────────────────────────────────────
  const wsServer = new WebSocketServer({
    server: httpServer,
    path:   '/graphql',
  });

  // useServer returns a cleanup handle Apollo needs for graceful shutdown
  const wsServerCleanup = useServer({ schema }, wsServer);

  // ── Apollo HTTP server ────────────────────────────────────────────────────
  const apolloServer = new ApolloServer({
    schema,
    plugins: [
      // Graceful HTTP drain
      ApolloServerPluginDrainHttpServer({ httpServer }),
      // Graceful WS drain
      {
        async serverWillStart() {
          return {
            async drainServer() {
              await wsServerCleanup.dispose();
            },
          };
        },
      },
    ],
  });

  await apolloServer.start();

  // ── Routes ────────────────────────────────────────────────────────────────
  app.use(
    '/graphql',
    cors({
      origin:      ['http://localhost:5173', 'http://localhost:4173'],
      credentials: true,
    }),
    json(),
    expressMiddleware(apolloServer),
  );

  // ── Listen ────────────────────────────────────────────────────────────────
  const PORT = 4000;

  httpServer.listen(PORT, () => {
    console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
    console.log('  ⚡  Skill Tree — GraphQL in 2026');
    console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
    console.log(`  🚀  HTTP  →  http://localhost:${PORT}/graphql`);
    console.log(`  🔌  WS    →  ws://localhost:${PORT}/graphql`);
    console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
  });
}

bootstrap().catch((err) => {
  console.error('Server bootstrap failed:', err);
  process.exit(1);
});
