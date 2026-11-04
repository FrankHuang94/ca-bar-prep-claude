---
description: Re-check calbar.ca.gov and ncbex.org for changes; update 00-exam-intel and flag plan impacts
argument-hint: "[focus, e.g. 'deadlines' or 'rules']"
---
Refresh exam intelligence. Optional focus: $ARGUMENTS

**Method**
- Try WebFetch on primary pages first. If the environment blocks them, use WebSearch with `allowed_domains` (calbar.ca.gov, ncbex.org, courts.ca.gov, leginfo.legislature.ca.gov, uscourts.gov, supremecourt.gov) and mark facts `confirmed-primary (search)`.
- **Cap: 40 searches.** If you delegate, give each agent an explicit cap.

**Check, in priority order**
1. **July 2027 exam page:**
   - application open, timely and final deadlines; proof-of-eligibility deadline;
   - test sites; laptop/Examplify and mock-exam dates; admittance tickets; results date;
   - fees (Appendix A).
2. **Eligibility:**
   - foreign-education guidelines (LLM units, online study, the 36-month limit);
   - anything bearing on V-012, V-014 or V-015;
   - registration and moral character timing.
3. **Exam scope and format:**
   - the Scope page and the CBX outlines;
   - grading/scaling changes;
   - any statement about the February 2028 format;
   - the NextGen and California-component timeline;
   - MPRE dates.
4. **Law changes since `last_verified`:**
   - FRE/FRCP amendments (and their Dec 1 status);
   - California Rules of Professional Conduct orders;
   - CCP, Evidence Code, Probate Code and Family Code statutes effective Jan 1 or Jul 1;
   - U.S. and California Supreme Court decisions affecting bar subjects.

**Update the repo**
- `00-exam-intel/*.md`.
- `config/plan.yml` admissions dates: replace `(est)` with confirmed dates.
- `sources.md`: new `S-###` rows with access date.
- `VERIFY-QUEUE.md`: move resolved items to *Resolved* with the source, and remove their inline tags.
- `recent-changes.md`.

**Flag every plan impact at the top of the reply**, e.g. "the final filing deadline is May 28, not June 1".

Finally, run `python scripts/validate.py` and `python -m pytest -q scripts/tests`, commit (`exam-intel: monthly update <date>`), push, and summarize in 10 lines or fewer.
