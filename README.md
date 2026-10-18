
# Mini-SOC | Security Monitoring & Threat Detection

A personal cybersecurity project focused on building a small Security Operations Center (SOC) environment using Splunk Enterprise and Windows Security Event Logs.

## Project Screenshots

### Security Monitoring Dashboard

![Mini-SOC Security Dashboard](screenshots/dashboard.png)

### Detection Logic Validation

![SOC-001 Detection Test](screenshots/detection-test.png)

### Automated Alert Validation

![Splunk Alert Validation](screenshots/alert-validation.png)

## Project Overview

The goal of this project was to gain hands-on experience with security monitoring, log analysis, threat detection, and automated alerting.

I configured a local Splunk environment to collect and analyze real Windows security events, developed SPL-based detection logic, and built an interactive security dashboard.

## Technologies Used

- Splunk Enterprise
- Windows Event Logs
- Search Processing Language (SPL)
- Python
- XML / Splunk Classic Dashboards
- Windows PowerShell

## Architecture

Windows Endpoint
    |
    v
Windows Security Event Logs
    |
    v
Splunk Enterprise
    |
    +-- Security Event Analysis
    +-- SPL Detection Rules
    +-- Scheduled Alerts
    +-- Security Dashboard

## Dashboard Features

The dashboard contains eight visualization panels:

1. Total Security Events
2. Failed Login Attempts
3. Authentication Activity Over Time
4. Top Failed Login Accounts
5. Security Investigation - Failed Logins
6. SOC-001 Brute-Force Detection
7. Privileged Logon Activity
8. Security Event Distribution

## Detection Rule: SOC-001

SOC-001 identifies accounts with five or more failed login attempts within the same five-minute time bucket.

The detection uses Windows Event ID 4625 and extracts the target account from Norwegian Windows event messages.

Matching events are marked for investigation.

The detection is intended to identify potentially suspicious authentication patterns. A matching event is not necessarily evidence of an attack.

## Validation

The project included the following tests:

- Confirmed ingestion of real Windows Security events
- Tested detection logic with six synthetic failed-login events
- Confirmed scheduled SOC-001 search execution through Splunk scheduler logs
- Validated the alerting mechanism using a separate scheduled test alert
- Observed four triggered test alerts

The synthetic detection test and the alert-action test were performed separately.

An end-to-end trigger of SOC-001 using actual Windows authentication events has not yet been demonstrated.

## Limitations

- The environment monitors one local Windows endpoint.
- Detection coverage focuses primarily on authentication events.
- Some field extractions depend on Norwegian Windows event-message formatting.
- SOC-001 uses fixed five-minute time buckets.
- Alert thresholds require tuning to reduce false positives.
- A triggered detection requires analyst investigation before an incident can be confirmed.

## Future Improvements

- Sysmon integration
- More advanced correlation rules
- MITRE ATT&CK mapping
- Improved alert triage and severity classification
- Additional monitored endpoints

## Repository Structure

- `splunk/` - Dashboard XML and SPL detection logic
- `docs/` - Detection documentation, investigation notes, and validation results
- `screenshots/` - Sanitized screenshots of the environment
- `log_generator.py` - Synthetic authentication log generator

## Security and Privacy

This repository does not contain raw Windows Security logs, credentials, or real authentication data exports.

Screenshots are sanitized before publication.

## Project Status

Version 1.0 - Local monitoring and core validation completed.
