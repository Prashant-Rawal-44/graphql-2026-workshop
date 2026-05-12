# Step 4 — SOLUTION: Real-time Subscriptions Working

## What we proved
- PubSub broadcasts events over WebSocket to all connected clients
- Two tabs open, level up in one → updates instantly in the other
- Apollo cache.modify() propagates changes to every component using that skill
- The green "Live" indicator shows active WebSocket connection

## Architecture
```
Browser Tab 1          Server                  Browser Tab 2
    │                    │                          │
    ├── levelUpSkill ──► │                          │
    │                    ├── pubsub.publish() ──────►│
    │                    │                          │
    │                    │   ◄── skillLeveledUp ────┤
    │                    │        (WS push)         │
    │                    │                   cache.modify()
    │                    │                   → UI re-renders
```

## Next Step
```bash
git checkout 05-rest-vs-graphql
```
