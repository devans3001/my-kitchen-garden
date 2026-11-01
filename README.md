# My Kitchen Garden

Online store and owner dashboard for a plant nursery in
Nigeria, built by Claro & Co. Customers browse plants with
care guides, then pay online with Paystack or order on
WhatsApp. Delivery is by zone, or free pickup at Moniya.

## Status

PREP ONLY. The build starts when the client's deposit lands
(expected mid to late November 2026). This repository currently
holds the project brief, the decisions of record, and the
engineering skill that governs the build. No application code
yet, on purpose.

## Start here, whichever agent you are

1. `HANDOVER.md`: the continuation file. Decisions, build
   sequence, rules, and the live status section. Read it
   first, and update its status when you finish a session.
2. `docs/BUILD_SPEC_OUTLINE.md`: the section-by-section
   summary of the full build spec.
3. `.cline/skills/fullstack-engineering/SKILL.md`: the
   engineering standard for this project, with
   `EVANS_ADDENDUM.md` carrying the house rules that win
   wherever the two differ.

## Stack (decided, see HANDOVER.md)

Next.js, Neon Postgres, Cloudinary for images, Paystack for
payments, provider-agnostic SMS from the owner's own wallet.
