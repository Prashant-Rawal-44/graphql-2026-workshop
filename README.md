# 🚀 GraphQL in 2026 — Workshop

## Starter Branch

This is where we begin. The server runs Express with the barest GraphQL setup.

### Run the project
```bash
# Terminal 1 — Server
cd server && npm install && npm run dev
# → http://localhost:4000/graphql

# Terminal 2 — Client
cd client && npm install && npm run dev
# → http://localhost:5173
```

### What's here
- Express server on port 4000
- Apollo Server 4 with a single `hello` query
- Static skill data in `server/data/skills.js`
- REST comparison endpoints at `/rest/skills`, `/rest/categories`, `/rest/stats`

### Try these REST calls (open in browser)
```
http://localhost:4000/rest/skills        ← needs 1 round trip
http://localhost:4000/rest/categories    ← needs another round trip
http://localhost:4000/rest/stats         ← needs a 3rd round trip!
```

### Discussion: What's wrong with REST here?
1. **Over-fetching** — `/rest/skills` returns ALL fields even if you only need `title` and `level`
2. **Multiple round trips** — you need 3 separate HTTP calls just for the dashboard
3. **No real-time** — you'd have to poll every few seconds
4. **No type safety** — nothing stops you returning wrong data shapes

### Next Step
```bash
git checkout 01-schema
```
