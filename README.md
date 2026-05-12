# Step 5 — REST vs GraphQL: The Full Picture

## Goal
Wire up the comparison panel to fetch live data from GraphQL.
Use this as a discussion point with the audience.

## Your Tasks

### 5a–5d. Connect RestVsGraphQL.jsx to real data
```jsx
const { data, loading } = useQuery(GET_REST_VS_GRAPHQL);
```
Remove the hardcoded demo data and use the live query result.

## Discussion Points for the Audience

### When GraphQL wins
| Scenario | Why GraphQL |
|---|---|
| Mobile apps with limited bandwidth | Request only needed fields |
| Complex dashboards | One request for all widget data |
| Public APIs with diverse clients | Each client shapes its own response |
| Rapidly evolving schemas | Add fields without versioning |

### When REST wins
| Scenario | Why REST |
|---|---|
| Simple CRUD services | REST is simpler to set up |
| File upload heavy apps | Multipart is painful in GraphQL |
| CDN-heavy public APIs | HTTP caching is effortless with REST |
| Teams unfamiliar with GraphQL | Learning curve is real |

### Latest Trends in GraphQL (2026)
1. **Federation & Supergraph** — Apollo Federation 2, Cosmo Router
   Multiple teams own separate subgraphs, unified into one API gateway
2. **GraphQL over HTTP 1.1** — The new spec standardizes transport
3. **@defer / @stream** — Stream large datasets incrementally
4. **Persisted Queries / APQ** — CDN-cacheable POST requests
5. **Code-first schemas** — Pothos, TypeGraphQL for type-safe schema building
6. **Edge GraphQL** — Running resolvers at the edge (Cloudflare Workers)

## Next Step
```bash
git checkout 05-rest-vs-graphql-solution
git checkout 06-scaling
```
