# Utilities — Developer Tools Collection

Welcome to **Utilities**, a collection of general developer-focused scripts and tools created for educational, productivity, and experimental purposes. This repository is designed to showcase modular utilities that can assist with system monitoring, automation, and other technical experiments.

---

## Repository Structure

```
Utilities/
 ├─ anti_vm/               # Educational anti-VM / sandbox detection utilities
 │    ├─ anti_vm.py        # Anti-VM detection logic
 │    ├─ 2nd_stage.py      # Safe demo payload
 │    └─ README.md         # Notes and usage instructions
 ├─ grabber-base/          # A Grabber Startup
 │    └─ anti_vm.py        # a simple grabber framework (only works for v10,v11)
 ├─injector/
 │    └─ obfuscated-injector.js # a injector
 └─ README.md              # This file
```

---

## Sections Overview

### 1. Anti-VM / Sandbox Utilities

This section contains educational tools that demonstrate system awareness and sandbox detection techniques. **Warning:** Some scripts can be destructive (e.g., process termination, self-deletion) if run directly. They are provided for learning purposes only.

* **anti_vm.py** — Detects virtual machines and sandboxed environments.
* **2nd_stage.py** — A safe demonstration that shows payload hooks without causing harm.



---

### 2. Grabber Frameowork

This section contains educational examples showing how token‑grabbing malware targets Discord credentials. 
**Warning:** Running these scripts on a real environment may expose sensitive account data. They are provided solely for cybersecurity research and defensive learning.

* **main.py** — A Simple Grabber Startup framework, might be outdated, since it only supports v10,v11 app-bound encryption, and today's encryption method by most chromium browsers uses v20!

### 3. Injector

This section contains educational tool showing how token-grabbing malware works under the hood, it is inspired from the
Black Grabber (A Open Source Project)specially thanks to the author and his community providing us an insight on how it works under the hood
even though their projects ends in mid August, 2023 but they left us an impact on how this complex software works!

> ⚠️ Always run these scripts in a controlled or virtual environment.
---

## Usage Instructions

* Each subfolder contains its own README.md explaining how to safely run and understand the scripts.
* Always read warnings and instructions before executing any script.

---

## Contribution & Educational Use

This repository is intended for **educational purposes**. You are welcome to study, modify, and extend the scripts, but please:

* Do not use these tools for malicious purposes
* Respect licensing if you incorporate other libraries
* Always run potentially destructive scripts in safe, controlled environments

---

## Contact

**Developer:** s4miEL
**GitHub:** [https://github.com/s4miel](https://github.com/s4miEL)

If you have questions, suggestions, or are interested in collaboration, feel free to reach out.
