# ⬡ GraphQL in 2026: From REST to Real-Time

> Workshop code repository — Apollo Server 4 · GraphQL Subscriptions · DataLoader · React + Apollo Client

**📖 Course Notes:** https://prashant-rawal-44.github.io/graphQl-2026

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/Prashant-Rawal-44/graphql-2026-workshop.git
cd graphql-2026-workshop

# 2. Start on the starter branch (blank canvas)
git checkout starter

# 3. Install dependencies
cd server && npm install
cd ../client && npm install

# 4. Run the app
# Terminal 1 — start the GraphQL server
cd server && npm run dev

# Terminal 2 — start the React client
cd client && npm run dev
```

Open **http://localhost:5173** in your browser.

---

## 🌿 Branch Structure

Each topic has a **start** branch (you code along) and a **solution** branch (completed code).

| Branch | Solution | What you build |
|--------|----------|---------------|
| `starter` | — | Empty project — your starting point |
| `01-schema` | `01-schema-solution` | SDL schema, types, Apollo Server setup |
| `02-queries` | `02-queries-solution` | Resolvers, `useQuery`, Apollo Client |
| `03-mutations` | `03-mutations-solution` | Mutations, `useMutation`, optimistic UI |
| `04-subscriptions` | `04-subscriptions-solution` | PubSub, WebSockets, `useSubscription` |
| `05-rest-vs-graphql` | `05-rest-vs-graphql-solution` | REST comparison panel, side-by-side demo |
| `06-scaling` | `06-scaling-solution` | DataLoader, fragments, query complexity |

### How to use the branches

```bash
# Jump to any section's starting point
git checkout 01-schema

# Stuck? Check the solution
git checkout 01-schema-solution

# Start fresh on next section
git checkout 02-queries
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| API Server | Apollo Server 4 + `graphql` |
| Real-time | `graphql-ws` + WebSocket subscriptions |
| Schema stitching | `@graphql-tools/schema` |
| Client | React 18 + Vite 5 |
| GraphQL Client | Apollo Client 3 |
| Animations | Framer Motion 11 |
| Batching | DataLoader |

---

## 📁 Project Structure

```
graphql-2026-workshop/
├── server/
│   ├── src/
│   │   ├── schema.js        # GraphQL SDL type definitions
│   │   ├── resolvers.js     # Query / Mutation / Subscription resolvers
│   │   ├── pubsub.js        # PubSub instance for subscriptions
│   │   ├── loaders.js       # DataLoader setup
│   │   └── index.js         # Apollo Server entry point
│   └── package.json
│
└── client/
    ├── src/
    │   ├── App.jsx           # Root component
    │   ├── apollo.js         # Apollo Client + WebSocket split link
    │   ├── components/       # React components per section
    │   └── queries/          # GraphQL query/mutation/subscription definitions
    └── package.json
```

---

## ⚡ Prerequisites

- **Node.js** v18 or higher (`node --version`)
- **npm** v9 or higher (`npm --version`)
- A terminal and a code editor (VS Code recommended)

No database required — data is in-memory for the workshop.

---

## 🔧 Troubleshooting

**Port already in use?**
```bash
# Server runs on :4000, client on :5173
# Kill whatever is using the port:
lsof -ti:4000 | xargs kill
lsof -ti:5173 | xargs kill
```

**Subscriptions not connecting?**
Make sure the server is running *before* you open the client. The WebSocket handshake happens at page load.

**`node_modules` issues?**
```bash
rm -rf server/node_modules client/node_modules
cd server && npm install && cd ../client && npm install
```

---

## 📖 Course Notes

Step-by-step lesson notes for every branch are published at:

**https://prashant-rawal-44.github.io/graphQl-2026**

Each lesson includes the full explanation, code snippets, and the matching `git checkout` command.

---

## 📜 License

MIT — use freely for learning and teaching.
