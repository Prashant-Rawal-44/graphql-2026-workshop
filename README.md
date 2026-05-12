# Step 4 — Real-time Subscriptions

## Goal
Make the app real-time with WebSocket subscriptions.
**Open two browser tabs — level up a skill in one, watch it update in the other instantly.**
This is impossible with plain REST without polling hacks.

## Your Tasks

### Server (server/resolvers.js)

#### 4a. Import PubSub
```js
import { PubSub } from 'graphql-subscriptions';
```

#### 4b. Create pubsub instance
```js
const pubsub = new PubSub();
const SKILL_LEVELED_UP = 'SKILL_LEVELED_UP';
```

#### 4c. Publish in levelUpSkill mutation
```js
// After updating the skill:
pubsub.publish(SKILL_LEVELED_UP, { skillLeveledUp: skill });
```

#### 4d. Add Subscription resolver
```js
Subscription: {
  skillLeveledUp: {
    subscribe: () => pubsub.asyncIterator([SKILL_LEVELED_UP]),
  },
},
```

### Client

#### 4e–4f. Import useSubscription + subscription document
```js
import { useSubscription } from '@apollo/client';
import { SKILL_LEVELED_UP } from './graphql/subscriptions';
```

#### 4g. Add the subscription hook in App.jsx
```jsx
useSubscription(SKILL_LEVELED_UP, {
  onData: ({ data }) => {
    const skill = data?.data?.skillLeveledUp;
    if (!skill) return;
    setWsConnected(true);
    addToast(`⬆ ${skill.title} leveled up to ${skill.level}!`);
    // 4h: Update cache
    apolloClient.cache.modify({
      id: apolloClient.cache.identify({ __typename: 'Skill', id: skill.id }),
      fields: { level: () => skill.level, xp: () => skill.xp, isMastered: () => skill.isMastered },
    });
  },
});
```

#### Note: client/src/apollo/client.js already has the split link configured.
The `split()` function routes subscription operations to WebSocket and everything else to HTTP.

## Demo moment
1. Start server + client
2. Open http://localhost:5173 in **two tabs**
3. Level up a skill in Tab 1
4. Watch Tab 2 update in real-time — no refresh, no polling!

## REST comparison
With REST you'd need:
- Server-Sent Events (SSE) + custom event handling
- WebSocket from scratch + message protocol
- Manual reconnection logic
GraphQL Subscriptions give you all of this with a 5-line resolver.

## Next Step
```bash
git checkout 04-subscriptions-solution   # See the answer
git checkout 05-rest-vs-graphql          # Next: deepen the comparison
```
