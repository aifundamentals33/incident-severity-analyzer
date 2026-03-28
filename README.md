# Incident Severity Analyzer

## Problem

Engineering teams waste critical time triaging incidents. When an alert fires, responders must quickly understand severity to prioritize response—but keyword-based triage is error-prone and inconsistent across team members.

## Solution

A lightweight CLI tool that analyzes incident descriptions using weighted keyword scoring to instantly classify severity: **CRITICAL**, **HIGH**, **MEDIUM**, or **LOW**.

## ITIL 4 Value Statement

**Value Co-Creation**: Reduces MTTR (Mean Time To Resolution) by enabling instant, consistent triage—freeing engineers to focus on fixing issues, not classifying them.

**Focus on Outcomes**: Eliminates subjective severity decisions. Same incident = same score, every time.

**Service Level Thinking**: Faster triage = faster resolution = better SLA compliance for incident response.

**Continual Improvement**: Open-source, extensible keyword engine—teams can tune weights based on their incident history.

## Business Impact

| Metric | Improvement |
|--------|-------------|
| Triage Time | Seconds vs. minutes |
| Consistency | 100% reproducible scoring |
| Dependencies | Zero—runs anywhere with Python |
| Learning Curve | None—just run and read |

## Tech Stack

- **Python 3**: Pure stdlib, no external packages needed
- **Keyword-weighted algorithm**: Fast, transparent, customizable

## How to Run

```bash
# Analyze an incident
python incident_analyzer.py "Server is down, critical outage"
# Output: Severity: CRITICAL (score: 30)

# More examples
python incident_analyzer.py "API is slow and returning errors"
# Output: Severity: HIGH (score: 11)

python incident_analyzer.py "Minor UI typo in footer"
# Output: Severity: MEDIUM (score: 5)
```

## Severity Scoring

| Level     | Score | Keywords |
|-----------|-------|----------|
| CRITICAL  | 15+   | outage, down, breach, emergency |
| HIGH      | 8+    | degraded, error, unavailable |
| MEDIUM    | 4+    | intermittent, minor, flaky |
| LOW       | <4    | cosmetic, typo |

---

*Built with AI assistance. ITIL 4-aligned.*
