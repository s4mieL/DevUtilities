# Demo Payload (Safe)

This folder contains a **safe demonstration payload** used for educational purposes. The script shows how a payload hook can be executed without performing any destructive or harmful actions.

The demo simply changes the Windows desktop wallpaper to a local image file.

---

## Purpose

* Demonstrate payload execution in a controlled, visible way
* Provide a harmless example for testing orchestration or anti‑VM triggers
* Avoid destructive behavior while still proving code execution

---

## Requirements

* Windows OS
* Python 3.x
* A local image file (e.g., `wallpaper.jpg`) in the same directory

---

## Usage

Place an image named `wallpaper.jpg` in this folder, then run:

```bash
python demo_payload.py
```

If successful, your desktop wallpaper will change to the image.

---

## Safety Notes

* This script performs **no destructive actions**
* It does not modify system files or registry entries beyond the standard wallpaper setting
* The effect is fully reversible by changing your wallpaper normally

---

## Educational Context

This payload is intended to accompany anti‑VM / sandbox detection demonstrations.
It provides a clear visual confirmation that a payload would execute on a real system while remaining safe for testing and learning.
