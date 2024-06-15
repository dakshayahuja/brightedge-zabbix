#!/usr/bin/env python3
import subprocess

def check_disk_space():
    result = subprocess.run(['df', '-h'], capture_output=True, text=True)
    lines = result.stdout.splitlines()

    for line in lines[1:]:
        parts = line.split()
        usage = int(parts[4].strip('%'))
        if usage > 80:
            return "True"

    return "False"

if __name__ == "__main__":
    print(check_disk_space())
