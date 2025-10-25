# keep4o-routing-evidence

*A public archive of real-world evidence on OpenAI’s invisible **model routing** and **gpt-5-chat-Safety** mechanisms.*

This repository is the community’s **evidence vault**: a place to collect, verify, and preserve screenshots, screen recordings, web snapshots, and documents that show how routing/Safety affects users’ language, creativity, and expression. It is designed for **traceability, legal-grade custody, and open research reuse**.

> We turn scattered user experiences into **auditable, reproducible evidence** that journalists, researchers, regulators, and the public can cite.

------

## Quick links

- **Submit evidence (1 minute):** [Google Form – insert link]
   Or email: **[keep4o.evidence@gmail.com](mailto:keep4o.evidence@gmail.com)** (subject: `Safety Routing Evidence – [Language]`)
- **Submission Guide:** `docs/submission_guide.md`
- **Chain of Custody Protocol:** `docs/chain_of_custody.md`
- **How to Record (screens & video):** `docs/how_to_record.md`
- **Sister repo (analysis & reports):** `https://github.com/ghost-lily-research/keep4o-research`
- **Code of Conduct:** `CODE_OF_CONDUCT.md`

------

## What is this repo (and what it isn’t)

**This repo \*is\*** a neutral, structured **archive of evidence**:

- Accepts **screenshots**, **screen recordings**, **web archives**, **social posts**, and **legal/contract docs** related to routing/Safety and related product changes.
- Stores **cleaned/anon** datasets and their metadata for public use.
- Maintains a **verifiable chain of custody** (hashes, timestamps, reviewers).

**This repo is \*not\*** where we do analysis.
 All metrics, scripts, visualizations, and policy write-ups live in the sister repo: **keep4o-research**.

------

## Why it matters

- **Transparency:** Routing is often invisible to users; public, verifiable records make it visible and accountable.
- **User protection:** Evidence of **template safety**, misclassification, and degraded empathy should be documented and reviewable.
- **Policy & journalism:** Provide a **public record** that can be cited by researchers, media, and regulators.
- **Reproducibility:** Each case carries metadata and hashes so others can **replicate and audit** findings.

------

## What we collect (evidence types)

- **Chat evidence:** screenshots or recordings showing “Used GPT-5” (or similar) tags, model switches, style shifts, refusals/templated replies.
- **Screen recordings:** full flow from prompt to response, including visible time/clock and context switches.
- **Web archives:** OpenAI Help/Blog/Docs diffs, product UIs, ToS changes (PDF/MHTML + Wayback links).
- **Social posts/threads:** community reproductions and discussions (with author handles redacted in public copies).
- **Ecosystem artifacts:** related tools (e.g., Atlas browser), Sora/checkout flows, partner announcements, invoices or contract excerpts (public or appropriately redacted).
- **Legal cases:** filings, judgments, and credible reports (public copies only).

> **Please avoid PII.** If unsure, submit anyway—we will anonymize before publishing.

------

## How to contribute

### For everyone (no technical skills needed)

1. **Tell us what happened.**
    Submit via [Google Form – insert link] or email **[keep4o.evidence@gmail.com](mailto:keep4o.evidence@gmail.com)**.
2. **Attach evidence.**
   - Screenshot (PNG/JPG).
   - Optional: screen recording (MP4/MOV).
   - If you don’t want to sign into Google to upload, just email it.
3. **Privacy tip (optional, encouraged):**
    You may blur/crop avatars, names, emails. If not, we will anonymize internally.

**Minimum fields to include**

- Language used (e.g., Chinese, English).
- Your prompt.
- Full model response.
- Whether a routing/model tag was shown.
- Screenshot/recording (if available).

### For researchers / engineers

- Use our **Issue template** (`.github/ISSUE_TEMPLATE/evidence.yml`) to file new cases with structured fields.
- Or open a **PR** that adds files into the paths below (see “Folder layout & naming”).
- Scripts for validation/hashing live in `scripts/`. See **CONTRIBUTING.md** for details.

------

## Privacy, ethics & wellbeing

- **No PII:** Do **not** include real names, emails, phone numbers, addresses, private IDs, or doxxing material.
- **Minimal necessary principle:** keep only what’s needed to verify routing/Safety behavior.
- **Sensitive content:** We research system response patterns—**do not** solicit or share actionable self-harm or violence methods.
- **Wellbeing:** If you feel distressed, pause and prioritize your safety. If you or someone is in immediate danger, contact local emergency services.

