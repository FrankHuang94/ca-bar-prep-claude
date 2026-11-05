---
subject: mbe
topic: Tracker for licensed practice questions
coverage_ids: []
tested_on: [MBE]
exam_frequency: {level: n/a, basis: "Personal log"}
last_verified: 2026-11-05
status: verified
---

# Official / commercial practice tracker

Licensed questions (NCBE study aids, commercial question banks) are **never copied into this repo**.
Log each attempt by ID only, so the dashboard counts it:

```bash
python scripts/quiz.py log --source official --item "NCBE-<product>-<set>-Q<n>" --subject EVD --correct N \
    --seconds 110 --coverage EVD-MBE-V.F --error-type misapplied --notes "present sense impression vs excited utterance"
```

Use `--source commercial` for commercial banks.

## Resources in use

| Resource | Type | Questions available | Started | Done | Notes |
|---|---|---|---|---|---|
