# My Kitchen Garden: Agent Handover and Continuation File

Read this first, whichever agent you are (Muse or Cline). This
file exists so the build never depends on one agent's memory or
token balance. Everything decided is written down. Do not ask
Evans questions this file or the spec already answers.

## The one-paragraph version

Evans (Claro & Co) is building an online store for a plant
nursery, My Kitchen Garden, in Nigeria. Storefront plus owner
dashboard on Next.js, Neon Postgres and Cloudinary (free tiers).
Customers browse plants with care guides, then pay online via
Paystack or order on WhatsApp. Every order is delivery (fee by
zone, added before payment) or free pickup at Moniya. Prices
are fixed; there is no negotiation feature. The governing test:
the platform must reduce the owner's stress and manual work,
or it has failed.

## Status (update this section after every work session)

- Deal: N400k total agreed with Damian Bolt (the owner's
  fiance) on Oct 26, 2026. N200k deposit, N200k balance when
  the build checklist is fully ticked and the store is ready
  to launch. Deposit expected mid to late Nov 2026.
- BUILD GATE: no build starts until the deposit lands. Prep
  and planning are fine now; code is not.
- Current phase: PREP ONLY. Spec written, checklist written,
  no code yet.
- Next action when the deposit lands: Stage 1 (foundation on
  placeholders plus test data), then stages 2 to 5, each one
  shown to Evans and approved before the next begins.
- Last updated: Nov 1, 2026, by Muse, at file creation.

## Where everything lives

- Full build spec: this goal's files folder,
  my-kitchen-garden-build-spec/ (its .src/OUTLINE.md is the
  section-by-section summary of record).
- Client-facing build checklist (the tick-box document the
  balance is tied to): my-kitchen-garden-build-checklist/.
- Agreement draft: my-kitchen-garden-agreement/ and
  ~/workspace/drafts/nigeria-nursery-400k-agreement.md.
- Engineering standard: the fullstack-engineering skill plus
  its EVANS_ADDENDUM.md. Visual direction: the
  captivating_web_design skill. Both are binding.

## Decisions of record (do not relitigate)

- Stack: Next.js, Neon Postgres (decided; Supabase and MongoDB
  Atlas rejected, reasons in the spec), Cloudinary free tier
  for images. Database runs free-tier as Evans's favour,
  estimated to cover roughly 20,000 orders; past that scale a
  monthly database charge sized by volume applies, already
  declared to the client up front.
- Platform first, content later. The store ships with an empty
  catalogue by design. Testing uses our own test products,
  removed before handover. The owner adds her first real
  products together with Evans at handover; that session is
  her training. Her photos and plant list are never build
  blockers.
- Owner details (full business name, pickup address and
  instructions) start as clearly marked placeholders in
  editable settings fields, replaced at handover.
- Payment: Paystack, verified by webhook before an order
  counts as paid or WhatsApp appears on the pay-online path.
- SMS: provider-agnostic sendSMS adapter, wallet in the
  owner's own name, sender ID KitchenGrdn, registered as early
  as possible (approval can take about 3 weeks, runs in
  parallel, never blocks launch). Spec of record names Emisri
  (about N5.40 to 6 per SMS). Open thread: Evans explored
  Sendchamp on Oct 30, 2026 (page prices SMS N6.30, WhatsApp
  N2.70) and asked whether the WhatsApp figure includes Meta's
  template fee; no reply yet. Quote nothing to the client
  until figures are confirmed.
- Owner dashboard: she self-manages plants, care guides, Q&A,
  orders, zones, pickup settings, FAQ and tracked links. Staff
  accounts with per-person permission switches; owner-only
  powers are never delegable; deactivation is instant;
  important actions are logged by user. New-order alert SMS
  goes to recipients she chooses; SMS is the bell, the
  dashboard is where the work happens.
- Design: the shop must feel like walking through a garden,
  while buying stays as simple as the Nature's Nook reference.
  Signature motion is THE GROWING SEASON: a pinned photoreal
  seed-to-harvest scroll sequence, mobile-first, with a
  reduced-motion fallback. Landing imagery is generated or
  sourced by the agent, photoreal; no client photos needed
  for the presentation layer.
- Money terms around the build: no monthly care plan on this
  deal. Post-launch changes at N10k per hour, 1-hour minimum,
  always quoted first. Domain N35k per year in her name.
  Running costs (SMS wallet, domain) are hers.

## Build sequence (from the spec)

Five stages, 7 to 10 working days from the deposit, each gated
by Evans's approval: 1) foundation on placeholders and test
data, 2) storefront including THE GROWING SEASON (screenshot
audited per the design skill before Evans sees it), 3) owner
dashboard and permissions, 4) payments, WhatsApp ordering and
SMS end to end, 5) full end-to-end testing on test products,
then the handover content session with the owner.

## Rules for whichever agent is holding the build

1. Read this file, the spec outline, the fullstack skill and
   its addendum, and the design skill before touching anything.
2. Evans is the only approver. Show each stage, wait for his
   word, then proceed. Never push or publish without it.
3. When you finish a work session, update the Status section
   above: what changed, what is verified, what is next. The
   next agent resumes from that text, not from chat history.
4. If a decision is genuinely missing, ask Evans once, in
   plain words. If it is written here or in the spec, do not
   ask at all.
5. No invented facts about the client or her business, no em
   dashes in any copy, no client photos required or waited on.

## Kickoff prompt for Cline (Evans pastes this)

Use the fullstack-engineering skill and read its
EVANS_ADDENDUM.md. Then read the file
my-kitchen-garden-HANDOVER.md in this project's goal folder and
the build spec outline it points to. You are continuing the My
Kitchen Garden build exactly where the handover file says it
stands. Follow the build sequence and the rules in that file,
and update its Status section when you finish.
