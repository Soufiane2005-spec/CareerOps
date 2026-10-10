# CareerOps — Architecture V1

## 1. Purpose

This document defines the first logical architecture of CareerOps.

The architecture is intentionally technology-aware but not yet tied
to every production AWS implementation detail.

The goal is to define clear responsibilities between components
before implementation begins.

---

## 2. High-Level Architecture

Users
  |
  v
CareerOps API
  |
  +-------------------+
  |                   |
  v                   v
PostgreSQL         Object Storage
  |                   |
  |                   +---- CV files
  |
  +---- Users
  +---- Profiles
  +---- Skills
  +---- Opportunities
  +---- Applications
  +---- Reminders
  +---- Providers
  +---- Import Runs

CareerOps API
  |
  v
Job Queue
  |
  +----------+-----------+
  |          |           |
  v          v           v
Importer   Matching    Reminder
Worker     Worker      Worker

Importer Worker
  |
  v
Authorized Job Providers

---

## 3. API Component

The CareerOps API is responsible for:

- authentication
- user profile management
- skill management
- opportunity access
- application tracking
- CV metadata management
- dashboard data
- creating asynchronous jobs

The API should not perform long-running work synchronously.

---

## 4. Database

PostgreSQL stores relational application data.

Main entities include:

- User
- Profile
- Skill
- UserSkill
- Company
- Provider
- Opportunity
- OpportunitySkill
- Application
- ApplicationStatusHistory
- CV
- Reminder
- ImportRun

---

## 5. Object Storage

CV files are stored separately from the relational database.

The database stores metadata such as:

- owner
- file name
- storage key
- checksum
- file size

Production storage will use private object storage.

---

## 6. Opportunity Importer

The importer is responsible for:

1. contacting authorized job providers
2. receiving opportunity data
3. validating external input
4. normalizing provider-specific structures
5. detecting duplicates
6. creating or updating opportunities
7. recording import execution results

Provider failures must not make the entire CareerOps platform unavailable.

---

## 7. Matching Worker

The matching worker is responsible for:

- comparing user skills with opportunity skills
- calculating match scores
- identifying matching skills
- identifying missing skills
- supporting skill-gap analysis

Matching work may execute asynchronously when the workload becomes large.

---

## 8. Reminder Worker

The reminder worker handles:

- follow-up reminders
- interview reminders
- deadline reminders

Reminder processing must not block normal API requests.

---

## 9. Queue

Queues decouple the API and background workers.

Queues support:

- asynchronous processing
- retries
- workload buffering
- independent worker scaling
- failed-task handling

The production AWS architecture will use Amazon SQS where appropriate.

---

## 10. External Providers

CareerOps integrates only with authorized APIs, public feeds, or
other permitted data sources.

External provider integrations must use a common provider interface.

CareerOps must not depend on unauthorized LinkedIn scraping.

---

## 11. Initial AWS Mapping

Logical Component -> AWS Service

API -> ECS Fargate

Database -> RDS PostgreSQL

CV Storage -> S3

Job Queues -> SQS

Background Workers -> ECS Fargate Workers

Container Registry -> ECR

Public Entry Point -> Application Load Balancer

Secrets -> Secrets Manager

Monitoring -> CloudWatch

Edge Protection -> AWS WAF

Notifications -> SNS where appropriate

---

## 12. Security Boundaries

### Internet Boundary

All public traffic is considered untrusted.

Production traffic will pass through controlled public entry points
before reaching the application.

### External Provider Boundary

Data received from external providers must be validated before
storage or processing.

### User Data Boundary

Private information such as:

- CV files
- application history
- profile information

must be accessible only to the owning user.

### Credential Boundary

Secrets and cloud credentials must not be stored in source code.

---

## 13. Design Principles

CareerOps architecture must follow:

- separation of concerns
- least privilege
- asynchronous processing for background workloads
- provider abstraction
- secure-by-design principles
- infrastructure as code
- observable services
- failure isolation
- cost awareness