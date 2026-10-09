# CareerOps — MVP Definition

## 1. MVP Goal

The first version of CareerOps must provide real value to students,
recent graduates, and junior technology professionals by helping them
discover relevant opportunities, understand skill compatibility, and
organize their applications.

The MVP should remain small enough to build, test, secure, deploy,
and operate professionally.

## 2. Core MVP Features

### 2.1 User Authentication

Users must be able to:

- register
- log in
- access their own profile
- access only their own private data

### 2.2 User Skill Profile

Users must be able to:

- add skills
- remove skills
- view their current skills
- update their skill profile

Example skills include:

- AWS
- Docker
- Linux
- Terraform
- Python
- Kubernetes
- Cybersecurity

### 2.3 Automatic Opportunity Import

CareerOps must automatically import internship and junior job
opportunities from at least one authorized API or public job feed.

The MVP must not depend on unauthorized scraping.

### 2.4 Opportunity Normalization

Imported opportunities must be converted into a common internal
format regardless of provider structure.

The normalized opportunity should contain fields such as:

- external ID
- title
- company
- location
- description
- source
- application URL
- publication date
- required skills

### 2.5 Skill Matching

CareerOps must compare the user's skill profile with the skills
required by an opportunity.

The system must provide:

- matching skills
- missing skills
- match score

### 2.6 Skill-Gap Analysis

CareerOps must analyze relevant opportunities to identify skills
frequently requested by employers but missing from the user's profile.

This information should help users prioritize what to learn next.

### 2.7 Application Tracking

Users must be able to save and track applications using statuses such as:

- SAVED
- APPLIED
- FOLLOW_UP
- INTERVIEW
- OFFER
- REJECTED
- ACCEPTED

## 3. MVP Quality Requirements

The MVP must include:

- clean code structure
- input validation
- proper error handling
- automated tests
- secure authentication
- environment-based configuration
- documentation

Later phases will add production AWS infrastructure, CI/CD,
DevSecOps controls, monitoring, autoscaling, disaster recovery,
and FinOps.

## 4. Out of Scope for MVP

The first version will not include:

- LinkedIn scraping
- unauthorized job scraping
- mobile application
- AI chatbot
- automatic CV rewriting
- recruiter messaging automation
- advanced machine-learning recommendations
- large numbers of job providers
- social networking features

These features may be evaluated after the core platform is stable.

## 5. MVP Success Criteria

The MVP is successful when a user can:

1. create an account
2. create a skill profile
3. receive automatically imported opportunities
4. view opportunity details
5. view skill match scores
6. identify missing skills
7. save and track an application