# CareerOps — Threat Model

## 1. Purpose

This document identifies the main security threats affecting CareerOps
and the controls planned to reduce those risks.

The goal is to design security into the platform before implementation.

---

## 2. Main Assets

CareerOps must protect:

- user accounts
- password hashes
- user profiles
- application history
- CV files
- provider API credentials
- database credentials
- cloud credentials
- infrastructure configuration
- CI/CD pipeline
- imported opportunity data

---

## 3. Trust Boundaries

Important trust boundaries include:

Internet
→ CareerOps API

External Job Provider
→ Importer

User
→ File Upload

GitHub Actions
→ AWS

CareerOps API
→ PostgreSQL

CareerOps API
→ Object Storage

Workers
→ Queue

Every boundary must validate and restrict access appropriately.

---

## 4. Threat — Broken Access Control

Example:

User A requests:

GET /applications/123

but application 123 belongs to User B.

Risk:

Private data exposure.

Controls:

- authenticated requests
- ownership checks
- authorization tests
- deny access by default

---

## 5. Threat — Credential Theft

Targets may include:

- passwords
- provider API keys
- AWS credentials
- database credentials

Controls:

- password hashing
- environment-based secrets locally
- AWS Secrets Manager in cloud
- GitHub OIDC instead of long-lived AWS keys
- secret scanning
- credential rotation after exposure

---

## 6. Threat — SQL Injection

An attacker may send malicious input to database-backed endpoints.

Controls:

- ORM or parameterized queries
- input validation
- no raw SQL using untrusted input
- automated security testing

---

## 7. Threat — Malicious File Upload

CV upload functionality accepts user-controlled files.

Risks:

- unexpected file type
- oversized files
- malicious payloads
- storage abuse

Controls:

- PDF-only policy for MVP
- file size limits
- content-type validation
- generated storage keys
- private object storage
- no direct execution of uploaded files
- additional malware scanning may be added later

---

## 8. Threat — External Provider Data

External opportunity data is untrusted.

Risks:

- malformed data
- malicious URLs
- unexpected payload size
- provider outage
- duplicated or manipulated records

Controls:

- schema validation
- timeouts
- payload limits
- normalization
- deduplication
- safe error handling
- provider isolation

---

## 9. Threat — Authentication Attacks

Examples:

- password guessing
- credential stuffing
- invalid token reuse

Controls:

- secure password hashing
- generic authentication error messages
- token expiration
- rate limiting later
- security monitoring
- HTTPS in deployed environments

---

## 10. Threat — Sensitive Data Exposure

Sensitive information may accidentally appear in:

- logs
- API responses
- Git commits
- error messages

Controls:

- redact secrets from logs
- do not expose password hashes
- structured error responses
- secret scanning
- least-privilege access
- private CV storage

---

## 11. Threat — Dependency Vulnerabilities

CareerOps depends on external packages and container images.

Controls:

- dependency scanning
- container image scanning
- pinned dependencies where practical
- regular updates
- critical vulnerability review

---

## 12. Threat — CI/CD Compromise

An attacker gaining control of the pipeline could deploy malicious code.

Controls:

- protected branches
- pull request review
- GitHub OIDC
- least-privilege deployment roles
- security checks before deployment
- immutable image identifiers
- artifact integrity verification later

---

## 13. Threat — Infrastructure Misconfiguration

Examples:

- public database
- public storage bucket
- overly permissive IAM
- unrestricted security groups

Controls:

- Terraform
- infrastructure scanning
- private-by-default resources
- least privilege
- code review
- security tests

---

## 14. Threat — Denial of Service

Attackers or faulty integrations may create excessive traffic.

Controls:

- request limits
- timeouts
- queue buffering
- worker isolation
- autoscaling when appropriate
- WAF/rate limiting in production-demo

---

## 15. Threat — Queue Abuse or Poison Messages

A malformed task may repeatedly fail.

Controls:

- message validation
- retry limits
- dead-letter queues
- failure monitoring
- idempotent worker design where practical

---

## 16. Threat — Duplicate Processing

Retries may process the same task multiple times.

Risks:

- duplicate reminders
- duplicate imported jobs
- inconsistent state

Controls:

- deduplication
- idempotency
- unique database constraints
- safe retry design

---

## 17. Threat — Excessive Permissions

Application services or CI/CD roles may have more AWS permissions
than necessary.

Controls:

- least privilege
- separate roles by workload
- separate dev and prod-demo permissions
- regular IAM review

---

## 18. Threat Priority

Initial high-priority risks:

1. broken access control
2. secret leakage
3. insecure file access
4. external input validation
5. CI/CD credential exposure
6. cloud misconfiguration
7. vulnerable dependencies

These risks should receive early automated tests and security controls.

---

## 19. Security Principle

CareerOps follows:

Never trust external input.

Never trust resource ownership implicitly.

Never store secrets in source code.

Use least privilege.

Fail safely.

Log security-relevant failures without exposing sensitive data.