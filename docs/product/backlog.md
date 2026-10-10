# CareerOps — Initial Backlog

## 1. Purpose

This backlog converts the CareerOps roadmap into small implementation tasks.

Each task should be:
- clear
- testable
- small enough to complete independently
- linked to a technical area

---

## 2. Backend Foundation

### BE-001 — Create backend project structure

Create the initial backend folder structure with clear separation of concerns.

Definition of Done:
- application package created
- configuration module created
- API structure created
- tests directory created
- project runs locally

---

### BE-002 — Add environment configuration

Add environment-based configuration.

Definition of Done:
- environment variables supported
- `.env` used locally
- secrets not hardcoded
- `.env.example` documented

---

### BE-003 — Add application startup

Create the initial FastAPI application.

Definition of Done:
- application starts successfully
- application metadata configured
- local development command documented

---

### BE-004 — Add health endpoint

Create a health endpoint.

Endpoint:

GET /health

Definition of Done:
- returns successful status
- tested automatically

---

### BE-005 — Add readiness endpoint

Create a readiness endpoint for dependency checks.

Endpoint:

GET /ready

Definition of Done:
- endpoint exists
- dependency behavior documented
- tests added

---

## 3. Database Foundation

### DB-001 — Configure PostgreSQL connection

Definition of Done:
- PostgreSQL connection configured
- credentials come from environment configuration
- connection errors handled

---

### DB-002 — Add database migrations

Introduce database schema migrations.

Definition of Done:
- migration tool configured
- initial migration can run
- rollback tested

---

### DB-003 — Implement initial data models

Implement core entities defined in the CareerOps data model.

Initial entities:
- User
- Profile
- Skill
- UserSkill

---

## 4. Authentication

### AUTH-001 — User registration

Endpoint:

POST /auth/register

Definition of Done:
- validates input
- securely hashes password
- prevents duplicate accounts
- tests included

---

### AUTH-002 — User login

Endpoint:

POST /auth/login

Definition of Done:
- credentials validated
- invalid login handled securely
- authentication token returned

---

### AUTH-003 — Authenticated user endpoint

Endpoint:

GET /users/me

Definition of Done:
- requires authentication
- returns authenticated user's data
- does not expose sensitive fields

---

## 5. User Skills

### SKILL-001 — Create normalized skill catalog

Definition of Done:
- normalized skill entity implemented
- duplicate skill names prevented

---

### SKILL-002 — Add skill to user profile

Definition of Done:
- authenticated user can add a skill
- ownership enforced
- duplicate association prevented

---

### SKILL-003 — Remove skill from user profile

Definition of Done:
- authenticated user can remove own skill
- cannot modify another user's profile

---

### SKILL-004 — List user skills

Definition of Done:
- user skills returned correctly
- tests included

---

## 6. Opportunity Providers

### PROVIDER-001 — Define provider interface

Create a common interface for opportunity providers.

Definition of Done:
- provider contract documented
- common normalized return structure defined

---

### PROVIDER-002 — Implement first authorized provider

Definition of Done:
- provider uses permitted API or feed
- credentials stored securely when required
- rate limits respected
- failures handled

---

## 7. Opportunity Import

### IMPORT-001 — Fetch external opportunities

Definition of Done:
- provider data retrieved
- timeout handling implemented
- failures logged

---

### IMPORT-002 — Validate provider data

Definition of Done:
- required fields validated
- malformed records rejected safely

---

### IMPORT-003 — Normalize opportunity data

Definition of Done:
- provider-specific fields mapped to internal schema
- normalization tests included

---

### IMPORT-004 — Deduplicate opportunities

Definition of Done:
- provider ID + external ID used when available
- fingerprint fallback implemented
- duplicate records prevented

---

### IMPORT-005 — Store import execution history

Definition of Done:
- import start recorded
- import completion recorded
- success and failure counts available

---

## 8. Opportunity API

### OPP-001 — List opportunities

Endpoint:

GET /opportunities

Definition of Done:
- active opportunities returned
- pagination supported

---

### OPP-002 — Get opportunity details

Endpoint:

GET /opportunities/{id}

Definition of Done:
- valid opportunity returned
- missing opportunity handled correctly

---

### OPP-003 — Add opportunity filters

Support filters such as:
- role
- location
- job type
- minimum match score

