# CareerOps — Opportunity Lifecycle

## 1. Purpose

This document defines how an opportunity moves through CareerOps
from initial discovery to expiration or deactivation.

The lifecycle ensures imported opportunities are validated,
normalized, deduplicated, stored, updated, and retired consistently.

---

## 2. Lifecycle States

### DISCOVERED

The opportunity has been received from an authorized provider.

At this stage, the provider data is considered untrusted input.

---

### VALIDATED

CareerOps validates required fields such as:

- title
- company
- application URL
- description
- publication date when available

Invalid opportunities are rejected or skipped and logged.

---

### NORMALIZED

Provider-specific fields are converted into CareerOps' internal
opportunity format.

Example:

provider field:

position_name

or:

jobTitle

becomes:

title

---

### DEDUPLICATED

CareerOps determines whether the opportunity already exists.

Duplicate detection should use:

1. provider ID + external opportunity ID when available
2. fallback opportunity fingerprint when necessary

If the opportunity already exists, CareerOps updates the existing
record instead of creating a duplicate.

---

### ACTIVE

The opportunity is valid, normalized, stored, and available for:

- user discovery
- filtering
- skill matching
- recommendations
- application tracking

---

### UPDATED

An active opportunity may change after a later provider import.

Examples:

- description updated
- deadline changed
- location changed
- required skills changed

CareerOps updates the existing opportunity while preserving its
internal identity.

---

### EXPIRED

An opportunity becomes expired when:

- its known deadline passes
- the provider marks it closed
- the source explicitly indicates that applications are no longer accepted

Expired opportunities should not appear as active recommendations.

Historical application records may still reference them.

---

### INACTIVE

An opportunity may become inactive when:

- it is removed by the provider
- the source becomes unavailable for an extended period
- the record is intentionally disabled

Inactive opportunities remain stored when useful for history but
are excluded from active discovery.

---

## 3. Lifecycle Flow

DISCOVERED
    |
    v
VALIDATED
    |
    v
NORMALIZED
    |
    v
DEDUPLICATED
    |
    v
ACTIVE
    |
    +----> UPDATED ----+
    |                  |
    +------------------+
    |
    +----> EXPIRED
    |
    +----> INACTIVE

---

## 4. Invalid Opportunity Flow

DISCOVERED
    |
    v
VALIDATION FAILED
    |
    v
LOG / SKIP

Invalid provider data must not cause the complete import process
to fail.

---

## 5. Duplicate Opportunity Flow

Imported Opportunity
        |
        v
Duplicate Detection
        |
   +----+----+
   |         |
  NO        YES
   |         |
CREATE     UPDATE
   |         |
   +----> ACTIVE

---

## 6. Design Goals

The lifecycle must:

- avoid duplicate opportunities
- tolerate invalid provider data
- support provider updates
- preserve historical references
- prevent expired jobs from appearing as active recommendations
- avoid making provider failures affect the full CareerOps platform