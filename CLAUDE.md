# Hold

Companion to `AGENTS.md`. Keep both files aligned.

Goal: keep this repository a product a stranger can read: a background clerk that files overnight work and stops on a Decision Card when money would move.

Success means:
- The only interactive UI is the Decision Card on public `/` (no login, no prompt box).
- Copy, comments, docs, and commits are English. Amounts are USD.
- README Demo truth is current: Built / Not yet / Mocked / Synthetic / Hardcoded. Canned Path is labeled. A live AgentCore URL appears only after it exists.

Stop when: the change is internal planning or process notes. Keep those out of this repository.

## Product language

Use Hold, Decision Card, Overnight Queue, Interrupt, Approve, Deny, Trust, Canned Path, payment tool.

## Layout

- `web/`: public adapter and Decision Card
- `agent/`: overnight graph, interrupt hook, tools
- `fixtures/`: canned overnight queue
- `deploy/`: AgentCore container and seed job

See README.md and ARCHITECTURE.md.

## Copy

Write complete sentences with mixed length. Prefer names, amounts, and mechanisms over slogans. Avoid stacked fragments, marketing contrasts ("it's not X, it's Y"), fake-profound closers, decorative bold, and em dashes. Keep honesty labels (Mocked, Canned Path). Keep the tagline: "The agent works overnight. You only approve what spends money."
