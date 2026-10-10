# CareerOps — Approved Job Source Policy

## 1. Purpose

This document defines which external job sources CareerOps is allowed
to integrate with.

The objective is to ensure that opportunity imports use permitted,
stable, and maintainable sources.

---

## 2. Approved Source Types

CareerOps may use:

- official job APIs
- public feeds explicitly intended for reuse
- partner APIs
- public datasets with suitable usage rights
- provider integrations where automated access is explicitly permitted

---

## 3. Conditionally Approved Sources

A source may be integrated only after reviewing:

- API documentation
- terms of use
- authentication requirements
- rate limits
- data usage restrictions
- redistribution restrictions
- automation restrictions

If these conditions are unclear, the source should not be used until
its usage is verified.

---

## 4. Prohibited Sources

CareerOps must not rely on:

- unauthorized LinkedIn scraping
- automated login bots
- Selenium-based scraping against restricted platforms
- Playwright-based scraping used to bypass platform restrictions
- CAPTCHA bypassing
- anti-bot bypassing
- session or cookie theft
- private API reverse engineering without permission
- rate-limit bypass techniques

---

## 5. LinkedIn Policy

CareerOps must not scrape LinkedIn.

LinkedIn may only be integrated if CareerOps receives access to an
official API or another explicitly permitted integration method.

CareerOps must not require users to provide LinkedIn credentials for
automated scraping.

---

## 6. Provider Requirements

Each provider integration should document:

- provider name
- integration method
- API or feed URL
- authentication method
- rate limits
- expected response format
- retry strategy
- timeout strategy
- allowed usage
- date usage rules were reviewed

---

## 7. Rate Limits

CareerOps must respect provider rate limits.

Provider connectors should support:

- controlled request frequency
- timeouts
- retry with backoff where appropriate
- handling of 429 responses
- failure isolation

Repeated requests must not be used to intentionally bypass provider
limits.

---

## 8. Provider Credentials

Provider credentials must:

- never be hardcoded
- never be committed to Git
- use environment variables locally
- use secure secret storage in cloud environments

---

## 9. Provider Isolation

The failure of one provider must not stop other providers or the
CareerOps platform.

Example:

Provider A unavailable
→ log failure
→ retry later
→ Provider B continues
→ CareerOps API remains available

---

## 10. Data Validation

All provider data must be treated as untrusted input.

CareerOps must validate and normalize provider data before storing it.

Checks may include:

- required fields
- field lengths
- valid URLs
- supported data types
- publication dates
- unexpected payload structure

---

## 11. Provider Approval Checklist

Before implementing a new provider, confirm:

- automated access is permitted
- API or feed documentation is available
- authentication requirements are understood
- rate limits are understood
- data usage rules are acceptable
- secrets can be managed securely
- failures can be handled safely
- the provider adds meaningful value to CareerOps

---

## 12. Design Principle

CareerOps prioritizes stable and authorized integrations over a large
number of risky data sources.

One reliable permitted provider is better than ten fragile scrapers.