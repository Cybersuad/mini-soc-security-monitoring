
# Detection Rule Documentation

## SOC-001: Multiple Failed Login Attempts

**Category:** Authentication Security  
**Data Source:** Windows Security Event Logs  
**Event ID:** 4625  
**Severity:** Medium  
**Status:** Implemented; detection logic tested

## Objective

Identify multiple failed login attempts against the same account within a short period.

## Detection Logic

1. Collect Windows Security Event ID 4625.
2. Extract the target account from the event message.
3. Group events by account and five-minute time bucket.
4. Count failed login attempts.
5. Report groups containing five or more failures.

## Detection Threshold

5 failed login attempts per account within a fixed
5-minute bucket.

## Possible Explanations

- Password guessing
- Repeated incorrect passwords
- Misconfigured Windows services
- Outdated stored credentials
- Automated authentication failures

## Limitations

The rule does not prove that a brute-force attack occurred.

Fixed time buckets can miss sequences crossing bucket boundaries.

Norwegian-language field extraction may require adjustments
for other Windows languages or event formats.

## Validation

Six synthetic failed-login events produced one matching
result with status INVESTIGATE.

Scheduled execution of SOC-001 was confirmed separately.

A dedicated synthetic alert successfully validated
Splunk's triggered-alert functionality.
