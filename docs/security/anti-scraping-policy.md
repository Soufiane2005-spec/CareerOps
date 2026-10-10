# CareerOps — Anti-Scraping Safety Policy

## 1. Purpose

This document defines the rules CareerOps follows to avoid unsafe,
unauthorized, or fragile web-scraping practices.

CareerOps prioritizes official APIs, permitted feeds, and documented
integration methods.

---

## 2. General Rule

CareerOps must not bypass technical or contractual restrictions in order
to collect job opportunity data.

If automated access is not clearly permitted, the source must not be used.

---

## 3. Prohibited Techniques

CareerOps must not use:

- automated account login for scraping
- Selenium bots against restricted platforms
- Playwright bots used to evade platform controls
- CAPTCHA bypassing
- anti-bot bypassing
- proxy rotation intended to evade restrictions
- user-agent rotation intended to evade blocking
- rate-limit bypassing
- session hijacking
- cookie theft
- private endpoint abuse
- reverse-engineered private APIs without permission

---

## 4. LinkedIn

CareerOps must not scrape LinkedIn.

CareerOps must not:

- automate LinkedIn login
- reuse user session cookies
- scrape profiles or jobs using browser bots
- attempt to bypass LinkedIn anti-automation controls

LinkedIn may only be integrated through an official or explicitly
permitted integration method.

---

## 5. Preferred Integration Order

CareerOps should prefer sources in this order:

1. official API
2. official public feed
3. documented partner integration
4. public dataset with suitable usage rights
5. permitted public source with explicit automation allowance

If none of these are available, the provider should be skipped.

---

## 6. Rate-Limit Safety

CareerOps must respect documented provider limits.

Provider connectors should support:

- request throttling
- timeouts
- exponential backoff where appropriate
- handling of HTTP 429 responses
- retry limits
- failure isolation

CareerOps must never intentionally increase request frequency to evade
provider limits.

---

## 7. User Credentials

CareerOps must never ask users to provide credentials for third-party
platforms solely to enable scraping.

Examples include:

- LinkedIn password
- session cookies
- authentication tokens copied from browser sessions

---

## 8. Engineering Principle

A provider integration should be:

- authorized
- documented
- stable
- maintainable
- observable
- easy to disable

If an integration requires bypassing protections to keep working,
it is not suitable for CareerOps.

---

## 9. Failure Behavior

If a provider changes its API, blocks access, or removes permission:

- disable the provider connector
- log the failure
- keep CareerOps available
- review the provider before re-enabling integration

The system must never respond by automatically attempting to bypass the
provider's restrictions.

---

## 10. Project Rule

CareerOps values reliability and legal/operational safety over the number
of job sources integrated.

A smaller number of permitted providers is preferred over a larger set of
fragile or unauthorized scrapers.