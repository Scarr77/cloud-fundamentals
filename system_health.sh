#!/bin/bash

# Configuration: Set the paths for your system logs
LOG_FILE="system_health.log"
THRESHOLD=80

echo "==========================================" >> $LOG_FILE
echo "System Health Check - $(date)" >> $LOG_FILE
echo "==========================================" >> $LOG_FILE

# 1. Check Disk Space Usage on Core Partitions
DISK_USAGE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')
echo "Storage Utilization: ${DISK_USAGE}%" >> $LOG_FILE

if [ "$DISK_USAGE" -gt "$THRESHOLD" ]; then
    echo "🚨 WARNING: Disk Space Utilization has crossed critical threshold of ${THRESHOLD}%!" >> $LOG_FILE
else
    echo "✅ Storage performance within operational tolerances." >> $LOG_FILE
fi

# 2. Check Memory (RAM) Allocation Stability
FREE_MEM=$(free -m | awk 'NR==2 {print $4}')
TOTAL_MEM=$(free -m | awk 'NR==2 {print $2}')
echo "Available Memory Resources: ${FREE_MEM}MB out of ${TOTAL_MEM}MB" >> $LOG_FILE

echo "System check completed successfully." >> $LOG_FILE
echo "" >> $LOG_FILE