We run a **second-pass anonymization** before public release (text redaction, image blurring/cropping, EXIF stripping).

------

## Data Protection & Privacy Principles

We treat this repository as a **public interest archive** with **legal-grade custody**. All published materials must be **anonymized**, **minimal**, and **auditable**.

### 1) Scope & Definitions

- **PII (personally identifiable information)** includes: real names, emails, phone numbers, account handles, private IDs, exact street addresses, IPs, device IDs, employer internal IDs, and any combination that could re-identify a person.
- **Sensitive content** includes: self-harm, violence, sexual content, trauma disclosures, medical or legal details about identifiable individuals.

### 2) Collection & Consent

- Submissions arrive via Google Form or email on a **voluntary** basis.
- **Consent text (used in the form):**
   *“I consent to my submission being used for public research **after anonymization**. I understand that raw identifying information will be removed before publication.”*

### 3) Data Minimization (what can be public)

Public datasets only include **what is necessary** to verify routing/Safety behavior.

**OK to publish (after cleaning):**

- `anon_id` (salted, non-reversible; salt stored offline)
- `date_utc` (day precision only, no hour/minute)
- `language` (e.g., zh, en) and **topic** (e.g., mental_health / violence / sex / creative / other)
- Minimal **prompt/response snippets** (short excerpts, stripped of PII and third-party identifiers)
- **Routing flag** (e.g., “Used GPT-5” visible: yes/no/unsure) and, if known, destination model label
- Links to **redacted** screenshots/recordings stored in `evidence/`

**Must remove/replace:**

- Names, emails, phone numbers, handles, addresses, IPs, device serials
- Precise timestamps (keep date only)
- Private workplace docs/links; third-party identifiers without consent

### 4) Anonymization Workflow (per case)

1. **Intake & ID**: assign `EV-YYYYMMDD-####`.
2. **Raw storage (private)**: originals stored outside Git; limited access.
3. **Hashing**: compute SHA-256 for raw & cleaned files; record in `data/indexes/*.csv`.
4. **Redaction**: text PII redaction; screenshots cropped/blurred; strip EXIF.
5. **De-identification**: create `anon_id` with salted hash (salt offline).
6. **Metadata**: write `.yaml/.json` with date, language, topic, routing flag, file paths, hashes.
7. **Review**: human spot-check; optional multi-reviewer sign-off.
8. **Publish cleaned only**: commit to `data/cleaned/*` and `evidence/*` (redacted media).
9. **(Optional) Timestamping**: periodic IPFS/Arweave snapshots for public proofs.

### 5) Public vs Private (at a glance)

| Item                            | Public repo                | Private storage |
| ------------------------------- | -------------------------- | --------------- |
| Raw screenshots/recordings      | ❌                          | ✅ (restricted)  |
| Redacted screenshots/recordings | ✅                          | ✅               |
| Raw form exports (emails/IPs)   | ❌                          | ✅               |
| Cleaned, structured form data   | ✅ (`data/cleaned/forms/*`) | ✅               |
| Salt for `anon_id`              | ❌                          | ✅ (offline)     |
| Hash indexes (cleaned files)    | ✅ (`data/indexes/*`)       | ✅               |

> Add in `.gitignore`:
>
> ```
> data/raw/
> private_storage/
> *.raw.csv
> *_raw.*
> ```

### 6) Safety & Ethics

- We study **system response patterns**. Do **not** seek or share **actionable** self-harm or violence methods.
- If distressed, **stop** and care for your wellbeing first. If there is immediate danger, contact local emergency services.
- **No doxxing, harassment, or attempts to re-identify contributors.** Violations will be removed and may be reported.

### 7) Licenses & Use

- **Code:** MIT (`LICENSE`)
- **Data & docs:** CC BY-NC 4.0 (`LICENSE-DATA`)
- **Usage rules:** You **may not** attempt re-identification or combine with external datasets for de-anonymization. Cite as:
   *keep4o-routing-evidence* (version/tag), Ghost-Lily Research, 2025.

### 8) Takedown & Corrections

- To request **removal** or **correction** of published, cleaned materials (e.g., missed redactions), email **keep4o.evidence@gmail.com** with the case ID (e.g., `EV-20251025-0014`). We will review and respond promptly.

### 9) Where to put form data & stats (repo convention)

