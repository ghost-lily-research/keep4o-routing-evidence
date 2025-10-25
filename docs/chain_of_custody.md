# Chain of Custody Protocol

Each accepted case follows these steps:
1) Intake & ID assignment (EV-YYYYMMDD-####)
2) Raw storage in a private location (restricted access)
3) Hashing (sha256) for raw and cleaned assets
4) Anonymization (text redaction, image crop/blur, EXIF strip)
5) Metadata file created (.yaml/.json)
6) Human review & sign-off
7) Publish cleaned assets to the public repo
8) Optional: IPFS/Arweave timestamping
9) Encourage independent replication in the research repo
