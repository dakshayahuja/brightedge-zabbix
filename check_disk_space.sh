#!/bin/bash

# Check all mounted file systems
df -h | awk '{if (NR!=1 && $5+0 > 80) print $0}' > /tmp/disk_usage_report.txt

# If any file system is above 80% usage, alert
if [ -s /tmp/disk_usage_report.txt ]; then
  echo "Disk space usage is above 80%"
  exit 1
else
  echo "Disk space usage is under control"
  exit 0
fi
