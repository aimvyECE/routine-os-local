# Verification record · 2026-11-13

## Passed

- JavaScript syntax: `node --check app.js`, `node --check core.js`.
- 22 Node logic tests: schema limits, dates, ID uniqueness, links, note preservation, moves without changing deadlines, reorder, archive semantics, suggestions, microsteps, non-destructive import conflicts and JSON roundtrip.
- 32 JSDOM interaction assertions: section and task capture, editing/reorder, microsteps without completing parent, note drafts across rerender, explicit note save, independent mood, timer start/pause/resume/stop, cancel/archive/restore, future-day move without due change, undo, literal untrusted text, AI context excludes journal, theme/text size, stale-storage blocking and explicit reload.
- 10 additional DOM import/export assertions: unsaved note drafts included in export without storage mutation, invalid import rejection, import preview before mutation, merge and conflict preservation.
- Independent code review led to corrections: essential mode no longer hides important metadata or first steps; export includes uncommitted note drafts; reload clears older drafts explicitly; microstep order controls added; immediate timer pause/resume fixed.

## Not verified

- Browser visual layout, real keyboard/screen-reader behaviour, real browser export/import file picker, iOS local HTML opening, real concurrent-tab event behaviour and performance on large datasets.
- The prepared Playwright scenario (`tests/ui.cjs`) could not run: Chromium process could not create its required socket in the available command environment. Browser automation also refused local `file:` navigation. No restriction was bypassed.
- JSDOM is a DOM simulation, not a browser rendering engine. Dialog methods were polyfilled for tests. These tests do not prove visual quality or full accessibility.
- No clinical, wellbeing or productivity outcome evaluation.

## Known limitations

- Local storage is unencrypted and finite. Local does not mean backed up. Export regularly.
- A pre-write snapshot comparison plus storage event catches many conflicts, but is not an atomic cross-tab transaction. Use one editing tab; concurrent writes remain a limitation until an indexed transactional store/lock design is implemented.
- No automatic daily recurrence, model/persistent-section semantics, project entity, external calendar, AI API or notifications.
- Note drafts persist through rerenders in memory and are included in an export, but only explicit save writes them to local storage. The browser unload warning is a best-effort safeguard, not a backup.
- No permanent deletion/purge. Archived sections can be restored.
- Any future public demo must start empty or with explicitly fictitious data. Never package browser storage or personal exports.
