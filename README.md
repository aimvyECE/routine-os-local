# Routine OS · local MVP 0.2

An experimental, independent organisation toolbox. Choose, start and resume without a prescribed routine. French interface; no account, analytics, remote AI or application network requests. AI-assisted development, not clinically validated software.

## Run

Open `RoutineOS.html` in a modern browser, or serve this directory **only on your own machine**:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
# Open http://127.0.0.1:8765
```

Keep using the same file/location or localhost port: browser storage belongs to an origin. Export before moving files, clearing browser data or changing devices. iOS preview apps may not execute local HTML; desktop browser is the first supported delivery, not a verified mobile installation.

## Implemented

- Date-specific sections: multiple todo lists, notes and optional mood records.
- Add, rename, collapse, reorder and recoverably archive sections. No permanent purge.
- Capture with one required title; editable tasks, first step, ordered microsteps, optional due date, importance, duration and energy.
- Reorder tasks with buttons, mark waiting/done, reopen, move to another section or future date without changing the real deadline.
- Reserve includes tasks from archived sections. Single-task view, resumption capsule and optional five-minute timer.
- Manual display modes, light/dark theme, larger text, keyboard controls. Modes do not diagnose or modify priorities.
- Local JSON export; validated merge import preserving existing IDs and reporting conflicts; undo last 30 successful edits in this session.
- Second-tab conflict detection blocks writes rather than silently replacing state.
- Optional **local prompt preparation**, not an AI integration: only chosen task title/first step, no journal/mood, no transmission.

## Not implemented / not claimed

No automatic recurring routines, persistent cross-day sections, project entity, calendar integration, background reminders, browser sync, cloud account, encryption, real AI engine, clinical efficacy or productivity guarantee. “Élan” is currently a named mode; it does not fill the schedule. Notes use an explicit Save button; uncommitted drafts survive in-app renders in memory, but are not a backup.

## Privacy and safety

User data lives in `localStorage` key `routine-os-v2`, **in plain text**. Anyone with access to the same browser profile can read it. Private browsing/clearing data can destroy it. Exports include private notes and mood; keep them private. All content is rendered with `textContent`/text fields. CSP disallows connections and embedded objects. No personal data, tokens or user-specific routines are shipped.

Archived sections retain content. Their tasks are also reachable in the reserve. Restoring brings the section back to its original day. Undo is session-local, not an audit history. Concurrent changes are detected by comparing storage snapshots before saving and a storage event; this is not a transactional multi-user database.

## Verification

```sh
npm test # Node's built-in runner, no dependencies needed
```

See `docs/VERIFICATION.md` for actual completed checks and known environmental limits. `tests/ui.cjs` is a planned Playwright browser scenario, not evidence of a pass by itself.

## Design and evidence

Organisation and planning can form part of structured support programmes. That does not establish that this application treats ADHD or any other condition. The design emphasises user control, accessible alternatives, privacy and easy resumption. Evaluation should ask whether it reduces friction and makes the next step clearer, not merely count completed tasks.

## Licence

MIT for this original code. No third-party runtime dependency is bundled. Optional development-only testing dependencies retain their own licences.
