# CareerOps — Data Classification

## 1. Purpose

This document defines how CareerOps classifies data according to
its sensitivity.

The objective is to apply appropriate protection to each type of data.

---

## 2. Classification Levels

CareerOps uses four levels:

- Public
- Internal
- Sensitive
- Secret

---

## 3. Public Data

Public data can be exposed without creating meaningful security risk.

Examples:

- public job opportunity title
- company name
- public job description
- public application URL
- public documentation
- non-sensitive API health information

Protection requirements:

- integrity should still be maintained
- data should not be modified by unauthorized users

---

## 4. Internal Data

Internal data is not highly sensitive but should not necessarily be
public.

Examples:

- import execution metadata
- internal provider status
- non-sensitive operational logs
- internal configuration values
- application metrics without personal data

Protection requirements:

- authenticated or service-only access where appropriate
- avoid unnecessary public exposure

---

## 5. Sensitive Data

Sensitive data belongs to users or can affect user privacy.

Examples:

- user email address
- profile information
- skill profile
- application history
- application notes
- CV metadata
- uploaded CV files
- interview dates
- reminder information

Protection requirements:

- authentication required
- ownership authorization required
- encrypted in transit
- encrypted at rest where supported
- must not appear unnecessarily in logs

---

## 6. Secret Data

Secret data provides access to systems or protected resources.

Examples:

- database passwords
- provider API keys
- JWT signing secrets
- AWS credentials
- third-party service credentials
- encryption keys

Protection requirements:

- never committed to Git
- never hardcoded
- stored in environment variables locally
- stored using a secrets management service in cloud environments
- access restricted through least privilege
- rotated if exposed
- never logged

---

## 7. Password Handling

User passwords are never stored directly.

CareerOps stores only secure password hashes.

Password hashes are still considered sensitive data and must not be
returned through API responses or exposed in logs.

---

## 8. CV Data

Uploaded CVs may contain:

- full name
- email
- phone number
- education history
- employment history
- location
- professional experience

CV files must therefore be treated as sensitive user data.

Requirements:

- private object storage
- ownership validation
- controlled download access
- no public bucket access
- no permanent public file URLs

---

## 9. Logging Rules

Logs must never contain:

- plaintext passwords
- API keys
- AWS credentials
- database passwords
- authentication tokens

Sensitive personal information should also be minimized in logs.

Prefer identifiers such as:

user_id

instead of full personal details where possible.

---

## 10. Environment Separation

Secrets must be isolated between environments.

Example:

dev database credentials

must be separate from:

prod-demo database credentials

Development must not depend on production-demo secrets.

---

## 11. Git Rules

The following must never be committed:

.env

real API keys

cloud credentials

private keys

database passwords

production configuration containing secrets

An example environment file may be committed only with placeholder
values.

Example:

DATABASE_URL=postgresql://user:password@localhost/careerops

PROVIDER_API_KEY=replace_me

---

## 12. Classification Summary

Public:
- opportunity information
- public company information
- public documentation

Internal:
- operational metadata
- non-sensitive logs
- import statistics

Sensitive:
- user profile
- user email
- CV files
- application history
- reminders
- application notes

Secret:
- passwords and signing secrets
- API credentials
- database credentials
- cloud credentials
- private keys