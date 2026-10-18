
# Mini-SOC Test Results

## Test 1 - Windows Log Ingestion

**Objective:** Verify that Splunk receives Windows Security logs.

**Method:** Search the WinEventLog:Security sourcetype.

**Result:** Successful.

Splunk returned real Windows Security events,
including Event IDs 4624, 4625 and 4672.

## Test 2 - Detection Logic

**Objective:** Confirm that six synthetic failed login
attempts match the SOC-001 threshold.

**Test account:** SOC_TEST_USER

**Expected:** One detection with INVESTIGATE status.

**Observed:** One result containing six failed attempts.

**Result:** PASS.

## Test 3 - Scheduled Search

**Objective:** Confirm SOC-001 runs automatically.

**Method:** Inspect Splunk internal scheduler logs.

**Observed:** Successful scheduled executions.
Visible executions returned zero matching results.

**Result:** PASS for scheduled execution.

## Test 4 - Triggered Alert Mechanism

**Objective:** Verify automatic triggered-alert creation.

**Method:** Create a separate scheduled test alert
returning one synthetic result.

**Observed:** Four triggered test alerts.

**Result:** PASS.

The test alert was disabled after validation.

## Remaining Validation

An end-to-end test demonstrating SOC-001 triggering
from collected Windows Event ID 4625 events has not
yet been completed.
