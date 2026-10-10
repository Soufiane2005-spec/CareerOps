# CareerOps — Environment Strategy

## 1. Purpose

CareerOps uses separate environments to isolate development,
testing, and production-like workloads.

The environment strategy helps reduce deployment risk, improve
security, control cloud costs, and support reliable testing.

---

## 2. Local Environment

The local environment runs on the developer workstation.

Purpose:

- application development
- debugging
- fast local testing
- unit and integration testing
- Docker testing
- development without unnecessary AWS costs

Initial local components may include:

- FastAPI application
- PostgreSQL
- background workers
- local queue implementation or emulator
- Docker Compose

Local secrets must be stored in environment variables and must not
be committed to Git.

---

## 3. Development Environment

Environment name:

dev

The development environment runs on AWS and is used to test:

- Terraform infrastructure
- AWS networking
- ECS deployments
- application integrations
- CI/CD workflows
- security scans and controls
- monitoring configuration

The development environment should prioritize low cost.

Example principles:

- minimal ECS task count
- small database configuration
- limited resource capacity
- temporary infrastructure where possible

---

## 4. Production-Demo Environment

Environment name:

prod-demo

The production-demo environment represents the production-style
CareerOps architecture used for final testing and portfolio
demonstration.

It should demonstrate:

- secure networking
- multiple application tasks where appropriate
- autoscaling
- monitoring and alerting
- WAF protection
- backups
- controlled deployments
- blue/green deployment
- automated rollback
- disaster recovery procedures

The production-demo environment does not need to remain running
continuously when not required.

---

## 5. Environment Isolation

Each AWS environment should have separate:

- resources
- databases
- secrets
- IAM permissions where appropriate
- configuration
- logs
- deployment controls

Development resources must not depend on production-demo data.

---

## 6. Naming Convention

Resources should include project and environment names.

Examples:

careerops-dev-vpc

careerops-dev-api

careerops-dev-db

careerops-prod-demo-vpc

careerops-prod-demo-api

careerops-prod-demo-db

---

## 7. Tagging

AWS resources should include tags such as:

Project = CareerOps

Environment = dev

or:

Environment = prod-demo

ManagedBy = Terraform

---

## 8. Configuration Strategy

Application code should remain the same across environments.

Environment-specific behavior must come from configuration.

Examples:

- database URL
- provider API credentials
- storage bucket
- queue URL
- log level

Secrets must never be hardcoded into source code.

---

## 9. Promotion Flow

Changes should generally move through:

Local
  |
  v
Dev
  |
  v
Prod-Demo

Code and infrastructure should be validated in development before
production-demo deployment.

---

## 10. Design Goals

The environment strategy should provide:

- safe testing
- clear isolation
- reproducible infrastructure
- controlled deployments
- lower AWS cost
- improved security