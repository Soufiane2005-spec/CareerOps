# CareerOps — Git Workflow

## 1. Purpose

This document defines the Git workflow used by CareerOps.

The objective is to keep development organized, reviewable, and safe.

---

## 2. Main Branch

The main stable branch is:

master

The master branch should contain working and reviewed code.

Direct development on master should be avoided once implementation begins.

---

## 3. Feature Branches

Each significant change should be developed in its own branch.

Examples:

feature/authentication

feature/opportunity-importer

feature/matching-engine

feature/application-tracking

feature/cv-management

feature/reminders

infra/aws-networking

infra/ecs

infra/rds

security/container-scanning

fix/application-status-validation

docs/update-architecture

---

## 4. Branch Naming

Recommended prefixes:

feature/   new application functionality

fix/       bug fixes

infra/     infrastructure and Terraform

security/  security improvements

test/      test-related work

docs/      documentation

chore/     maintenance work

Examples:

feature/user-skills

infra/aws-vpc

security/add-trivy-scan

fix/opportunity-deduplication

---

## 5. Development Flow

The normal workflow is:

master
  |
  v
create branch
  |
  v
implement change
  |
  v
test locally
  |
  v
commit changes
  |
  v
push branch
  |
  v
open pull request
  |
  v
CI checks
  |
  v
review
  |
  v
merge into master

---

## 6. Commit Strategy

Commits should be small and focused.

Each commit should represent one logical change.

Examples:

feat: add user registration endpoint

fix: prevent duplicate opportunity imports

test: add application lifecycle tests

infra: add AWS VPC module

security: add container vulnerability scanning

docs: document deployment architecture

---

## 7. Commit Prefixes

CareerOps uses simple conventional commit prefixes:

feat:
fix:
test:
docs:
infra:
security:
refactor:
chore:

---

## 8. Pull Requests

Before merging a pull request:

- code should run successfully
- automated tests should pass
- security checks should pass
- infrastructure validation should pass when relevant
- secrets must not be committed
- documentation should be updated when necessary

---

## 9. Protected Main Branch

When the GitHub repository is configured, the main branch should
eventually require pull requests and successful CI checks before merge.

Direct force pushes should be avoided.

---

## 10. Secrets

Secrets must never be committed to Git.

Files such as:

.env

must remain ignored.

If a real secret is accidentally committed, deleting the file alone
is not enough. The secret must also be rotated.

---

## 11. Definition of Done

A change is considered complete when:

- implementation is finished
- tests pass
- documentation is updated if required
- no secrets are included
- commits are clear
- pull request checks pass
- change is merged cleanly