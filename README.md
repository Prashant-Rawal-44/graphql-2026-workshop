# Step 3 — Implement GraphQL Mutations

## Goal
Add write operations. See how returning the updated object makes Apollo cache updates automatic.

## Your Tasks

### Server (server/resolvers.js)

#### 3a. levelUpSkill mutation
```js
levelUpSkill: (_, { id }) => {
  const skill = skills.find(s => s.id === id);
  if (!skill) throw new Error('Skill not found');
  if (skill.level >= skill.maxLevel) throw new Error('Already at max level');
  skill.level += 1;
  skill.xp += 100;
  if (skill.level === skill.maxLevel) skill.isMastered = true;
  return skill; // Return updated skill — Apollo cache auto-updates!
},
```

#### 3b. addTagToSkill
```js
addTagToSkill: (_, { id, tag }) => {
  const skill = skills.find(s => s.id === id);
  if (!skill) throw new Error('Skill not found');
  if (!skill.tags.includes(tag)) skill.tags.push(tag);
  return skill;
},
```

#### 3c. resetSkill
```js
resetSkill: (_, { id }) => {
  const skill = skills.find(s => s.id === id);
  if (!skill) throw new Error('Skill not found');
  skill.level = 1; skill.xp = 100; skill.isMastered = false;
  return skill;
},
```

### Client (client/src/components/SkillCard.jsx)

#### 3d. Wire up useMutation
```jsx
const [levelUp, { loading }] = useMutation(LEVEL_UP_SKILL, {
  variables: { id: skill.id },
  onCompleted: () => { setFlashing(true); setTimeout(() => setFlashing(false), 600); },
});
```
**Key insight:** The mutation returns the updated Skill object. Apollo Client uses the `id`
field to find it in the normalized cache and updates it — **every component showing that skill
instantly re-renders with the new level**. No manual state updates needed!

## Verify in GraphiQL
```graphql
mutation {
  levelUpSkill(id: "sk-6") {
    id title level xp isMastered
  }
}
```

## REST vs GraphQL: Write operations
- REST PATCH: returns 204 No Content — you have to refetch or manually update state
- GraphQL Mutation: returns the updated object — cache updates automatically

## Next Step
```bash
git checkout 03-mutations-solution   # See the answer
git checkout 04-subscriptions        # Next task — Real-time!
```