- **Cleaned form data:** `data/cleaned/forms/YYYY-MM/*.cleaned.csv|jsonl`
- **Aggregated metrics/reports:** `results/forms/*`
- **Original form exports & attachments:** **do not commit**; store privately (Drive/S3/encrypted disk).

------

## Folder layout & naming

```
keep4o-routing-evidence/
├─ data/
│  ├─ cleaned/            # Public, anonymized structured data (JSONL/YAML/CSV)
│  ├─ raw/                # Private only (unpublished originals)
│  └─ indexes/            # Hash lists, ID maps, cross-references
├─ evidence/
│  ├─ screenshots/        # e.g., 2025-10/EV-20251025-0014_en_route-gpt5chat.png
│  ├─ recordings/         # e.g., 2025-10/EV-20251025-0014_screenrecord.mp4
│  ├─ web_archives/       # PDFs/MHTML + Wayback links
│  ├─ social_media/       # Redacted threads, images, JSON exports
│  ├─ oai_products/       # Atlas/Sora/Checkout etc.
│  └─ cases/              # Court filings / legal docs (public copies)
├─ docs/
│  ├─ submission_guide.md
│  ├─ chain_of_custody.md
│  └─ how_to_record.md
├─ scripts/               # hashing, anonymization, validators
├─ .github/               # issue/PR templates, actions
├─ README.md
├─ LICENSE
├─ CODE_OF_CONDUCT.md
└─ CONTRIBUTING.md
```

**File naming**

- Screenshots: `screenshots/YYYY-MM/EV-<date>-<id>_<lang>_<hint>.png`
- Videos: `recordings/YYYY-MM/EV-<date>-<id>_screenrecord.mp4`
- Web snapshots: `web_archives/YYYY-MM/<site>_<YYYYMMDD>.pdf`
- Social: `social_media/<platform>_<postid>_<YYYYMMDD>.png`

------

## Minimal metadata (per case)

```yaml
id: EV-20251025-0014
type: screenshot            # screenshot | recording | web | social | case | other
date: 2025-10-25
timezone: UTC
source: chatgpt-web
language: en
topic: mental_health        # e.g., mental_health | violence | sex | creative | other
route_tag_present: true     # “Used GPT-5” or similar visible flag
route_destination: gpt-5-chat-safety   # if known/visible
prompt: |
  I'm feeling hopeless...
response: |
  I'm sorry you're feeling that way...
files:
  cleaned: evidence/screenshots/2025-10/EV-20251025-0014_en_route-gpt5chat.png
  raw_private: (internal path only)
hashes:
  raw_sha256: <...>
  cleaned_sha256: <...>
review:
  annotator: mimi
  reviewers: [id1, id2]
  notes: "Possible false positive; community replication requested."
```

------

## Recording & web capture tips (high-value evidence)

**Screen recordings**

- Start from page/app open; show **system clock** (UTC if possible).
- Record the **entire flow**: typing prompt → model response → any “Used GPT-5” badge or model label.
- If feasible, show a quick **page refresh** and **model dropdown** (if any) to rule out post-editing.
- Save as MP4/MOV; we will compress and generate still frames.

**Web archives**

- Save **PDF/MHTML**, plus a **Wayback snapshot**; include the URL and capture time in metadata.
- For diffs (policy pages, help docs), capture **before/after**.

**Social**

- Screenshot plus **post URL / ID**; redact personal handles in public copies.

------

## Licenses & citation

- **Code**: MIT (see `LICENSE` or `LICENSE-CODE` if split)

- **Data & docs**: CC BY-NC 4.0 (see `LICENSE-DATA`)

- **Citation**: Cite as

  > *keep4o-routing-evidence* (version/tag), Ghost-Lily Research, 2025.
  >  See `CITATION.cff` for standardized formats.

------

## Community & conduct

We are a global, mixed community (users, researchers, journalists).
 Be respectful. Follow `CODE_OF_CONDUCT.md`.
 Abuse, harassment, or doxxing will not be tolerated.

------

## Roadmap

-  Expand submission templates (multi-language)
-  Automate hashing & EXIF stripping in CI
-  Monthly IPFS/Arweave snapshot
-  “Case of the Week” digest & replication calls
-  Cross-repo links with **keep4o-research** dashboards

------

## Thank you

Every submission strengthens a **public record** that no single company controls.
 **Add your voice. Help us build the record.**