---

## 9. Matching Engine

### MATCH-001 — Compare user and opportunity skills

Definition of Done:
- matching skills calculated
- missing skills calculated
- unit tests included

---

### MATCH-002 — Calculate match score

Definition of Done:
- deterministic scoring rule defined
- edge cases tested

---

### MATCH-003 — Rank opportunities by relevance

Definition of Done:
- opportunities can be sorted by user match score

---

## 10. Skill Gap Intelligence

### GAP-001 — Aggregate missing skills

Definition of Done:
- missing skills across relevant jobs can be counted

---

### GAP-002 — Rank learning priorities

Definition of Done:
- frequently missing skills ranked
- dashboard-ready output available

---

## 11. Applications

### APP-001 — Save opportunity as application

Definition of Done:
- authenticated user can create application
- initial status validated

---

### APP-002 — Update application status

Definition of Done:
- valid state transitions enforced
- invalid transitions rejected

---

### APP-003 — Store application status history

Definition of Done:
- every status transition recorded

---

### APP-004 — Add application notes

Definition of Done:
- notes stored securely
- ownership enforced

---

## 12. CV Management

### CV-001 — Upload CV metadata

Definition of Done:
- authenticated user can create CV record
- file ownership stored

---

### CV-002 — Validate uploaded CV

Definition of Done:
- PDF type validated
- size limit enforced
- invalid uploads rejected

---

### CV-003 — Store CV privately

Definition of Done:
- file storage abstraction created
- unauthorized access prevented

---

### CV-004 — Link CV to application

Definition of Done:
- user can associate owned CV with owned application

---

## 13. Reminders

### REM-001 — Create reminder

Definition of Done:
- user can schedule reminder
- reminder linked to owned application

---

### REM-002 — Process due reminders

Definition of Done:
- background processing supported
- failures handled safely

---

### REM-003 — Add reminder retry behavior

Definition of Done:
- failed task retried
- exhausted failures handled separately

---

## 14. Docker

### DOCKER-001 — Containerize API

Definition of Done:
- API Docker image builds
- container starts successfully
- non-development configuration supported

---

### DOCKER-002 — Create local Docker Compose environment

Definition of Done:
- API runs
- PostgreSQL runs
- dependencies start together

---

## 15. Testing

### TEST-001 — Configure pytest

Definition of Done:
- test command documented
- test environment isolated

---

### TEST-002 — Add API integration tests

Definition of Done:
- authentication tested
- ownership tested
- main API flows tested

---

## 16. Security

### SEC-001 — Add secret scanning

### SEC-002 — Add dependency scanning

### SEC-003 — Add static analysis

### SEC-004 — Add container scanning

### SEC-005 — Add infrastructure scanning

### SEC-006 — Test broken access control protections

---

## 17. Infrastructure

### INFRA-001 — Terraform foundation

### INFRA-002 — AWS networking

### INFRA-003 — ECR

### INFRA-004 — ECS API service

### INFRA-005 — RDS PostgreSQL

### INFRA-006 — S3 CV storage

### INFRA-007 — SQS queues

### INFRA-008 — Worker services

### INFRA-009 — Secrets Manager

### INFRA-010 — CloudWatch monitoring

All AWS implementation must follow the CareerOps cost guardrails.

---

## 18. CI/CD

### CI-001 — Run tests on pull requests

### CI-002 — Run security scans

### CI-003 — Build container image

### CI-004 — Publish immutable image

### CI-005 — Configure GitHub OIDC

### CD-001 — Deploy development environment

### CD-002 — Deploy production-demo environment

### CD-003 — Add deployment validation

### CD-004 — Add rollback strategy

---

## 19. Observability

### OBS-001 — Structured application logs

### OBS-002 — API metrics

### OBS-003 — Worker metrics

### OBS-004 — Queue monitoring

### OBS-005 — Alerts

---

## 20. Reliability

### REL-001 — Retry strategy

### REL-002 — Dead-letter queue handling

### REL-003 — Backup strategy

### REL-004 — Restore test

### REL-005 — Failure simulation

---

## 21. Documentation

### DOC-001 — Local setup guide

### DOC-002 — Architecture documentation

### DOC-003 — API documentation

### DOC-004 — Deployment guide

### DOC-005 — Security documentation

### DOC-006 — Final portfolio case study