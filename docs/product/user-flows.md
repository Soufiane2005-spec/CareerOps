# CareerOps — User Flows

## 1. Purpose

This document defines the main user journeys through CareerOps.

The objective is to ensure that the product workflow is clear before
backend implementation begins.

---

## 2. User Registration Flow

1. User opens CareerOps.
2. User creates an account.
3. CareerOps validates the registration data.
4. CareerOps stores the user securely.
5. User logs in.
6. CareerOps returns access to the authenticated area.

Flow:

Visitor
→ Register
→ Validate
→ Account Created
→ Login
→ Authenticated User

---

## 3. Skill Profile Flow

1. Authenticated user opens their profile.
2. User adds skills.
3. CareerOps normalizes the selected skills.
4. Skills are associated with the user.
5. User can update or remove skills later.

Example:

User
→ Add AWS
→ Add Docker
→ Add Terraform
→ Save Profile

---

## 4. Automatic Opportunity Discovery Flow

1. CareerOps starts a scheduled import process.
2. An authorized job provider is contacted.
3. Opportunities are received.
4. Provider data is validated.
5. Opportunity data is normalized.
6. Duplicates are detected.
7. New opportunities are stored.
8. Existing opportunities may be updated.

Flow:

Authorized Provider
→ Importer
→ Validation
→ Normalization
→ Deduplication
→ Database

---

## 5. Opportunity Matching Flow

1. CareerOps retrieves a stored opportunity.
2. Required skills are identified.
3. CareerOps retrieves the user's skill profile.
4. User skills are compared with opportunity skills.
5. A match score is calculated.
6. Matching skills are displayed.
7. Missing skills are displayed.

Flow:

Opportunity Skills
+
User Skills
→ Matching Engine
→ Match Score
→ Missing Skills

---

## 6. Opportunity Discovery Flow

1. User opens the opportunity dashboard.
2. CareerOps displays imported opportunities.
3. User may filter opportunities.
4. Opportunities may be ranked by match score.
5. User opens an opportunity.
6. CareerOps displays:
   - company
   - title
   - location
   - description
   - required skills
   - match score
   - missing skills
   - source
   - application URL

---

## 7. Application Tracking Flow

1. User selects an opportunity.
2. User saves the opportunity.
3. User applies through the official application URL.
4. User marks the application as APPLIED.
5. CareerOps records the application date.
6. User may add notes.
7. User may attach a CV version.
8. User may create a follow-up reminder.
9. Application status may later change.

Example lifecycle:

SAVED
→ APPLIED
→ FOLLOW_UP
→ INTERVIEW
→ OFFER
→ ACCEPTED

Alternative outcomes:

APPLIED
→ REJECTED

INTERVIEW
→ REJECTED

---

## 8. Reminder Flow

1. User creates a reminder.
2. Reminder is scheduled.
3. Background processing checks due reminders.
4. Due reminder is processed asynchronously.
5. Notification is generated.
6. Reminder status is updated.

Flow:

User
→ Create Reminder
→ Queue
→ Worker
→ Notification

---

## 9. Skill-Gap Analysis Flow

1. CareerOps analyzes relevant opportunities.
2. Required skills are aggregated.
3. User skills are compared against market demand.
4. Missing skills are counted.
5. Frequently requested missing skills are ranked.
6. CareerOps shows learning priorities.

Example:

Kubernetes — missing in 35 jobs
Ansible — missing in 21 jobs
Helm — missing in 14 jobs

Result:

Recommended learning priority:
1. Kubernetes
2. Ansible
3. Helm

---

## 10. CV Management Flow

1. User uploads a PDF CV.
2. CareerOps validates file type and size.
3. CV metadata is stored.
4. File is stored privately.
5. User may create multiple CV versions.
6. A CV version may be linked to an application.
7. Only the owner may access the CV.

---

## 11. Failure Flow — Job Provider

1. CareerOps contacts a provider.
2. Provider returns an error or times out.
3. CareerOps records the failure.
4. The platform remains available.
5. Import may be retried later.
6. Other providers continue operating if available.

The failure of one external provider must not break CareerOps.

---

## 12. Failure Flow — Background Job

1. Worker receives a task.
2. Task fails.
3. Task is retried.
4. If retries are exhausted, the task is moved to a failed-job mechanism such as a DLQ.
5. The failure is logged and monitored.

---

## 13. Security Flow — Private Data Access

1. User sends an authenticated request.
2. CareerOps identifies the authenticated user.
3. CareerOps loads the requested resource.
4. CareerOps verifies resource ownership.
5. Access is allowed only if the resource belongs to the authenticated user.

Example:

User A
→ requests CV belonging to User B
→ ownership check fails
→ access denied