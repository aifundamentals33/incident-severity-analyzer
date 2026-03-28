#!/usr/bin/env python3
"""
Minimal CLI tool to analyze incident descriptions and output severity.
"""

import sys
import re

# Severity keywords with weights
CRITICAL_KEYWORDS = {
    "outage": 10, "down": 10, "failure": 8, "critical": 10,
    "breach": 10, "data loss": 9, "corruption": 8, "emergency": 10
}
HIGH_KEYWORDS = {
    "degraded": 6, "slow": 5, "error": 6, "warning": 5,
    "unavailable": 7, "issue": 4, "problem": 4
}
MEDIUM_KEYWORDS = {
    "intermittent": 4, "occasional": 3, "minor": 3, "flaky": 3
}
LOW_KEYWORDS = {
    "cosmetic": 1, "typo": 1, "ui": 1, "enhancement": 1
}

def analyze_severity(description: str) -> tuple[str, int]:
    """Analyze incident description and return severity level and score."""
    desc_lower = description.lower()
    score = 0

    for keyword, weight in CRITICAL_KEYWORDS.items():
        if keyword in desc_lower:
            score += weight
    for keyword, weight in HIGH_KEYWORDS.items():
        if keyword in desc_lower:
            score += weight
    for keyword, weight in MEDIUM_KEYWORDS.items():
        if keyword in desc_lower:
            score += weight
    for keyword, weight in LOW_KEYWORDS.items():
        if keyword in desc_lower:
            score += weight

    if score >= 15:
        return "CRITICAL", score
    elif score >= 8:
        return "HIGH", score
    elif score >= 4:
        return "MEDIUM", score
    else:
        return "LOW", score

def main():
    if len(sys.argv) < 2:
        print("Usage: python incident_analyzer.py <incident_description>")
        print("Example: python incident_analyzer.py 'Server is down, critical outage'")
        sys.exit(1)

    description = " ".join(sys.argv[1:])
    severity, score = analyze_severity(description)

    print(f"Incident: {description}")
    print(f"Severity: {severity} (score: {score})")

if __name__ == "__main__":
    main()
