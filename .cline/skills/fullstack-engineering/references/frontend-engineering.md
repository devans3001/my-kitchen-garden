# Frontend Engineering

## Defaults

For new web products, prefer TypeScript, React, Next.js App Router and Tailwind CSS when they fit. Use the current stable versions supported by the repository and consult official documentation for version-sensitive APIs. Do not migrate an existing app merely to match these defaults.

## Structure and state

- Organize substantial UI by feature/domain; keep shared components truly shared.
- Keep server state, URL state, form state, and ephemeral UI state conceptually separate.
- Prefer server rendering and server components where the framework benefits; add client components only for interactivity/browser APIs.
- Use native `fetch` for straightforward data access. Add TanStack Query when cache lifecycle, optimistic updates, polling, retries, or complex client synchronization justify it.
- Use React Hook Form and schema validation for complex forms; simple forms need not acquire extra dependencies.
- Avoid duplicate sources of truth and broad global state by default.

## UX states

Every data-driven view should consider loading/skeleton, empty, success, error, stale/offline, and permission-denied states as applicable. Every action should provide feedback and prevent accidental duplicate submission.

## Accessibility

Use semantic HTML, labels, keyboard-operable controls, visible focus, logical focus order, sufficient contrast, reduced-motion preferences, and accessible validation/error announcements. Do not use color alone to communicate status.

## Responsive design

Design mobile-first but verify real tablet and desktop layouts. Test narrow widths, long text, zoom, touch targets, overflow, and orientation. Avoid simply shrinking desktop layouts.

## Quality

- Keep components cohesive and avoid giant page components.
- Use stable keys and correct effect dependencies.
- Avoid unsafe HTML injection.
- Avoid unnecessary client-side JavaScript and expensive re-renders.
- Use optimized image/font loading appropriate to the framework.
- Test important flows at browser level.
- Never ship dead controls, placeholder links, fake metrics, or static mock data disguised as live data.
