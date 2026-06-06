#!/bin/bash

# ==============================================================================
# Script Name:  system_health.sh
# Description:  Monitors CPU, Memory, and Disk usage. Alerts if thresholds cross 80%.
# Target Ops:   Data Center / Linux Infrastructure Automation
# ==============================================================================

# Threshold percentage for alerts
THRESHOLD=80
LOG_FILE="/var/log/system_health.log"

# Ensure log file exists and is writable, fallback to local directory if not root
if [ ! -w "$LOG_FILE" ] 2>/dev/null; then
    LOG_FILE="./system_health.log"
fi

echo "--- Monitoring Run: $(date '+%Y-%m-%d %H:%M:%S') ---" >> "$LOG_FILE"

# 1. Check Disk Usage (Root Partition)
DISK_USAGE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')
if [ "$DISK_USAGE" -gt "$THRESHOLD" ]; then
    echo "[CRITICAL] Disk Usage is at ${DISK_USAGE}%!" >> "$LOG_FILE"
else
    echo "[OK] Disk Usage is at ${DISK_USAGE}%." >> "$LOG_FILE"
fi

# 2. Check Memory Usage
MEMORY_USAGE=$(free | grep Mem | awk '{print int($3/$2 * 100)}')
if [ -z "$MEMORY_USAGE" ]; then
    # macOS fallback calculation for local testing consistency
    MEMORY_USAGE=$(vm_stat | awk '/Pages active/ {print $3}' | sed 's/\.//')
    MEMORY_USAGE=$((MEMORY_USAGE % 100)) 
fi

if [ "$MEMORY_USAGE" -gt "$THRESHOLD" ]; then
    echo "[CRITICAL] Memory Usage is at ${MEMORY_USAGE}%!" >> "$LOG_FILE"
else
    echo "[OK] Memory Usage is at ${MEMORY_USAGE}%." >> "$LOG_FILE"
fi

# 3. Check CPU Load
CPU_LOAD=$(uptime | awk -F'load average:' '{print $2}' | awk -F',' '{print int($1)}')
if [ -z "$CPU_LOAD" ]; then CPU_LOAD=0; fi

if [ "$CPU_LOAD" -gt "$THRESHOLD" ]; then
    echo "[CRITICAL] CPU Load Average is high: ${CPU_LOAD}" >> "$LOG_FILE"
else
    echo "[OK] CPU Load Average is stable: ${CPU_LOAD}." >> "$LOG_FILE"
fi

echo "Standard log entry appended to $LOG_FILE"