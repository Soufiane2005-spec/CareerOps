# CareerOps — Application Lifecycle

## 1. Purpose

This document defines how a CareerOps application moves through
different statuses during the user's job search process.

The lifecycle helps maintain consistent application tracking,
status history, reminders, analytics, and validation.

---

## 2. Application States

### SAVED

The user is interested in an opportunity but has not yet applied.

Typical actions:

- review opportunity
- compare skill match
- prepare CV
- decide whether to apply

---

### APPLIED

The user has submitted an application through the official
application channel.

CareerOps records the application date.

Possible next states:

- FOLLOW_UP
- INTERVIEW
- REJECTED
- WITHDRAWN

---

### FOLLOW_UP

The user has reached the follow-up stage.

This may happen when:

- the user plans to contact the employer
- no response has been received after a certain period
- CareerOps reminds the user to follow up

Possible next states:

- INTERVIEW
- REJECTED
- WITHDRAWN
- APPLIED

---

### INTERVIEW

The user has been invited to an interview.

CareerOps may store:

- interview date
- notes
- reminder information

Possible next states:

- OFFER
- REJECTED
- WITHDRAWN

---

### OFFER

The employer has made an offer.

Possible next states:

- ACCEPTED
- REJECTED
- WITHDRAWN

---

### ACCEPTED

The user accepts the offer.

This is a terminal state.

---

### REJECTED

The application is rejected by the employer.

This is normally a terminal state.

---

### WITHDRAWN

The user voluntarily stops the application process.

Examples:

- no longer interested
- accepted another offer
- role no longer suitable

This is normally a terminal state.

---

## 3. Main Lifecycle

SAVED
  |
  v
APPLIED
  |
  +------> FOLLOW_UP
  |           |
  |           v
  |       INTERVIEW
  |           |
  |           v
  |         OFFER
  |           |
  |           v
  |        ACCEPTED
  |
  +------> INTERVIEW
  |
  +------> REJECTED
  |
  +------> WITHDRAWN

---

## 4. Alternative Paths

### Rejection After Interview

INTERVIEW
   |
   v
REJECTED

### Withdrawal

APPLIED
   |
   v
WITHDRAWN

or

INTERVIEW
   |
   v
WITHDRAWN

### Follow-Up Without Interview

APPLIED
   |
   v
FOLLOW_UP
   |
   v
REJECTED

---

## 5. Status History

Every application status change should be recorded.

Example:

2026-10-01 — SAVED
2026-10-03 — APPLIED
2026-10-10 — FOLLOW_UP
2026-10-14 — INTERVIEW
2026-10-20 — OFFER

This history allows CareerOps to support:

- analytics
- timeline visualization
- debugging
- user review
- application funnel statistics

---

## 6. Invalid Transitions

CareerOps should prevent clearly invalid transitions.

Examples:

ACCEPTED -> APPLIED

REJECTED -> INTERVIEW

WITHDRAWN -> OFFER

Terminal states should normally not transition to active states.

---

## 7. Reminder Behavior

Certain states may generate reminders.

Examples:

APPLIED
→ follow-up reminder

INTERVIEW
→ interview reminder

OFFER
→ offer response reminder

Reminder logic should remain separate from application status logic.

---

## 8. Design Goals

The application lifecycle must:

- remain simple
- support real-world job search behavior
- preserve status history
- prevent invalid state transitions
- support reminders
- support analytics