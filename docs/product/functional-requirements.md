# CareerOps — Functional Requirements

## 1. User Accounts

FR-001 — The system shall allow a user to register an account.

FR-002 — The system shall allow a registered user to log in.

FR-003 — The system shall allow an authenticated user to view their profile.

FR-004 — The system shall prevent users from accessing another user's private data.

---

## 2. User Skill Profile

FR-005 — The system shall allow a user to add skills to their profile.

FR-006 — The system shall allow a user to remove skills from their profile.

FR-007 — The system shall allow a user to update their skill level.

FR-008 — The system shall allow a user to view their current skills.

---

## 3. Opportunity Import

FR-009 — The system shall automatically import internship and junior job opportunities from authorized providers.

FR-010 — The system shall store the source of each imported opportunity.

FR-011 — The system shall store the provider's external identifier when available.

FR-012 — The system shall handle provider failures without crashing the entire platform.

FR-013 — The system shall avoid unauthorized scraping.

---

## 4. Opportunity Normalization

FR-014 — The system shall convert provider-specific job data into a common CareerOps opportunity format.

FR-015 — The normalized opportunity shall support:

- title
- company
- location
- description
- source
- external ID
- application URL
- publication date
- required skills

FR-016 — The system shall validate imported opportunity data before saving it.

---

## 5. Duplicate Detection

FR-017 — The system shall detect duplicate opportunities.

FR-018 — The system shall use the provider external ID when available for duplicate detection.

FR-019 — The system shall support a fallback fingerprint when an external ID is unavailable.

---

## 6. Skill Matching

FR-020 — The system shall compare opportunity skills with user skills.

FR-021 — The system shall calculate a match score for each relevant opportunity.

FR-022 — The system shall show matching skills.

FR-023 — The system shall show missing skills.

---

## 7. Skill-Gap Analysis

FR-024 — The system shall analyze missing skills across relevant opportunities.

FR-025 — The system shall rank frequently requested missing skills.

FR-026 — The system shall help the user identify learning priorities.

---

## 8. Application Tracking

FR-027 — The system shall allow a user to save an opportunity.

FR-028 — The system shall allow a user to create an application from an opportunity.

FR-029 — The system shall allow a user to update an application status.

Supported statuses:

- SAVED
- APPLIED
- FOLLOW_UP
- INTERVIEW
- OFFER
- REJECTED
- ACCEPTED

FR-030 — The system shall store the application date.

FR-031 — The system shall allow users to add application notes.

FR-032 — The system shall allow users to store follow-up dates.

FR-033 — The system shall allow users to store interview dates.

FR-034 — The system shall maintain application status history.

---

## 9. CV Management

FR-035 — The system shall allow a user to upload a CV in PDF format.

FR-036 — The system shall validate CV file type.

FR-037 — The system shall enforce a maximum CV file size.

FR-038 — The system shall allow multiple CV versions.

FR-039 — The system shall allow a CV version to be associated with an application.

FR-040 — The system shall prevent users from accessing CVs belonging to other users.

---

## 10. Reminders

FR-041 — The system shall allow users to create reminders.

FR-042 — The system shall support application follow-up reminders.

FR-043 — The system shall support interview reminders.

FR-044 — The system shall support application deadline reminders.

FR-045 — Reminder processing shall run asynchronously.

---

## 11. Opportunity Search and Filtering

FR-046 — The system shall allow users to list available opportunities.

FR-047 — The system shall allow filtering by role or keyword.

FR-048 — The system shall allow filtering by location.

FR-049 — The system shall allow filtering by job type.

FR-050 — The system shall allow filtering by minimum match score.

---

## 12. Dashboard

FR-051 — The system shall provide application statistics.

FR-052 — The system shall provide opportunity match statistics.

FR-053 — The system shall show upcoming reminders.

FR-054 — The system shall show commonly missing skills.

FR-055 — The system shall show high-match opportunities.