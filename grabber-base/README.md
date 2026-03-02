# Discord Token Grabber (Legacy Demo)

This folder contains a **legacy demonstration of a Discord token grabber concept** for educational and research purposes.  
It illustrates how early token‑extraction techniques targeted local client storage.

**Note:** Modern Discord clients and browsers have significantly improved security, and this approach is largely obsolete.

---

## Purpose

* Demonstrate how applications may store authentication tokens locally
* Show why secure storage and encryption mechanisms matter
* Provide historical context for malware analysis and defense education
* Help learners understand token‑based authentication risks

---

## How It Worked (Historically)

Early grabbers searched local Discord or browser storage paths for plaintext or weakly protected tokens, such as:

* Local storage / LevelDB files
* Cached session data
* Application data directories

Extracted tokens could then be used to impersonate a session without a password.

---

## Requirements

* Windows OS
* Python 3.x+ (3v and above)
* Discord desktop client (older storage models)

---

## Usage

Run the demonstration script in a controlled test environment:

```bash
python grabber_demo.py
