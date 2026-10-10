# CareerOps — AWS Cost Guardrails

## 1. Objective

CareerOps is a portfolio and learning project running under a
limited AWS budget.

The infrastructure must demonstrate professional AWS architecture
without allowing unnecessary cloud costs.

CareerOps therefore follows a free-first and cost-aware strategy.

---

## 2. General Rule

AWS resources must not be created only because they appear in the
final architecture.

Every resource must have:

- a technical purpose
- a learning objective
- an understood cost impact
- a cleanup strategy

---

## 3. Local-First Development

Most application development should happen locally.

Local development will use:

- FastAPI
- Docker
- Docker Compose
- PostgreSQL
- background workers
- automated tests
- security scanning tools

AWS should only be used when an AWS-specific feature needs to be
implemented or tested.

---

## 4. AWS Development Environment

The AWS development environment must prioritize low cost.

Principles:

- minimum required ECS tasks
- smallest practical database configuration
- minimal log retention
- no unnecessary high-availability resources
- expensive resources should not remain running when unused
- infrastructure should be destroyed after temporary testing when practical

---

## 5. Production-Demo Environment

The prod-demo environment may demonstrate production-oriented
features such as:

- multiple ECS tasks
- Application Load Balancer
- autoscaling
- WAF
- monitoring
- backups
- blue/green deployment
- automated rollback

The prod-demo environment does not need to run continuously.

It should be deployed for:

- testing
- evidence collection
- portfolio demonstrations
- final project validation

and destroyed when no longer required.

---

## 6. Cost-Sensitive Services

Extra attention must be given before creating services such as:

- NAT Gateway
- RDS
- Application Load Balancer
- continuously running ECS Fargate tasks
- AWS WAF
- public IPv4 resources
- VPC endpoints
- large CloudWatch log retention

The expected cost should be reviewed before deployment.

---

## 7. AWS Budget Protection

The AWS account must use budget alerts.

Resources must use tags such as:

Project = CareerOps
Environment = dev
ManagedBy = Terraform

These tags help identify and review CareerOps-related costs.

---

## 8. Infrastructure Lifecycle

Terraform-managed environments should follow:

terraform plan
    |
    v
terraform apply
    |
    v
Test / Learn / Demo
    |
    v
Collect Evidence
    |
    v
terraform destroy

Temporary resources must not be forgotten after testing.

---

## 9. Cost Review Rule

Before adding a new AWS service, CareerOps must answer:

1. Why is this service needed?
2. Is it required for the current phase?
3. Is there a cheaper development alternative?
4. Does the current AWS offer cover its intended usage?
5. How will the resource be stopped or destroyed?
6. What evidence should be collected before destruction?

---

## 10. Project Priority

CareerOps prioritizes:

learning
+
security
+
reliability
+
cost awareness

The project must not spend additional AWS money simply to make the
architecture appear more complex.