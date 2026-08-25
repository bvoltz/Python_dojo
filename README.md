# Python_dojo

# 🥋 Python Automation Dojo: Wax On, Wax Off

Welcome to my Python automation training ground. This repository tracks my journey from a complete beginner to a professional automation engineer through daily repetition, defensive coding habits, and muscle memory training.

## 🎯 The Routine (`wax_on.py`)
This script serves as my daily baseline practice. It is designed to drill the fundamental DNA of automated systems: data handling, defensive exception tracking, file manipulation, and real-time execution logging.

### Key Concepts Practiced Daily:
*   **Data Layout:** Manipulating native Python Lists (`[]`) and Dictionaries (`{}`) to map machine statuses.
*   **The Shield (Error Handling):** Implementation of active `try/except` safeguards to ensure background processes never crash silently.
*   **The Trail (File I/O):** Utilizing safe `with open()` constructs to automatically manage and write system log files without memory leaks.
*   **Dynamic Injection:** Harnessing f-strings to inject live, 24-hour military-grade `datetime` timestamps into outputs.

## 🛠️ How It Works
When executed, the system safely processes a simulation of background tasks, validates their status, and instantly outputs a synchronized report to the terminal and a local log file:

```text
Automation Initialize at 2026-08-24 08:54:58...
SUCCESS: clean_logs completed.
ERROR: backup_db failed.
SUCCESS: send_report completed.
```

## 📈 My Training Schedule
*   **Days 1–20:** Build perfect syntax execution and flawless layout alignment.
*   **Day 21:** Inject intentional failures to stress-test the defensive error handling.
*   **Days 22+:** Speed run validation (flawless script deployment under 120 seconds).


## 🧠 Deep Dive
* To understand the core mental model behind this script, read the [Automation Concept Guide](CONCEPT_GUIDE.md).
