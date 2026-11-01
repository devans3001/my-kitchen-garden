# Authentication and Authorization

## Separate the concepts

Authentication establishes identity. Authorization decides what that identity may do to a specific resource in a specific context. A logged-in user is not automatically allowed to access every record.

## Prefer established identity systems

Use a reputable maintained provider/library when it reduces risk and fits constraints. Do not roll custom password cryptography, session protocols, or OAuth flows. Keep provider-specific code behind a small boundary where practical.

## Authorization

- Deny by default.
- Check permissions server-side on every protected operation.
- Apply resource-level ownership and membership checks, not only route-level role checks.
- Model roles and permissions around real business capabilities.
- Prevent insecure direct object references.
- Test cross-user, cross-role, and cross-tenant access.
- Re-check authorization for background jobs and exports.

## Sessions and credentials

Use secure, HttpOnly, SameSite cookies where applicable; protect session lifecycle, rotation, revocation, expiration, and CSRF according to the architecture. Store password hashes only using modern vetted password-hashing libraries and parameters. Support secure account recovery and MFA when risk warrants it.

## Admin access

Use least privilege, separate privileged actions, audit sensitive operations, and require re-authentication or approval for high-impact changes where appropriate.
