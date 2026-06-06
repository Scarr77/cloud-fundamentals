# Linux System Infrastructure Automation

## 📋 Overview
This directory contains production-ready Bash scripts designed to automate system administration and monitoring tasks. In enterprise data center operations, tracking system metrics and keeping precise log records is critical for maintaining high availability and catching resource constraints before they cause system downtime.

## 🛠️ Featured Script: `system_health.sh`
This script acts as a lightweight resource monitor that evaluates the primary subsystems of a Linux server: **Storage, RAM, and CPU.**

### Key Features & Infrastructure Concepts Demonstrated:
* **Automated Log Rotation/Appends:** Simulates basic enterprise `syslog` or logging workflows by sending timestamped statuses to a centralized log file (`/var/log/system_health.log`).
* **Threshold Metrics:** Utilizes programmatic conditional logic to differentiate between normal operating parameters (`[OK]`) and resource exhaustion events (`[CRITICAL]`).
* **Linux CLI Toolkit Integration:** Leverages foundational system utilities including `df`, `free`, `uptime`, `awk`, and `sed` to extract and parse raw data on the fly.

### How to Run Locally
1. Grant execution permissions to the script:
   ```bash
   chmod +x linux-automation/system_health.sh